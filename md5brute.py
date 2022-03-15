import hashlib

def tryOpen(wordlist):
    global pass_file
    try:    
        pass_file = open(wordlist, "r")
    except:
        print("** No such file at that path **")
        quit()

pass_hash = input("Enter a MD5 hash value:")
wordlist = input("Enter path to the password list: ")
tryOpen(wordlist)

for word in pass_file:
    print("[!] Trying " + word.strip("\n"))
    enc_word = word.encode('utf-8')
    md5digest = hashlib.md5(enc_word.strip()).hexdigest()

    if md5digest == pass_hash:
        print(f"PASSWORD FOUND: {word}")
        exit(0)

print("Password not in the password list :(")
