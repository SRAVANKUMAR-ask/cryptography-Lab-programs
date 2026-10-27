"""
Keyword-based Monoalphabetic Cipher

Instead of memorizing a random 26-letter permutation, both sender and
receiver only need to remember a keyword. The cipher alphabet is built by:
  1. Writing the keyword's unique letters first (duplicates removed).
  2. Following with the remaining unused letters of the alphabet,
     in normal A-Z order.

Example with keyword "CIPHER":
plain : a b c d e f g h i j k l m n o p q r s t u v w x y z
cipher: C I P H E R A B D F G J K L M N O Q S T U V W X Y Z
"""

import string

ALPHABET = string.ascii_uppercase


def build_cipher_alphabet(keyword):
    """Build the 26-letter cipher alphabet from the keyword."""
    seen = []
    for ch in keyword.upper():
        if ch.isalpha() and ch not in seen:
            seen.append(ch)

    remaining = [ch for ch in ALPHABET if ch not in seen]
    return "".join(seen) + "".join(remaining)


def print_mapping(cipher_alpha):
    print("plain : " + " ".join(ALPHABET.lower()))
    print("cipher: " + " ".join(cipher_alpha))
    print()


def encrypt(plaintext, cipher_alpha):
    result = []
    for c in plaintext:
        if c.isalpha():
            idx = ALPHABET.index(c.upper())
            enc = cipher_alpha[idx]
            result.append(enc if c.isupper() else enc.lower())
        else:
            result.append(c)
    return "".join(result)


def decrypt(ciphertext, cipher_alpha):
    result = []
    for c in ciphertext:
        if c.isalpha():
            idx = cipher_alpha.index(c.upper())
            dec = ALPHABET[idx]
            result.append(dec if c.isupper() else dec.lower())
        else:
            result.append(c)
    return "".join(result)


if __name__ == "__main__":
    keyword = input("Enter keyword: ")
    plaintext = input("Enter plaintext message: ")

    cipher_alpha = build_cipher_alphabet(keyword)

    print(f"\nKeyword: {keyword.upper()}\n")
    print_mapping(cipher_alpha)

    encrypted = encrypt(plaintext, cipher_alpha)
    print(f"Plaintext : {plaintext}")
    print(f"Encrypted : {encrypted}")

    decrypted = decrypt(encrypted, cipher_alpha)
    print(f"Decrypted : {decrypted}")