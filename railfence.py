up_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def col_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    cipher = ""
    row = []
    i = 1
    table = [["" for i in range(len(plaintext))] for j in range(int(key))]

    i = 0
    j = 0
    up = True
    for char in plaintext:
        table[i][j] = char
        j += 1
        if up:
            i += 1
            if i == int(key) - 1:
                up = False
        else:
            i -= 1
            if i == 0:
                up = True

    print(str('\n'.join(table)).strip('[]',))
    # for i in range(len(table)):
    #     for j in range(len(table[i])):
    #         table[i][j] = plaintext[]
    #
    #
    # for i in num_key:
    #     sorted_key = num_key.copy()
    #     sorted_key.sort()
    #     key_index.append(sorted_key.index(i) + 1)
    #
    # while len(plaintext) % len(key_index) != 0:
    #     plaintext = plaintext + 'X'
    #
    #
    # for char in plaintext:
    #     row.append(char)
    #     if i % len(key_index) == 0:
    #         table.append(row.copy())
    #         row.clear()
    #     i = i + 1
    #
    # for i in range(len(key_index)):
    #     for row in table:
    #         cipher = cipher + row[key_index.index(i + 1)]

    return cipher


col_encrypt(input(), input())


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
