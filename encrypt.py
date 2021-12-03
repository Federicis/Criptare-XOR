import sys
import codecs
s = sys.argv
parola = s[1]
binp = []
for litera in parola:
    binp += litera
fisier = s[2]
out = s[3]
f = codecs.open(fisier, "r", "utf-8")
text = f.read()
text_binar = ""
it = 0
lungime = len(parola)
f = open(out, "wb")
for caracter in text:
    it %= lungime
    t = chr(ord(caracter) ^ ord(binp[it]))
    f.write(t.encode("utf-8"))
    it += 1
