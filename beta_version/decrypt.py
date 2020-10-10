# importing the cryptography function to encrypt or decrypt
from cryptography.fernet import Fernet
# importing os to handle the system files
import os

# load the key to decrypt the message
load_key=open("secret.key", "rb").read()
f = Fernet(load_key)

# loading the encrpyted file
data=open("data.file", "rb").read()

#encrypted_message=input()

# decrypt function
decrypted_message = f.decrypt(data)

print(decrypted_message)

# deleting both the files after the message is received
os.remove("secret.key")
os.remove("data.file")