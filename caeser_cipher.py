import smtplib  #for email protocol

print("\nWelcome to Caesar's Cypher!\n")


def cipher_or_decipher():  # function that runs the cipher and decipher
    ciph_or_deciph = input('Do you want to cipher (c) or decipher (d) a code? ')
    if ciph_or_deciph == ('c' or "cipher"):
        key = int(input('Great! To get started choose a number for you secret key: '))  # numerical encryption key
        newString = ""    # initializes new message variable as blank space
        message = input('Please enter a message: ')  # message to be encrypted
        for character in message:  # loop that runs through every character in the message and sets new index
            newChar = ord(character) + key
            newString = newString + chr(newChar)
        print('The new message is: ' + newString)
    elif ciph_or_deciph == ('d' or "decipher"):  # to decipher messages
        deciph_key = int(input('To decipher a message, enter your key: '))
        decrypted_message = ""
        encrypted_message = input('Please enter your encrypted message: ')
        for character in encrypted_message:
            decryptedChar= ord(character) - deciph_key
            decrypted_message= decrypted_message + chr(decryptedChar)
        print('The original message was: ' + decrypted_message)
    else:
        print("Sorry, that is not a valid option. Please try again.")
        cipher_or_decipher()


def play_again():  # function to let user cipher or decipher another message
    another_round = input("Do you want to cipher or decipher another message? y or n:")
    while another_round == "y":
        cipher_or_decipher()
        another_round = input("Do you want to cipher or decipher another message? ")
    print("Ok, thanks for using the cipher!")


def send_email():  # function to send an email. Can be used to send encrypted message.
    email = input("Would you like to send your message in an email? y or n ")
    if email == 'y':
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.ehlo()
        smtp_obj.starttls()
        smtp_obj.login(input("Please input email address you wish to login to: "),
                       input("Please input email password: "))
        smtp_obj.sendmail(input("Please input sender's email address: "),
                          input("Please input receiver's email address: "),
                          "Subject: " + input("Please input Subject line: ") + "\n" +
                          input("Please input message to be sent: "))
        smtp_obj.quit()
    else:
        print("Ok, maybe next time!")


cipher_or_decipher()
play_again()
send_email()