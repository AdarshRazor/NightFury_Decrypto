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
User can select from the 2 options of encryption and 1 to print out the export the key(encryption key)





---
### Possible errors

> tkinter module not found

Install the module by launching the cmd and using command:

```bash
pip install tkinter (Python2)
pip3 install tkinter (Python3)
```