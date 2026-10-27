"""
Playfair Cipher Encryption
Using the given 5x5 matrix:
  M F H I K   (I/J share a cell)
  U N O P Q
  Z V W X Y
  E L A R G
  D S T B C

Encryption rules for a digraph (pair of letters):
  - Same row    -> shift each letter one position RIGHT (wrap around)
  - Same column -> shift each letter one position DOWN (wrap around)
  - Otherwise (rectangle) -> swap columns, keep same rows

Preparation rules:
  - Remove non-letters, convert J -> I, uppercase everything
  - Split into digraphs; if both letters in a pair are the same,
    insert 'X' between them
  - If the final letter is alone, pad with 'X'
"""

SIZE = 5

matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C'],
]


def print_matrix():
    print("Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))
    print()


def find_pos(letter):
    for r in range(SIZE):
        for c in range(SIZE):
            if matrix[r][c] == letter:
                return r, c
    return None


def clean_text(text):
    """Uppercase, keep letters only, J -> I."""
    cleaned = "".join(ch for ch in text.upper() if ch.isalpha())
    return cleaned.replace("J", "I")


def build_digraphs(clean):
    """Split into digraphs, inserting X between duplicate letters, padding a trailing single letter."""
    digraphs = []
    i = 0
    n = len(clean)
    while i < n:
        a = clean[i]
        b = clean[i + 1] if i + 1 < n else 'X'

        if a == b:
            digraphs.append(a + 'X')
            i += 1  # only consume 'a'; repeated letter stays for next pair
        else:
            digraphs.append(a + b)
            i += 2

    return digraphs


def encrypt_pair(a, b):
    ra, ca = find_pos(a)
    rb, cb = find_pos(b)

    if ra == rb:
        # same row -> shift right
        return matrix[ra][(ca + 1) % SIZE], matrix[rb][(cb + 1) % SIZE]
    elif ca == cb:
        # same column -> shift down
        return matrix[(ra + 1) % SIZE][ca], matrix[(rb + 1) % SIZE][cb]
    else:
        # rectangle -> swap columns
        return matrix[ra][cb], matrix[rb][ca]


def encrypt_message(message):
    clean = clean_text(message)
    digraphs = build_digraphs(clean)

    cipher = ""
    for pair in digraphs:
        ca, cb = encrypt_pair(pair[0], pair[1])
        cipher += ca + cb

    return clean, digraphs, cipher


if __name__ == "__main__":
    message = "Must see you over Cadogan West. Coming at once."

    print_matrix()

    clean, digraphs, cipher = encrypt_message(message)

    print(f"Cleaned plaintext : {clean}\n")
    print(f"Digraphs: {' '.join(digraphs)}\n")

    print(f"Original message  : {message}")
    print(f"Ciphertext (raw)  : {cipher}")

    grouped = " ".join(cipher[i:i + 5] for i in range(0, len(cipher), 5))
    print(f"Ciphertext (grouped in 5s): {grouped}")