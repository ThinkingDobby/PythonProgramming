import sys

s = sys.argv[1]
d = sys.argv[2]

f = open(s, 'r')
t = f.read()
f.close()

f = open(d, 'w')
f.write(t.replace("\t", " "*4))
f.close()