# NightFury_Decrypto

### What is NightFury_Decrypto

A basic sript to encrypt and decrypt your data. Where the main catch is to deliver the encrypted file to the reciever.
It divides the encrypted file into 4 or more parts and then send it to the reciever. Even if hacker manages to get his/her hands on the file, in order to decrypt it, other file will be required as it will make the file more secured from hackers.

---

### Installation

First install the requiement.txt using following command in cmd in that particular folder.
```bash
pip install -r requirements.txt (Python2) 
pip3 install -r requirements.txt (Python3)
```
---

### Usuage

There are 2 files depends on the user desire. [encryption.py](https://github.com/AdarshRazor/NightFury_Decrypto/blob/main/encryption.py) and [decrypt.py](https://github.com/AdarshRazor/NightFury_Decrypto/blob/main/decrypt.py) which do as per their given names.

In order to encrypt the file. Type the following command in CMD.
```python
python encryption.py
```

> User can select from the 2 options of encryption and other print out the export the key(encryption key)


![alt text](https://github.com/AdarshRazor/NightFury_Decrypto/blob/main/imgs/1.PNG "selection menu")


> **Encryption**


1. You can enter the short messages and it will encrypt it and while giving the output it will ask either to print it or to store it in the file. Along with the file one secret.key will be exported in the output folder which will be you  encryption/decryption key

2. User can print the encryption/decryption key to view the secret code and use that key to encypt the file later on.

3. If user have a file to encrypt instead of a small message then this option will be the best one as it will cover the full file and store the encrypted file in the output folder.


![alt text](https://github.com/AdarshRazor/NightFury_Decrypto/blob/main/imgs/2.PNG "selection menu")


> **Decryption**


1. In order to decrypt it first you need to locate the _secret.key_ file and then the _data.file_ which you can find in the output folder.

2. It will decrypt and stores the output in _result.txt_ and will delete the _data.file_ and _secret.key_ file from the output.

---
### Possible errors


> tkinter module not found


Install the module by launching the cmd and using command:


```bash
pip install tkinter (Python2)
pip3 install tkinter (Python3)
```