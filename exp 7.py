from collections import Counter

ciphertext = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83*

*(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*

;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

# Count frequency of each symbol
frequency = Counter(ciphertext)

print("Character Frequency Analysis")
print("----------------------------")

for symbol, count in frequency.most_common():
    if symbol not in [' ', '\n', '\t']:
        print(repr(symbol), ":", count)

print("\nCiphertext:")
print(ciphertext)
from collections import Counter

ciphertext = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83*
*(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

frequency = Counter(
    char for char in ciphertext
    if char not in [' ', '\n', '\t']
)

print("Symbol    Frequency")
print("------------------")

for symbol, count in frequency.most_common():
    print(f"{symbol!r:8} {count}")