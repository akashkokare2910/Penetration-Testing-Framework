import os
import hashlib

hashval = input("Enter the password string:")

hashobj1 = hashlib.md5()
hashobj1.update(hashval.encode())
print(f"Md5 hash value is + {hashobj1.hexdigest()}")
md5 = hashobj1.hexdigest()

hashobj2 = hashlib.sha256()
hashobj2.update(hashval.encode())
print("sha256 hash value is " +hashobj2.hexdigest())
sha256 = hashobj2.hexdigest()

hashobj4 = hashlib.sha1()
hashobj4.update(hashval.encode())
print('Sha1 hash value is ' + hashobj4.hexdigest())
sha = hashobj4.hexdigest()

# hashobj3 = hashlib.sha512()
# hashobj3.update(hashval.encode())
# print(hashobj3.hexdigest())


def switch():
    option = int(input("\n 1--> MD5 \n 2--> SHA \n Enter your option from 1-2 to select the method to crack the password : "))

    if option == 1:
        os.system('python md5brute.py')
        
    
    elif option == 2:
        os.system('python sha1hash.py')
    
    else:
        print("Invalid Option Selected!!")

switch()