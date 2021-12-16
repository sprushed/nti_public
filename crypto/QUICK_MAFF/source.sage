import Crypto.Util.number

flag = "***REDACTED***"

bits = 62
while True:
    n = Crypto.Util.number.getPrime(bits)
    if n % 8 == 5:
        break

f = GF(n)

enc = ''.join(format(ord(x), 'b').zfill(7) for x in flag)
singles = []

for e in range(len(enc)):
    s = int(enc[e])

    a = f(Crypto.Util.number.getPrime(bits-3))
    a = pow(a, 2, n)

    single = f(pow(3, s, n)) * a
    singles.append(single)

print("n:", n)
print("singles:", singles)
