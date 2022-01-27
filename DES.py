import pycrypto
from crypto.Cipher import DES
from Crypto import Random

des1 = DES.new('01234567', DES.MODE_ECB)
des2 = DES.new('01234567', DES.MODE_ECB)
text = 'abcdefghijklmnop'
cipher_text = des1.encrypt(text)
print(cipher_text)
des2.decrypt(cipher_text)
print(cipher_text)
