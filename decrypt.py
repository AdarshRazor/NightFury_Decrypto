from cryptography.fernet import Fernet
from tkinter import filedialog
import tkinter as tk 
import os

def decryption():
    s = filedialog.askopenfilename(title = 'Choose the key file location')
    load_key=open(s, "rb").read()
    f = Fernet(load_key)

    #load_key=open("secret.key", "rb").read()
    #f = Fernet(load_key)

    tk.Tk().withdraw()
    p = filedialog.askopenfilename(title = 'Choose the file location')
    #path = os.path.dirname(p)
    data=open(p, "rb").read()
    decrypted_message = f.decrypt(data)

    #print(decrypted_message)

    data_file = open("result.txt", "wb")
    data_file.write(decrypted_message)
    data_file.close()

    '''yesno=input("Do you want to delete the Key and Data ? (Y/N): ")
    if yesno=="Y" or yesno=="y":
        os.remove("secret.key")
        os.remove("data.file")
    else:
        exit()'''

    os.remove(s)
    os.remove(p)