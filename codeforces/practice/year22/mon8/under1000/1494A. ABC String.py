import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a = input().rstrip()

    ac = a.count('A')
    bc = a.count('B')
    cc = a.count('C')


    def check(f):
        dq = collections.deque()

        if f == a[0]:
            for i in a:
                if i == f:
                    dq.append(i)
                else:
                    if len(dq) == 0:
                        return False
                    else:
                        dq.pop()
        else:
            for i in a:
                if i != f:
                    dq.append(i)
                else:
                    if len(dq) == 0:
                        return False
                    else:
                        dq.pop()

        return len(dq) == 0


    if ac == bc + cc:
        print("YES" if check('A') else "NO")
    elif bc == ac + cc:
        print("YES" if check('B') else "NO")
    elif cc == ac + bc:
        print("YES" if check('C') else "NO")
    else:
        print("NO")
