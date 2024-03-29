import sys
import time
from cryptography.fernet import Fernet
from tkinter import filedialog
import tkinter as tk 
import encryption
import glob, os
import decrypt
from fsplit.filesplit import Filesplit
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
                p="../"
                os.chdir(p)
                print(os.getcwd())
                os.system("python megaauth.py")
                break
            else:
                break   

    elif main_input==2:
        fs = Filesplit()
        folder_selected = filedialog.askdirectory(title = 'Choose the directory file location')
        fs.merge(input_dir=folder_selected)
        os.chdir(folder_selected)
        os.remove("./fs_manifest.csv")
        filename=[]
        
        #os.chdir("./output/divided")
        
        for file in glob.glob("*.file"):
            filename.append(file)
        for i in range(len(filename)-1):
            os.remove(filename[i+1])
        
        decrypt.decryption()

        print("Please check the download folder for the result file.")
        print("Thank for using Nightfury_Decrypto !!")
    else:
        exit
