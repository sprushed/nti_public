from collections import Counter
from math import log
import random
from typing import List, Tuple
from operator import itemgetter

def entropy(b: bytes) -> float:
    c = Counter(b)
    e = 0.0
    for v in c.values():
        p = v/len(b)
        e += p*log(p, 256)

    return -e

def xor(b: bytes, k: bytes) -> bytes:
    return bytes(b[i] ^ k[i % len(k)] for i in range(len(b)))


if __name__ == "__main__":
    f = open("hexes", "r")
    lines = f.readlines()

    sol: List[Tuple[bytes, float]] = []

    for s in lines:
        b = bytes.fromhex(s.strip())
        
        sol.append((b, entropy(b)))

    sol.sort(key=itemgetter(1))
    print(sol[0])
