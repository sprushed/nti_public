import gzip
import os
import random
from string import ascii_letters, digits
import sys
import socket

import lorem
from Crypto.Util.number import bytes_to_long as b2l

import flagshare_pb2

alphabet = ascii_letters + digits

def xor(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])


def gen_flag():
    return ("SPR{" + "".join(random.choices(alphabet, k=random.randrange(10,30))) + "}").encode()


def gen_description():
    return lorem.sentence()


def gen_value():
    return random.randrange(0, 501)


def form_protobuf(flag, description, value=None):
    secured_flag = flagshare_pb2.SecuredFlag()
    key = os.urandom(2)
    secured_flag.encrypted_flag = xor(flag, key)
    secured_flag.xor_key = b2l(key)
    secured_flag.description = description.encode()
    if value is not None:
        secured_flag.value = value

    serialized = secured_flag.SerializeToString()
    return gzip.compress(serialized)


manual_flags = [
    {
        "flag": b"flag{cool_protobufed_service_very_efficient}",
        "description": "Actually, the flag for this challenge. Go ahead, submit it",
    },
    {
        "flag": b"ABOBABOBABOBABOBABOBABOBABOBABO=",
        "description": "My first attack-defense flag",
        "value": 1337,
    },
    {
        "flag": b"CC{s0_symm3tr1c_diffid_https://i.imgur.com/JB5Z0HU.png}",
        "description": "Flag from student's CC2020",
        "value": 6969,
    },
]

def send_data(gzipped_protobuf):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.01", 9999))
    s.sendall(gzipped_protobuf)

if __name__ == "__main__":
    for i in range(4):
        proto = form_protobuf(gen_flag(), gen_description(), gen_value())
        send_data(proto)
    
    send_data(form_protobuf(**manual_flags[2]))

    for i in range(3):
        proto = form_protobuf(gen_flag(), gen_description(), gen_value())
        send_data(proto)

    send_data(form_protobuf(**manual_flags[0]))
    
    for i in range(5):
        proto = form_protobuf(gen_flag(), gen_description(), gen_value())
        send_data(proto)

    send_data(form_protobuf(**manual_flags[1]))
