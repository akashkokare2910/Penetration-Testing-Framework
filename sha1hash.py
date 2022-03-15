from urllib.request import urlopen 
import hashlib


sha1 = input("Enter SHA1 HASH value:")

passlist = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), 'utf-8')

for password in passlist.split('\n'):
    hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    if hashguess == sha1:
        print("[+] The correct password is found:" + str(password))
        exit()
    else:
        print("[*] The password guess: " + str(password) + " doesn't match, trying next")

print("[*] The password is not found! :(")

