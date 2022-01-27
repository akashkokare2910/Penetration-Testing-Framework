import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, askdirectory, asksaveasfilename
from tkinter.ttk import Combobox

low_alpha = "abcdefghijklmnopqrstuvwxyz"
up_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
plain_text_array = []
enc_text_array = []
dec_text_array = []
file_names = []


class Caesar:

    def c_encrypt(self, plaintext, key):
        cipher = ""
        for i in range(len(plaintext)):
            char = plaintext[i]
            if char in low_alpha:
                char = low_alpha[(low_alpha.index(char) + key) % 26]
            elif char in up_alpha:
                char = up_alpha[(up_alpha.index(char) + key) % 26]
            cipher = cipher + char
        return cipher

    def c_decrypt(self, cipher, key):
        plaintext = ""
        for i in range(len(cipher)):
            char = cipher[i]
            if char in low_alpha:
                char = low_alpha[(low_alpha.index(char) - key + 26) % 26]
            elif char in up_alpha:
                char = up_alpha[(up_alpha.index(char) - key + 26) % 26]
            plaintext = plaintext + char
        return plaintext


class Vigenere:

    def v_encrypt(self, plaintext, key):
        cipher = ""
        j = 0
        for i in range(len(plaintext)):
            char = plaintext[i]
            if j == len(key):
                j = 0
            if char in low_alpha:
                char = low_alpha[(low_alpha.index(char) + low_alpha.index(key[j].lower())) % 26]
                j = j + 1
            elif char in up_alpha:
                char = up_alpha[(up_alpha.index(char) + up_alpha.index(key[j].upper())) % 26]
                j = j + 1
            cipher = cipher + char
        return cipher

    def v_decrypt(self, cipher, key):
        plaintext = ""
        j = 0
        for i in range(len(cipher)):
            char = cipher[i]
            if j == len(key):
                j = 0
            if char in low_alpha:
                char = low_alpha[(low_alpha.index(char) - low_alpha.index(key[j].lower())) % 26]
                j = j + 1
            elif char in up_alpha:
                char = up_alpha[(up_alpha.index(char) - up_alpha.index(key[j].upper())) % 26]
                j = j + 1
            plaintext = plaintext + char
        return plaintext


class Columnar:
    def col_encrypt(self, plaintext, key):
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

    def col_decrypt(self, cipher, key):
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

        for col in table:
            for j in key_index:
                cipher += col[j]

        return plaintext


class Playfair:

    def create_table(self, key):
        keytext = []
        row = []
        table = []
        for char in key.upper():
            if char not in keytext and char in alphabet:
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

    def create_bitext(self, plaintext):
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

    def pf_encrypt(self, plaintext, key):
        cipher = ""
        bitext = self.create_bitext(plaintext)
        table = self.create_table(key)

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

    def pf_decrypt(self, cipher, key):
        plaintext = ""
        bitext = self.create_bitext(cipher)
        table = self.create_table(key)

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


def cb_change(event):
    key_entry.delete(0, 'end')


