# importing the library to encrypt the messages
from cryptography.fernet import Fernet

#generating the key
key = Fernet.generate_key()

# storing the key in in a file secret.key and using variable keyfile
keyfile = open("secret.key", "wb")
keyfile.write(key)
keyfile.close()

#message = "message I want to encrypt".encode()

message_box=input("Enter the text you want to encrypt: ")
message = message_box.encode() # fernet classes ( encode )

# loading the key from the secret.key
load_key=open("secret.key", "rb").read()
f = Fernet(load_key)
encrypted_message = f.encrypt(message)  

# storing the encrypted message in the file name data.file
data = open("data.file", "wb")
data.write(encrypted_message)
data.close()

print("\n",encrypted_message)


#decrypted_message = f.decrypt(encrypted_message)
#print(decrypted_message)