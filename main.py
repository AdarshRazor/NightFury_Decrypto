import sys
import time
import os
from cryptography.fernet import Fernet
from tkinter import filedialog
import tkinter as tk 
import encryption
import decrypt
from encryption import key


def print_slowt(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)

##############         printing the heading             #####################

if __name__ == "__main__":
    os.system('cls')
    print_slowt('''
                                    WELCOME  to    
                    ____
    |*    |  ----  |    |  |    |  -----        |-----  |    |  |-----|  |    |
    | *   |   |    |       |    |    |          |       |    |  |     |  |    |
    |  *  |   |    |       |----|    |          |-----  |    |  |-----|  |____|
    |   * |   |    |  --|  |    |    |          |       |    |  |  *       |
    |    *|  ----  |____|  |    |    |          |       |____|  |    *;    |

    ''')

    ################      main menu        #####################################

    

    print_slow("\nCollecting data ....")
    print_slow("\nLoading ......")
    print_slow("\n\nSelect the option to encrypt or decrypt")
    print("\n\n1. Encrypt")
    print("2. Decrypt")
    print("0. Exit")
    main_input=int(input("\nEnter the choice: "))

    if main_input==1:
        while(1):
            os.system("cls")
            print("\n1. Enter the Message")
            print("2. Print and Export Key")
            print("3. Locate the file")
            print("4. Exit\n")    
            option=int(input("Enter the Choice: "))

            if option==1:
                message=input("Enter the message: ")
                encryption.encryption_message(message,key)
                break
            elif option==2:
                print("Key is stored with file name - secret.key\n",key)
                encryption.export_key()
                break
            elif option==3:
                tk.Tk().withdraw()
                p = filedialog.askopenfilename(title = 'Choose the file location')
                message=open(p, "rb").read()
                print(p)
                encryption.encrypting_file(message,key,p)
                break
            else:
                break   

    elif main_input==2:
        decrypt.decryption()
        '''
        s = filedialog.askopenfilename(title = 'Choose the key file location')
        load_key=open(s, "rb").read()
        f = Fernet(load_key)

        #load_key=open("secret.key", "rb").read()
        #f = Fernet(load_key)

        tk.Tk().withdraw()
        p = filedialog.askopenfilename(title = 'Choose the file location')
        #path = os.path.dirname(p)
        data_dec=open(p, "rb").read()
        decrypted_message = f.decrypt(data_dec)

        #print(decrypted_message)

        data_file = open("result.txt", "wb")
        data_file.write(decrypted_message)
        data_file.close()
        os.remove(s)
        os.remove(p)
        '''

    else:
        exit