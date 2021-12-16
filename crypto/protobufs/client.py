import flagshare_pb2
import os
from Crypto.Util.number import bytes_to_long as b2l
import gzip
import blackboxprotobuf

flag = b"CS{temporary_flag_idunno}"
xorkey = os.urandom(2)


def xor(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])


secured_flag = flagshare_pb2.SecuredFlag()
secured_flag.encrypted_flag = xor(flag, xorkey)
print(xor(flag, xorkey))
secured_flag.xor_key = b2l(xorkey)
secured_flag.description = b"Actually, the flag for this challenge. Value is unknown"

print(secured_flag.SerializeToString())

f = open("dump", "wb")
f.write(gzip.compress(secured_flag.SerializeToString()))
f.close()
