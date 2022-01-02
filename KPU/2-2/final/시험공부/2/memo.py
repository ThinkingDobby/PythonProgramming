import sys

if sys.argv[1] == '-a':
    with open("memo.txt", 'w', encoding='utf-8') as f:
        f.write(sys.argv[2] + "\n")
elif sys.argv[1] == '-v':
    with open("memo.txt", 'r', encoding='utf-8') as f:
        print(f.read())