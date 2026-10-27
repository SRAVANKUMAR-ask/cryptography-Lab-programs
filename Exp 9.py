"""
Playfair Cipher Decryption
(Historical example: PT-109 rescue message, keyword "ROYAL NEW ZEALAND NAVY")

Playfair uses a 5x5 key square (I and J share a cell).
Decryption rules for a digraph (pair of letters):
  - Same row    -> shift each letter one position LEFT (wrap around)
  - Same column -> shift each letter one position UP (wrap around)
  - Otherwise (rectangle) -> swap columns, keep same rows
"""

SIZE = 5


def build_square(keyword):
    """Build the 5x5 key square from a keyword."""
    keyword = keyword.upper().replace("J", "I")
    seen = []
    for c in keyword:
        if c.isalpha() and c not in seen:
            seen.append(c)

    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # note: no J (merged into I)
        if c not in seen:
            seen.append(c)

    square = [seen[i * SIZE:i * SIZE + SIZE] for i in range(SIZE)]
    return square


def print_square(square):
    print("Playfair Key Square:")
    for row in square:
        print(" ".join(row))
    print()


def find_pos(square, letter):
    for r in range(SIZE):
        for c in range(SIZE):
            if square[r][c] == letter:
                return r, c
    return None


def decrypt_pair(square, a, b):
    ra, ca = find_pos(square, a)
    rb, cb = find_pos(square, b)

    if ra == rb:
        # same row -> shift left
        return square[ra][(ca - 1) % SIZE], square[rb][(cb - 1) % SIZE]
    elif ca == cb:
        # same column -> shift up
        return square[(ra - 1) % SIZE][ca], square[(rb - 1) % SIZE][cb]
    else:
        # rectangle -> swap columns
        return square[ra][cb], square[rb][ca]


def decrypt_message(ciphertext, keyword):
    square = build_square(keyword)
    clean = "".join(c for c in ciphertext.upper() if c.isalpha()).replace("J", "I")

    result = []
    for i in range(0, len(clean), 2):
        a, b = clean[i], clean[i + 1]
        da, db = decrypt_pair(square, a, b)
        result.append(da)
        result.append(db)

    return square, "".join(result)


if __name__ == "__main__":
    keyword = "ROYAL NEW ZEALAND NAVY"
    ciphertext = (
        "KXJEY UREBE ZWEHE WRYTU HEYFS "
        "KREHE GOYFI WTTTU OLKSY CAJPO "
        "BOTEI ZONTX BYBNT GONEY CUZWR "
        "GDSON SXBOU YWRHE BAAHY USEDQ"
    )

    square, decrypted = decrypt_message(ciphertext, keyword)

    print_square(square)
    print(f"Keyword    : {keyword}")
    print(f"Ciphertext : {ciphertext}\n")
    print(f"Decrypted (raw) : {decrypted}")