def type_change(event):
    if combobox2.get() == "Text":
        encrypt_button.grid(row=4, column=0, padx=10, pady=10, columnspan=3, sticky="w")
        decrypt_button.grid(row=4, column=2, padx=0, pady=10, columnspan=3, sticky="w")
        open_eButton.grid_forget()
        save_eButton.grid_forget()
        open_dButton.grid_forget()
        save_dButton.grid_forget()
        enc_text_array.clear()
        dec_text_array.clear()
        file_names.clear()
        plain_text_array.clear()
        before_entry.configure(state='normal')

    elif combobox2.get() == "File":
        encrypt_button.grid_forget()
        decrypt_button.grid_forget()
        open_eButton.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky="w")
        save_eButton.grid(row=4, column=1, padx=45, pady=10, columnspan=2, sticky="w")
        open_dButton.grid(row=4, column=2, padx=0, pady=10, columnspan=2, sticky="w")
        save_dButton.grid(row=4, column=3, padx=65, pady=10, sticky="w")
        open_eButton["text"] = "Encrypt File"
        open_dButton["text"] = "Decrypt File"
        enc_text_array.clear()
        dec_text_array.clear()
        file_names.clear()
        plain_text_array.clear()
        before_entry.configure(state='readonly')

    elif combobox2.get() == "Folder":
        encrypt_button.grid_forget()
        decrypt_button.grid_forget()
        open_eButton.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky="w")
        save_eButton.grid(row=4, column=1, padx=55, pady=10, columnspan=2, sticky="w")
        open_dButton.grid(row=4, column=2, padx=0, pady=10, columnspan=2, sticky="w")
        save_dButton.grid(row=4, column=3, padx=55, pady=10, sticky="w")
        open_eButton["text"] = "Encrypt Folder"
        open_dButton["text"] = "Decrypt Folder"
        enc_text_array.clear()
        dec_text_array.clear()
        file_names.clear()
        plain_text_array.clear()
        before_entry.configure(state='readonly')


cs = Caesar()
vg = Vigenere()
cl = Columnar()
pf = Playfair()
window = Tk()

window.title('Cipher Calc')
window.geometry("320x158")

Label(window, text='Type').grid(row=0, column=0, padx=7, pady=5, sticky="w")
combobox1 = Combobox(window,
                     values=(
                         'Caesar', 'Vigenere', 'Columnar', 'Playfair'
                     ), state='readonly', width=10)
combobox1.grid(row=0, column=1, sticky="w", pady=5)
combobox1.set("Caesar")
combobox1.bind('<<ComboboxSelected>>', cb_change)

combobox2 = Combobox(window,
                     values=(
                         'Text', 'File', 'Folder'
                     ), state='readonly', width=10)
combobox2.grid(row=0, column=2, sticky="w", pady=5, padx=10, columnspan=2)
combobox2.set("Text")
combobox2.bind('<<ComboboxSelected>>', type_change)

Label(window, text='Key').grid(row=1, column=0, padx=7, pady=5, sticky="w")
key_text = StringVar()
key_entry = Entry(window, textvariable=key_text, width=13)
key_entry.grid(row=1, column=1, sticky="w")

first_label = Label(window, text='Plaintext')
first_label.grid(row=2, column=0, padx=7, pady=5, columnspan=2, sticky="w")
before_text = StringVar()
before_entry = Entry(window, textvariable=before_text, width=24)
before_entry.grid(row=3, column=0, columnspan=2, padx=10, sticky="w")

second_label = Label(window, text='Ciphertext')
second_label.grid(row=2, column=2, padx=0, pady=5, columnspan=2, sticky="w")
after_text = StringVar()
after_entry = Entry(window, textvariable=after_text, state='readonly', width=23)
after_entry.grid(row=3, column=2, columnspan=2, sticky="w")


def open_file():
    file = askopenfile(parent=window, mode='r', filetypes=[('Text Files', '.txt .py .doc .docx')])
    if file:
        content = file.read()
        file.close()
        print(content)
        messagebox.showinfo('Success', 'File correctly read. Please press "Save as" button and write new name of file')
        return content


def open_dir():
    enc_text_array.clear()
    dec_text_array.clear()
    file_names.clear()
    plain_text_array.clear()
    directory = askdirectory()
    directory = os.path.normpath(directory)
    files = []
    i = 0
    for r, d, f in os.walk(directory):
        for file in f:
            if file.lower().endswith(('.txt', '.py', '.doc')):
                file_names.append(os.path.basename(file))
                files.append(os.path.join(r, file))
                f = open(os.path.join(r, file), "r")
                data = f.read()
                plain_text_array.append(data)
                f.close()
                i += 1

    messagebox.showinfo('Success', str(i) + ' files successfully read')
    return plain_text_array


