import sys
import codecs
s = sys.argv
parola = s[1]
binp = []
for litera in parola:
    binp += litera
# print([chr(int(i,2)) for i in binp])
fisier = s[2]
out = s[3]
f = open(fisier, "rb")
text = f.read()
text = text.decode("utf-8")
it = 0
lungime = len(parola)
f = codecs.open(out, "w","utf-8")
for caracter in text:
    it %= lungime
    t = chr(ord(caracter) ^ ord(binp[it]))
    print(t,sep= "", end= "", file= f)
    it += 1
