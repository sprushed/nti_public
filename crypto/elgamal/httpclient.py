import requests
import os
from Crypto.Util.number import long_to_bytes as l2b
from Crypto.Util.number import bytes_to_long as b2l

message = input().encode()
m = b2l(message)

key = requests.get("http://172.17.0.3:8887/get_key").json()

A = key["A"]
g = key["g"]
p = key["p"]

k = int(os.urandom(128).hex(), base=16)
c1 = pow(g, k, p)
c2 = m*pow(A, k, p)

requests.post("http://172.17.0.3:8887/send_flag", json={"c1": c1, "c2": c2})
