import sys

if sys.argv[1] == "-a":
    with open("memo.txt", "a", encoding="UTF-8") as f:
        s = sys.argv[2]
        f.write(s + "\n")
else:
    with open("memo.txt", "r", encoding="UTF-8") as f:
        r = f.read()
        print(r)