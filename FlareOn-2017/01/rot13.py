flag 		   = "PyvragFvqrYbtvafNerRnfl@syner-ba.pbz"
flag_decrypted = ""

for c in flag:
	e = 0x0

	if c in ["-", ".", "@"]:
		e = ord(c)
	else:
		d = 90 if c <= "Z" else 122
		e = ord(c)+13
		e = (e-26) if e >= d else e 
		
	
	flag_decrypted += chr(e)

print(flag_decrypted)