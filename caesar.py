class Caesar:
    low_alpha = "abcdefghijklmnopqrstuvwxyz"
    up_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def c_encrypt(plaintext, key, low_alpha, up_alpha):
        cipher = ""
        for i in range(len(plaintext)):
            char = plaintext[i]
            if char in low_alpha:
                char = low_alpha[(low_alpha.index(char) + key) % 26]
            elif char in up_alpha:
                char = up_alpha[(up_alpha.index(char) + key) % 26]
            cipher = cipher + char
        return cipher

    def c_decrypt(cipher, key, low_alpha, up_alpha):
        plaintext = ""
        for i in range(len(cipher)):
            char = cipher[i]
            if char in low_alpha:
                char = low_alpha[(low_alpha.index(char) - key + 26) % 26]
            elif char in up_alpha:
                char = up_alpha[(up_alpha.index(char) - key + 26) % 26]
            plaintext = plaintext + char
        return plaintext
