from cryptography.fernet import Fernet
from tkinter import filedialog
import tkinter as tk 
import os
import time

def decryption():
    print("\nChoose the data.file to decrypt it")
    time.sleep(2.5)
    p = filedialog.askopenfilename(title = 'Choose the file location', filetypes=[("file type", ".file")])
    print("\nSelect the secret key")
    time.sleep(2.5)
    s = filedialog.askopenfilename(title = 'Choose the key file location',filetypes=[("secret key", ".key")])
    load_key=open(s, "rb").read()
    f = Fernet(load_key)
    tk.Tk().withdraw()
    data=open(p, "rb").read()
    decrypted_message = f.decrypt(data)
    
    data_file = open("result.txt", "wb")
    data_file.write(decrypted_message)
    data_file.close()

    os.remove(s)
    os.remove(p)
