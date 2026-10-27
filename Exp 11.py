"""
Playfair Cipher Key Space Analysis

Part (unignoring duplicates): How many possible 5x5 key matrices are there?
  - The Playfair matrix holds 25 distinct letters (I/J merged into one cell).
  - Any arrangement of these 25 letters into the 25 cells is a valid key.
  - Total possible keys = 25! (25 factorial)

Part a (accounting for duplicate encryptions): Some different matrices produce
IDENTICAL encryption/decryption behavior:
  - Cyclically shifting all rows down (5 possible shifts, including no shift)
    does not change how any pair of letters encrypts.
  - Cyclically shifting all columns right (5 possible shifts) likewise has
    no effect on encryption behavior.
  - Transposing the matrix (reflecting along the main diagonal) also
    preserves encryption behavior (swapping "row rule" and "column rule"
    symmetrically swaps roles but yields the same ciphertext for any pair).
  - These three symmetries combine multiplicatively: 5 * 5 * 2 = 50
    equivalent keys per "effectively unique" key.

  Effectively unique keys = 25! / 50
"""

import math


def total_possible_keys():
    """Total raw key matrices: all permutations of 25 letters into a 5x5 grid."""
    return math.factorial(25)


def effectively_unique_keys():
    """Account for row-shift, column-shift, and transpose symmetries."""
    total = total_possible_keys()
    equivalence_factor = 5 * 5 * 2  # 5 row shifts * 5 column shifts * 2 (transpose)
    return total / equivalence_factor


if __name__ == "__main__":
    total = total_possible_keys()
    log2_total = math.log2(total)

    unique = effectively_unique_keys()
    log2_unique = math.log2(unique)

    print("=== Part 1: Total possible Playfair keys (ignoring duplicates) ===")
    print(f"Total keys = 25! = {total:,}")
    print(f"log2(25!) = {log2_total:.2f}")
    print(f"Approximate as a power of 2: 2^{round(log2_total)}\n")

    print("=== Part a: Effectively unique keys (accounting for duplicate encryptions) ===")
    print("Equivalence factor = 5 (row shifts) x 5 (column shifts) x 2 (transpose) = 50")
    print(f"Effectively unique keys = 25! / 50 = {unique:,.0f}")
    print(f"log2(effective unique keys) = {log2_unique:.2f}")
    print(f"Approximate as a power of 2: 2^{round(log2_unique)}")