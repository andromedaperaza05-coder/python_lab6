def vigenere_header(alphabet):
    alpha_len = len(alphabet)
    print("|   ", end='')
    for i in range(alpha_len):
        print(f"| {alphabet[i % alpha_len]}", end=' ')
    print('|')
    print(f"{'|---'*(alpha_len + 1)}|")

def vigenere_sq(alphabet):
    alpha_len = len(alphabet)
    vigenere_header(alphabet)
    for shift in range(alpha_len):
        for i in range(alpha_len):
            if i == 0:
                c = alphabet[(i + shift) % alpha_len]
                print(f"| {c}", end=' ')
                print(f"| {c}", end=' ')
            else:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
        print("|")


def letter_to_index(letter, alphabet):
    return alphabet.index(letter)


def index_to_letter(index, alphabet):
    return alphabet[index]


def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)

    ciphertext_index = (key_index + plaintext_index) % len(alphabet)
    return index_to_letter(ciphertext_index, alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    ciphertext = ""

    for i, plaintext_letter in enumerate(plaintext):
        key_letter = key[i % len(key)]
        ciphertext += vigenere_index(key_letter, plaintext_letter, alphabet)

    return ciphertext

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)

    plaintext_index = (cipher_index - key_index) % len(alphabet)
    return index_to_letter(plaintext_index, alphabet)


def decrypt_vignere(key, cipher_text, alphabet):
    plaintext = ""

    for i, cipher_letter in enumerate(cipher_text):
        key_letter = key[i % len(key)]
        plaintext += undo_vigenere_index(key_letter, cipher_letter, alphabet)

    return plaintext

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "DAVINCI"
plaintext = "ATTACKATDAWN"

ciphertext = encrypt_vigenere(key, plaintext, alphabet)
print(ciphertext)
decrypted = decrypt_vignere(key, ciphertext, alphabet)
print(decrypted)

#vigenere_sq(alphabet)