def save_enc():
    if combobox2.get() == "File":
        if enc_text_array:
            filename = asksaveasfilename(defaultextension=".py",
                                         filetypes=[("Text files", ".txt"), ("Python files", ".py"),
                                                    ("Word files", ".docx"), ("Old Word files", ".doc")])
            with open(filename, "w") as file:
                file.write(enc_text_array[0])
            messagebox.showinfo('Success', 'File successfully encrypted')
        else:
            messagebox.showerror('Empty File', 'Please choose 1 file!')
    elif combobox2.get() == "Folder":
        if enc_text_array:
            directory = askdirectory()
            if directory:
                i = 0
                for filename in file_names:
                    if i >= len(file_names):
                        break
                    filepath = os.path.normpath(os.path.join(directory, filename))
                    print(filename)
                    with open(filepath, "w") as file:
                        file.write(enc_text_array[i])
                    i += 1
                messagebox.showinfo('Success', 'Folder successfully encrypted')

        else:
            messagebox.showerror('Empty File', 'Please select a non-empty folder!')


def save_dec():
    if combobox2.get() == "File":
        if dec_text_array:
            filename = asksaveasfilename(defaultextension=".py",
                                         filetypes=[("Text files", ".txt"), ("Python files", ".py"),
                                                    ("Word files", ".docx"), ("Old Word files", ".doc")])
            with open(filename, "w") as file:
                file.write(dec_text_array[0])
            messagebox.showinfo('Success', 'File successfully decrypted')
        else:
            messagebox.showerror('Empty File', 'Please choose 1 file!')
    elif combobox2.get() == "Folder":
        if dec_text_array:
            directory = askdirectory()
            if directory:
                i = 0
                for filename in file_names:
                    if i >= len(file_names):
                        break
                    filepath = os.path.normpath(os.path.join(directory, filename))
                    print(filename)
                    with open(filepath, "w") as file:
                        file.write(dec_text_array[i])
                    i += 1
                messagebox.showinfo('Success', 'Folder successfully decrypted')

        else:
            messagebox.showerror('Empty File', 'Please select a non-empty folder!')


def onclick_encrypt():
    after_entry.configure(state='normal')
    first_label.config(text='Plaintext')
    second_label.config(text='Ciphertext')
    if combobox1.get() == "Caesar":
        if key_text.get().isdigit():
            if combobox2.get() == "Text":
                after_text.set(cs.c_encrypt(before_text.get(), int(key_text.get())))
            elif combobox2.get() == "File":
                text = open_file()
                if text:
                    enc_text_array.append(cs.c_encrypt(text, int(key_text.get())))
            elif combobox2.get() == "Folder":
                for data in open_dir():
                    enc_text_array.append(cs.c_encrypt(data, int(key_text.get())))
        else:
            messagebox.showerror('ValueError', 'Key must be a digit!')

    elif combobox1.get() == "Vigenere":
        if key_text.get().isalpha():
            if combobox2.get() == "Text":
                after_text.set(vg.v_encrypt(before_text.get(), key_text.get()))
            elif combobox2.get() == "File":
                text = open_file()
                if text:
                    enc_text_array.append(vg.v_encrypt(text, key_text.get()))
            elif combobox2.get() == "Folder":
                for data in open_dir():
                    enc_text_array.append(vg.v_encrypt(data, key_text.get()))
        else:
            messagebox.showerror('ValueError', 'The key must consist only letters!')
    elif combobox1.get() == "Columnar":
        key = key_text.get().replace(" ", "")
        if key.isalpha():
            if combobox2.get() == "Text":
                after_text.set(cl.col_encrypt(before_text.get(), key))
            elif combobox2.get() == "File":
                text = open_file()
                if text:
                    enc_text_array.append(cl.col_encrypt(text, key))
            elif combobox2.get() == "Folder":
                for data in open_dir():
                    enc_text_array.append(cl.col_encrypt(data, key))

        else:
            messagebox.showerror('ValueError', 'The key must consist only letters!')
    elif combobox1.get() == "Playfair":
        key = key_text.get().replace(" ", "")
        if key.isalpha():

            if combobox2.get() == "Text":
                after_text.set(pf.pf_encrypt(before_text.get(), key))
            elif combobox2.get() == "File":
                text = open_file()
                if text:
                    enc_text_array.append(pf.pf_encrypt(text, key))
            elif combobox2.get() == "Folder":
                for data in open_dir():
                    enc_text_array.append(pf.pf_encrypt(data, key))
        else:
            messagebox.showerror('ValueError', 'The key must consist only letters!')

    after_entry.configure(state='readonly')


