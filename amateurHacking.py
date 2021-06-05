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


def calcSubsetSum(nums, i, sum, strArr):
    """
    this function take from class slideshow that implement the calculation of sub set sum
    :param nums: is the array of numbers the we get to calculate
    :param i: is parameter that needs for the recursion
    :param sum: is the sum we want to get
    :param strArr: this is empty string that needed for return the solution
    :return: the sub set sum of the arrays
    """
    res = False
    if (sum == 0):
        res = True
        # print(strArr)
    elif (i >= len(nums)):
        res = False
    else:
        res = calcSubsetSum(nums, i + 1, sum - nums[i], strArr + str(nums[i]) + " ") or calcSubsetSum(nums, i + 1, sum, strArr)
    return res


def calcSubsetSumOver(nums, sum):
    """
    help function the init the calcSubsetSum function
    :param nums: the array that given by the calling function
    :param sum: the sum that given by the calling function
    :return: the sub set sum that get from calcSubsetSum function
    """
    return calcSubsetSum(nums, 0, sum, "")


def found_min(array_min):
    """
    this function helping to found the  minimum number in the array
    :param array_min: get  array from calling function
    :return: the minimum number
    """
    return min(array_min)


def found_min_sum(array_min_sum):
    """
    this function helping to found the  sum of the array
    :param array_min_sum:get the array form the calling function
    :return: the summation of the array
    """
    return sum(array_min_sum)


def mssp():
    print("this is MSSP function")
    cypher_text = str(input("please enter the cypher text: "))
    n = int(input("enter the number of arrays :  "))
    m = int(input("enter the number of array members : "))
    d = int(input("enter the number of  size of array members : "))
    len_cypher_text, len_to_split_n = len(cypher_text), int(len(cypher_text) / n)
    len_to_split_m = int(len_to_split_n / m)
    new_cypher_after_m = []
    if len(cypher_text) != (n * m * d):
        raise Exception("there was error in the input text check if the encrypt text valid to the algorithm")
    else:
        new_cypher_after_n = [cypher_text[i:i + len_to_split_n] for i in range(0, len_cypher_text, len_to_split_n)]
        #print(new_cypher_after_n)
        for m_list in new_cypher_after_n:
            new_cypher_after_m.append(
                [int(m_list[i:i + len_to_split_m]) for i in range(0, len(m_list), len_to_split_m)])
        # this print is for developing peppers
        # print(new_cypher_after_m[0])
        """
        this is a help array to get all the minimum numbers from all arrays
        """
        smin = []
        """
                this is a help array to get all the sums  from all arrays
        """
        min_sum = []
        for i in new_cypher_after_m:
            smin.append(found_min(i))
            min_sum.append(found_min_sum(i))
        """
                this is a verbal to get  the maximum  number from the minimum array
        """
        smin_max = max(smin)
        """
                this is a help verbal to get  the minimum summation  from all  sums array
        """
        min_of_sums = min(min_sum)

        for sum_1 in range(smin_max, min_of_sums):
            counter = 0
            for array_of_nums in new_cypher_after_m:
                if calcSubsetSumOver(array_of_nums, sum_1):
                    print("hacking ....")
                    counter += 1
            if counter == n:
                final_sum = sum_1
        print("the plain text is: %s" % final_sum)


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
