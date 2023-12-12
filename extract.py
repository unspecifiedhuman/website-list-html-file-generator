with open("web.txt") as f:
	txt=f.read()
lines = txt.count('\n')
for i in range(0,lines):
	n1=txt.find('addr="')
	for i in range(0,9):
		if txt[n1+13+i] == '"':
			if '"' in txt[n1+6:n1+13+i]:
				print(txt[n1+7:n1+13+i])
			else:
				print(txt[n1+6:n1+13+i])
			txt=txt[n1+14+i:]
