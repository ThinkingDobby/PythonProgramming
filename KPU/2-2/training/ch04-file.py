import sys

(i, o) = (sys.argv[1:3])

f = open("%s" %i, 'r', encoding="UTF-8")
s = open("%s" %o, 'w', encoding="UTF-8")
while True:
    line = f.readline()
    if not line: break
    l = map(int, line.split())
    s.write("%s = %d\n" %(line.strip(), sum(l)))

f.close()
s.close()