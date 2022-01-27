class Playfair:

    def __init__(self):
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    def create_table(key):
        keytext = []
        row = []
        table = []
        for char in key.upper():
            if char not in keytext and char in self.alphabet:
                keytext.append(char)

        for char in alphabet:
            if char not in keytext:
                keytext.append(char)

        i = 1
        for char in keytext:
            row.append(char)
            if i % 5 == 0:
                table.append(row.copy())
                row.clear()
            i = i + 1
        return table

    def create_bitext(plaintext):
        plaintext = plaintext.upper().replace("J", "I")
        text = []
        bitext = []
        rep_char = ""
        for char in plaintext:
            if char in alphabet:
                text.append(char)

        for i in range(len(text)):
            if i % 2 == 0:
                rep_char = text[i]
                continue
            elif rep_char == text[i]:
                text.insert(i, 'X')

        if len(text) % 2 == 1:
            text.append('X')

        i = 0
        for j in range(int(len(text) / 2)):
            bitext.append(list(text[i] + text[i + 1]))
            i = i + 2

        return bitext

    def pf_encrypt(plaintext, key):
        cipher = ""
        bitext = create_bitext(plaintext)
        table = create_table(key)

        for bichar in bitext:
            colx = -1
            coly = -1
            rowx = -1
            rowy = -1
            for i in range(len(table)):
                if bichar[0] in table[i]:
                    colx = table[i].index(bichar[0])
                    rowx = i
                if bichar[1] in table[i]:
                    coly = table[i].index(bichar[1])
                    rowy = i

                if rowx != -1 and rowy != -1 and rowx == rowy:
                    if colx == 4:
                        colx = -1
                    if coly == 4:
                        coly = -1
                    cipher = cipher + table[rowx][colx + 1] + table[rowx][coly + 1]
                    break
                elif colx != -1 and coly != -1 and colx == coly:
                    if rowx == 4:
                        rowx = -1
                    if rowy == 4:
                        rowy = -1
                    cipher = cipher + table[rowx + 1][colx] + table[rowy + 1][coly]
                    break
                elif rowx != -1 and rowy != -1 and colx != -1 and coly != -1:
                    cipher = cipher + table[rowx][coly] + table[rowy][colx]
                    break
        return cipher

    def pf_decrypt(cipher, key):
        plaintext = ""
        bitext = create_bitext(cipher)
        table = create_table(key)

        for bichar in bitext:
            colx = -1
            coly = -1
            rowx = -1
            rowy = -1
            for i in range(len(table)):
                if bichar[0] in table[i]:
                    colx = table[i].index(bichar[0])
                    rowx = i
                if bichar[1] in table[i]:
                    coly = table[i].index(bichar[1])
                    rowy = i

                if rowx != -1 and rowy != -1 and rowx == rowy:
                    if colx == 0:
                        colx = 5
                    if coly == 0:
                        coly = 5
                    plaintext = plaintext + table[rowx][colx - 1] + table[rowx][coly - 1]
                    break
                elif colx != -1 and coly != -1 and colx == coly:
                    if rowx == 0:
                        rowx = 5
                    if rowy == 0:
                        rowy = 5
                    plaintext = plaintext + table[rowx - 1][colx] + table[rowy - 1][colx]
                    break
                elif rowx != -1 and rowy != -1 and colx != -1 and coly != -1:
                    plaintext = plaintext + table[rowx][coly] + table[rowy][colx]
                    break
        return plaintext
