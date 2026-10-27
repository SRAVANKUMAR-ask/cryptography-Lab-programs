# Playfair Cipher Encryption

def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = []

    for ch in key:
        if ch not in used and ch.isalpha():
            used.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            used.append(ch)

    for i in range(0, 25, 5):
        matrix.append(used[i:i+5])

    return matrix


def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(filter(str.isalpha, text))

    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 == len(text):
            b = 'X'
            i += 1
        else:
            b = text[i + 1]

            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2

        result += a + b

    return result


def encrypt(matrix, text):
    cipher = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


key = input("Enter Keyword: ")
plaintext = input("Enter Plaintext: ")

matrix = generate_matrix(key)

print("\nPlayfair Matrix")
for row in matrix:
    print(" ".join(row))

prepared = prepare_text(plaintext)

ciphertext = encrypt(matrix, prepared)

print("\nPrepared Text :", prepared)
print("Encrypted Text:", ciphertext)