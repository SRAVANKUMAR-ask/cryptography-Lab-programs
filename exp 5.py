from math import gcd


def mod_inverse(a):
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return None


def encrypt(plaintext, a, b):
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            p = ord(char.upper()) - ord('A')
            c = (a * p + b) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += char

    return ciphertext


def decrypt(ciphertext, a, b):
    plaintext = ""
    a_inverse = mod_inverse(a)

    if a_inverse is None:
        return "Invalid value of a"

    for char in ciphertext:
        if char.isalpha():
            c = ord(char.upper()) - ord('A')
            p = (a_inverse * (c - b)) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += char

    return plaintext


# Main program
plaintext = input("Enter plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if gcd(a, 26) != 1:
    print("Invalid value of a.")
    print("a must be relatively prime to 26.")
else:
    ciphertext = encrypt(plaintext, a, b)

    print("Encrypted text:", ciphertext)

    decrypted = decrypt(ciphertext, a, b)
    print("Decrypted text:", decrypted)