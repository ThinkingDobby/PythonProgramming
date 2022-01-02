import sys

src = sys.argv[1]
dest = sys.argv[2]

f = open(src, 'r', encoding="UTF-8")
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " " * 4)

f = open(dest, 'w', "UTF-8")
f.write(space_content)
f.close()