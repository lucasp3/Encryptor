import sys
import os
import pyperclip


def copy(data):
    question = input("Copy to clipboard? ")

    if question.lower() == 'yes' or question.lower() == 'y' or question.lower() == 'ja':
        pyperclip.copy(data)
        print("Encrypted message copied to clipboard.")
        rerun()

    elif question.lower() == 'no' or question.lower() == 'n' or question.lower() == 'nej' or question.lower() == 'nein':
        rerun()

    else:
        print("You did not enter a valid input.")
        copy(data)


def rerun():
    ask = input("\nWould you like to run this program again? ")

    if ask.lower() == "yes" or ask.lower() == "y" or ask.lower() == 'ja':
        print(" ")
        run()

    elif ask.lower() == 'no' or ask.lower() == 'n' or ask.lower() == 'nej' or ask.lower() == 'nein':
        sys.exit("\nThank you!")

    else:
        print("You did not enter a valid input.")
        rerun()


def encrypt(key, msg):
    encrypted_message = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encrypted_message.append(chr((msg_c + key_c) % 127))
    return ''.join(encrypted_message)


def decrypt(key, encrypted):
    msg = []
    for i, c in enumerate(encrypted):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)


def run():
    function_type = input("Would you like to encrypt or decrypt a message? ")
    encrypted = None

    if function_type.lower() == "encrypt" or function_type.lower() == "e":
        key = input("\nKey: ")
        msg = input("Message: ")
        data = encrypt(key, msg)
        enc_message = "\nYour encrypted message is: " + data
        print(enc_message)
        copy(data)

    elif function_type.lower() == "decrypt" or function_type.lower() == "d":
        key = input("\nKey: ")

        question = input("Paste encrypted message from clipboard? ")

        if question.lower() == 'yes' or question.lower() == 'y':
            encrypted = pyperclip.paste()
            print("Message: " + encrypted)

        elif question.lower() == 'no' or question.lower() == 'n':
            encrypted = input("Message: ")

        else:
            print("You did not enter a valid input.")
            run()

        decrypted = decrypt(key, encrypted)
        decrypted_message = "\nYour decrypted message is: " + decrypted
        print(decrypted_message)
        copy(decrypted)

    else:
        print("\nYou did not enter a valid input.\n")
        run()

run()
