import struct
enc = b"\x1b]\x16[\nC\x01\x1a^@5q.i!8`\x15\x0fKR'<I\x0f\x15IP%l.5"
enc += struct.pack("I", 3698545)[:3]

#b[0] = 
#b[1] = a[1] ^ b[0]
#a[1] = b[1] ^ b[0]
#Первый символ флага - f, потому что такой формат
dec = bytearray(35)
dec[0] = ord('f')^42 # ^42 потому что memfrob
for i in range(1,35,1):
    dec[i] = enc[i]^enc[i-1]


dec = [c^42 for c in dec]
print(bytearray(dec).decode())


