Делаем обратный алгоритм для

```python
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
```

```python
def revhash(k):
    maxed = 0x100 ** BLEN
    REV_CONST = pow(CONST, -1, maxed)
    for nround in range(ROUNDS):
        k *= REV_CONST
        k %= maxed
        ror(k, 13)
```

Далле подгоняем по XOR
