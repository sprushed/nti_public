from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l
from flag import flag

ROUNDS = 17
BLEN = 8
CONST = 0x6e65706f6e2e7079
ALPHABET = range(97, 123)

def rol(numeric, shift):
    maxed = 0x100 ** BLEN
    shift1 = BLEN * 8 - shift
    return ((numeric << shift) % maxed) + (numeric >> shift1)

def generate_hash(bbytes):
    maxed = 0x100 ** BLEN
    bword = list(bbytes)
    bword_len = len(bword)
    k = 0x7370727573686564
    if (bword_len > BLEN):
        for i in range(BLEN, bword_len):
            bword[i % BLEN] ^= bword[i]
    k ^= b2l(bytes(bword[:BLEN]))
    for nround in range(ROUNDS):
        k = rol(k, 13)
        k %= maxed
        k *= CONST
        k %= maxed
    return k

def generate_hash_word(word):
    return generate_hash(word.encode('ascii'))

def generate_hash_num(numeric):
    return generate_hash(l2b(numeric))

def main():
    word = input()
    for i in word:
        if ord(i) not in ALPHABET:
            return 0
    if (generate_hash_word(word) == 0x712e241608d44a98):
        print(flag)
        return 1
    return 0

if (__name__ == "__main__"):
    main()
