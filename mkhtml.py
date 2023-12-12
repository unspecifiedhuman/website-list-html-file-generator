with open("filtered.txt") as f:
	txt=f.readlines()
lines = len(txt)
print('<script>const randomLines = (str, count) => str.split(/\\r?\\n/).reduce((p, _, __, arr) => (p[0] < count) ? [p[0] + 1, p[1].concat(arr.splice(Math.random() * arr.length | 0, 1))] : p, [0, []])[1];</script>')
print('<button onclick="a = String(randomLines(document.body.innerHTML, 1)); a=a.slice(0,-4); console.log(\'http://\'+a); window.open(\'http://\'+a)">Go to a random IP!</button>')
print('<button onclick="for (let i = 0; i < 11; i++) { a = String(randomLines(document.body.innerHTML, 1)); a=a.slice(0,-4); console.log(\'http://\'+a); window.open(\'http://\'+a)}">Go to 10 random IPs!</button>')
print("<br>")
for i in range(0,lines):
    print(txt[i][:-1]+"<br>")
