import re
import sys

input = sys.stdin.readline

n = int(input())
data = input().rstrip()

pattern = re.compile(r"o(go)+")
data = pattern.sub("***", data)

print(data)