def onclick_decrypt():
    after_entry.configure(state='normal')
    first_label.config(text='Ciphertext')
    second_label.config(text='Plaintext')
    if combobox1.get() == "Caesar":
        if key_text.get().isdigit():
            if key_text.get().isdigit():
                if combobox2.get() == "Text":
                    after_text.set(cs.c_decrypt(before_text.get(), int(key_text.get())))
                elif combobox2.get() == "File":
                    text = open_file()
                    if text:
                        dec_text_array.append(cs.c_decrypt(text, int(key_text.get())))
                elif combobox2.get() == "Folder":
                    for data in open_dir():
                        dec_text_array.append(cs.c_decrypt(data, int(key_text.get())))
            else:
                messagebox.showerror('ValueError', 'Key must be a digit!')

        else:
            messagebox.showerror('ValueError', 'Key must be a digit!')
    elif combobox1.get() == "Vigenere":
        if key_text.get().isalpha():
            if combobox2.get() == "Text":
                after_text.set(vg.v_decrypt(before_text.get(), key_text.get()))
            elif combobox2.get() == "File":
                text = open_file()
                if text:
                    dec_text_array.append(vg.v_decrypt(text, key_text.get()))
            elif combobox2.get() == "Folder":
                for data in open_dir():
                    dec_text_array.append(vg.v_decrypt(data, key_text.get()))

        else:
            messagebox.showerror('ValueError', 'The key must consist only letters!')
    elif combobox1.get() == "Columnar":
        key = key_text.get().replace(" ", "")
        if key.isalpha():
            if combobox2.get() == "Text":
                after_text.set(cl.col_decrypt(before_text.get(), key))
            elif combobox2.get() == "File":
                text = open_file()
                if text:
                    dec_text_array.append(cl.col_decrypt(text, key))
            elif combobox2.get() == "Folder":
                for data in open_dir():
                    dec_text_array.append(cl.col_decrypt(data, key))
        else:
            messagebox.showerror('ValueError', 'The key must consist only letters!')
    elif combobox1.get() == "Playfair":
        key = key_text.get().replace(" ", "")
        if key.isalpha():
            if combobox2.get() == "Text":
                after_text.set(pf.pf_decrypt(before_text.get(), key))
            elif combobox2.get() == "File":
                text = open_file()
                if text:
                    dec_text_array.append(pf.pf_decrypt(text, key))
            elif combobox2.get() == "Folder":
                for data in open_dir():
                    dec_text_array.append(pf.pf_decrypt(data, key))
        else:
            messagebox.showerror('ValueError', 'The key must consist only letters!')

    after_entry.configure(state='readonly')


encrypt_button = Button(window, text='Encrypt', command=onclick_encrypt)
encrypt_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky="w")

decrypt_button = Button(window, text='Decrypt', command=onclick_decrypt)
decrypt_button.grid(row=4, column=2, padx=0, pady=10, columnspan=2, sticky="w")

open_eButton = Button(window, text='Encrypt file', command=onclick_encrypt)
save_eButton = Button(window, text='Save as', command=save_enc)
open_dButton = Button(window, text='Decrypt file', command=onclick_decrypt)
save_dButton = Button(window, text='Save as', command=save_dec)

window.mainloop()
