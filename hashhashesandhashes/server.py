"""
Asynchronous server for PPC tasks.
- TIMELIMIT  - general timelimit for tasks completion in seconds
- PROBLEM - problem generator. Generator should return tuple of two variables - challenge and expected output. Both should be strings.
- GREETING - a string to be printed before challenges 
- N_PROBLEMS - amount of PROBLEMs to solve in TIMELIMIT
- FLAG - what to return in case of successful completion of all PROBLEMs in TIMELIMIT
"""

from flag import flag
import asyncio
import time
from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l

ROUNDS = 17
BLEN = 8
CONST = 0x6e65706f6e2e7079
TIMELIMIT = 60
GREETING = "My greeting should be here\n"
ALPHABET = range(97, 123)
IP = "0.0.0.0"
PORT = 6667
HASHCASH = True

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

if any([x is None for x in [TIMELIMIT, IP, PORT, GREETING]]):
    raise Exception("Please fill global vars")

async def handle_requests(reader, writer):
    addr = writer.get_extra_info('peername')
    print("[+] Connection from {}".format(addr))
    if HASHCASH:
        pass

    writer.write(bytes(GREETING, encoding="utf-8"))
    await writer.drain()

    inp = await reader.read(128)
    inp = inp[:-1]
    for i in inp:
        if i not in ALPHABET:
            writer.write(bytes("SHOULD BE IN ALPHABET\nPON?", encoding="utf-8"))
            await writer.drain()
            writer.close()
            return
    if (generate_hash(inp) == 0x712e241608d44a98):
        writer.write(bytes(flag, encoding="utf-8"))
        await writer.drain()
        writer.close()
        return
    writer.write(bytes("no way\nPON?", encoding="utf-8"))
    await writer.drain()
    writer.close()
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_requests, IP, PORT, loop=loop)
server = loop.run_until_complete(coro)

print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
