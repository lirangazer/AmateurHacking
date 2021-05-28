"""
this python script provide system for the amateur hacker
the file will implement hash encryption , caesar cipher hack , MSSP encryption
"""
import sys
import subprocess
import os
import hashlib

"""
this method install the cryptography package 
"""
try:
    from cryptography.fernet import Fernet
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'cryptography'])
    from cryptography.fernet import Fernet


def fernet_encrypt():
    """
    this function operate fernet encryption
    :return: the string after hash function
    """
    print("this is Fernet function")
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(bytes(input("enter word: "), 'ascii'))
    plain_text = cipher_suite.decrypt(cipher_text)
    print("Cipher text is: ", cipher_text)
    print("Key is: ", key)
    print("Plain text is:", plain_text)


def hash_encrypt():
    """
    this function operate hash encryption
    :return: the string after hash function
    """
    print("this is hash function")
    hash_string = input("enter your word: ")
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    print(sha_signature)
    while True:
        exit_function = input("to return main menu press Q/q : ").lower()
        if exit_function == 'q':
            return
        else:
            print('this is wrong value please try again')


def encrypt(encrypt_text, key):
    """
this function simulate the caesar cipher encrypt
    :param encrypt_text:
    :param key:
    :return:
    """
    result = ""
    for i in range(len(encrypt_text)):
        char = encrypt_text[i]
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result


def decrypt(encrypt_text, key):
    result = ""
    for i in range(len(encrypt_text)):
        char = encrypt_text[i]
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return result


def caesar_cipher_break(encrypt_text):
    """
this function will break caesar cipher
    :param encrypt_text:
    """
    table = {}
    print("this is caesar_cipher function")
    encrypt_text = input("enter word: ")

    for key in range(26):
        table[key] = decrypt(encrypt_text, key)
    print(table)
    while True:
        exit_function = input("to return main menu press Q/q : ").lower()
        if exit_function == 'q':
            return
        else:
            print('this is wrong value please try again')


def mssp():
    print("this is MSSP function")
    cypher_text = input("please enter the cypher text: ")
    n = int(input("enter the number of array: "))
    m = int(input("enter the number of array members : "))
    d = int(input("enter the number of  size of array members : "))
    if len(cypher_text) != (n*m*d):
        raise Exception("there was error in the input text check if the encrypt text valid to the algorithm")
    else:
        pass



def main():
    """
this is the main function
    """

    while True:
        try:
            choice = int(input("\n##########-Welcome to the Amateur Hacker menu-##########\n"
                               "\t1. encrypt text using hash function \n"
                               "\t2. break the Caesar cipher  \n"
                               "\t3. using MSSP encryption   \n"
                               "\t4. exit   \n"
                               "########################################################\n"
                               "please choose option from the menu : "))
            if choice == 1:
                encrypt_choice = int(input("\n##############choose your encryption##########\n"
                                           "\t1.Fernet encryption \n"
                                           " \t2. sha-256\n"
                                           "###################################################\n"
                                           "choose your encryption: "))
                if encrypt_choice == 1:
                    fernet_encrypt()
                elif encrypt_choice == 2:
                    hash_encrypt()
                else:
                    raise Exception
            elif choice == 2:
                text = input("please enter a word to break: ")
                key = int(input("please enter a key for encryption: "))
                encrypt_text = encrypt(text, key)
                print(encrypt_text)
                caesar_cipher_break(encrypt_text)
            elif choice == 3:
                mssp()
            elif choice == 4:
                break
            else:
                raise Exception(sys.stderr)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
