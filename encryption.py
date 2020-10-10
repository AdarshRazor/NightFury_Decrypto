'''
Night_Fury v2.0

AdarshRazor
10.10.2020 06:30AM
'''

from cryptography.fernet import Fernet
from tkinter import filedialog
import tkinter as tk 
import os

def encryption_message(message,key,path="./output"):
    print(message)
    en_message=message.encode()
    k=Fernet(key)
    encrypted_message=k.encrypt(en_message)
    os.system('cls')
    print("Message is encrypted !!")
    print("1. Print message")
    print("2. Export file")

    option_encryption_message=int(input("\nEnter option :"))

    if(option_encryption_message==1):
        print("\n",encrypted_message)
    elif(option_encryption_message==2):
        print("Exporting file and secret key")
        os.chdir(path)
        data_file = open("data.file", "wb")
        data_file.write(encrypted_message)
        data_file.close()
        export_key()
        exit()
    else:
        breakpoint

def encrypting_file(message,key,path):
    k=Fernet(key)
    encrypted_message=k.encrypt(message)
    os.system('cls')

    x="/"
    p=path.split(x)
    p.pop()
    p.append("output")
    p=tuple(p)
    path=x.join(p)

    print("Message is encrypted !! Check the ouput folder")
    #print("\n",encrypted_message)
    print("Exporting file and secret key")
    os.chdir(path)
    data_file = open("data.file", "wb")
    data_file.write(encrypted_message)
    data_file.close()
    export_key()


def export_key():
    key_file=open("secret.key", "wb")
    key_file.write(key)
    key_file.close()

############ main program

key=Fernet.generate_key()

os.system('cls')
print("\nWelcome to Encry_Decry")
print("\n1. Enter the Message")
print("2. Print and Export Key")
print("3. Locate the file")
print("4. Exit\n")


option=int(input("\nEnter the option: "))

while 1:
    #option=int(input("\nEnter the option: "))
    if option==1:
        message=input("Enter the message: ")
        encryption_message(message,key)
        break
    elif option==2:
        print("Key is stored with file name - secret.key\n",key)
        export_key()
        break
    elif option==3:
        tk.Tk().withdraw()
        p = filedialog.askopenfilename(title = 'Choose the file location')
        message=open(p, "rb").read()
        print(p)
        encrypting_file(message,key,p)
        break
    else:
        break