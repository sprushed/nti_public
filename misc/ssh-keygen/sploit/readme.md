### nobody -> user
curl has CAP\_DAC\_READ\_SEARCH capability, which allows nobody to read /home/user/mypassword

### user -> root
`ssh-keygen` has SUID bit set, which in general case would allow us to overwrite `authorized\_keys`, but image is read-only and there's not ssh client running on image. solution is to load shared library `ssh-keygen -D lib.so` to pop a shell.
