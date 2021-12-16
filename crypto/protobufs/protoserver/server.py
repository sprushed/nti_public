import asyncio
from Crypto.Util.number import long_to_bytes as l2b
from Crypto.Util.number import bytes_to_long as b2l
from blackboxprotobuf.lib.api import decode_message
import gzip

def xor(data, key):
    if isinstance(data, str):
        data = data.encode()
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

def decode_flag(data):
    data = gzip.decompress(data)
    message, typedef = decode_message(data)
    key = l2b(message["4"])
    message["1"] = xor(message["1"], key)
    print(message)

async def handle_request(reader, writer):
    addr = writer.get_extra_info('peername')
    print("[+] Connection from {}".format(addr))
    
    writer.write(bytes("Extra efficient checksystem! Just send your flags in our extremely efficient google-backed compressed format!\n", encoding="utf-8"))
    await writer.drain()
    
    data = await reader.read(10000)
    decode_flag(data)

    writer.close()

IP = "0.0.0.0"
PORT = 9999

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_request, IP, PORT, loop=loop)
server = loop.run_until_complete(coro)

print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

