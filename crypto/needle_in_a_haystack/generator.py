import random
from solver import entropy

flag = b"""In information theory, the entropy of a random variable is the average level of "information", "surprise", or "uncertainty" inherent in the variable's possible outcomes. The concept of information entropy was introduced by Claude Shannon in his 1948 paper "A Mathematical Theory of Communication", and is sometimes called Shannon entropy. flag{x0r_pr3s3rv3s_sh4nn0n_3ntr0py}"""

print("Flag entropy:", entropy(flag))

flaglen = len(flag)
insert_position = random.randrange(100, 9900)

f = open("hexes", "w")

def xor(b: bytes, k: int) -> bytes:
    return bytes(k ^ c for c in b)


for i in range(10000):
    if i == insert_position:
        xored = xor(flag, random.randrange(256))
        f.write(xored.hex()+"\n")
        continue

    f.write(random.randbytes(flaglen).hex()+"\n")

f.close()
