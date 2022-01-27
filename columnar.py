up_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Columnar:
    def col_encrypt(plaintext, key):
        plaintext = plaintext.replace(" ", "")
        cipher = ""
        num_key = []
        key_index = []
        table = []
        row = []
        for i in key.upper():
            num_key.append(up_alpha.index(i))

        for i in num_key:
            sorted_key = num_key.copy()
            sorted_key.sort()
            key_index.append(sorted_key.index(i) + 1)

        while len(plaintext) % len(key_index) != 0:
            plaintext = plaintext + 'X'

        i = 1
        for char in plaintext:
            row.append(char)
            if i % len(key_index) == 0:
                table.append(row.copy())
                row.clear()
            i = i + 1

        for i in range(len(key_index)):
            for row in table:
                cipher = cipher + row[key_index.index(i + 1)]

        return cipher

    def col_decrypt(cipher, key):
        cipher = cipher.replace(" ", "")
        plaintext = ""
        num_key = []
        key_index = []
        table = []
        col = []
        for i in key.upper():
            num_key.append(up_alpha.index(i))

        for i in num_key:
            sorted_key = num_key.copy()
            sorted_key.sort()
            key_index.append(sorted_key.index(i) + 1)

        while len(plaintext) % len(key_index) != 0:
            cipher = cipher + 'X'

        i = 1
        for char in cipher:
            col.append(char)
            if i % (len(key_index) // len(key_index)) == 0:
                table.append(col.copy())
                col.clear()
            i = i + 1

        for i in range(len(key_index)):
            for col in table:
                cipher = cipher + col[key_index[i]]

        return plaintext
