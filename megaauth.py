from mega import Mega # importing 
import glob, os
from fsplit.filesplit import Filesplit


fs = Filesplit()

inp1=int(input("Enter the split size (5 = 500KB, 50 = 5MB, 500 = 50MB [default 5]) : "))

fs.split(file="./output/data.file", split_size=inp1*100000, output_dir="./output/divided")
os.remove("./output/data.file")

print("Files are divided, Please check output/divided folder")

mega = Mega() # creating instance of mega
print("\nPlease wait, logging in .....")
m = mega.login("Email", "Password") #email id and passwor of www.mega.nz
print("login done !! ")

filename=[]
os.chdir("./output/divided")

for file in glob.glob("*.file"):
    filename.append(file)

print("No. of division created:",len(filename))

print("Uploading file in progress ....")
for i in range(len(filename)):
    file_upload=filename[i]
    file = m.upload(file_upload)
    link=m.get_upload_link(file)
    print("\nLink of file :",link)
    os.remove(filename[i])

'''for i in range(len(filename)):
    os.remove(filename[i])'''

file = m.upload("fs_manifest.csv")
link=m.get_upload_link(file)
print("Link of manifest :",link)
print("\n\n")

os.remove("fs_manifest.csv")