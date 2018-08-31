import string
import os


def print_greeting():
    print("-------------------------------------------")
    print("Howdy!")
    print("-------------------------------------------")

def get_shift():
    shift = input("How much would you like to shift [1-26] ")
    return int(shift)

def shift(n):
    alpha = list(string.ascii_lowercase)

    shift_z = alpha[n:]
    shift_after_z = alpha[0:n]


    for letter in shift_after_z:
        shift_z.append(letter)

    return alpha,shift_z

def create_dict(alphabet, replacement):
    mydict = {}

    for letter, sub in zip(alphabet, replacement):
        mydict[letter] = sub.upper()

    return mydict

def get_text():
    file_path = os.path.abspath("./ToEncrypt.txt")
    with open(file_path, 'r') as myfile:
        text = myfile.read().replace('\n', ' ')
    return text.lower()

def encrypt_text(text, cipher):

    for letter in list(string.ascii_lowercase):
        replacement = cipher[letter]
        text = text.replace(letter, replacement)

    return text.lower()

def write_text(text):
    with open('Encrypted.txt', 'w') as myfile:
        myfile.write(text)


def main():
    print_greeting()
    n = get_shift()
    alphabet, replacement = shift(n)
    my_cipher = create_dict(alphabet, replacement)

    text = get_text()

    encrypted_text = encrypt_text(text, cipher=my_cipher)

    write_text(encrypted_text)



if __name__ == '__main__':
    main()