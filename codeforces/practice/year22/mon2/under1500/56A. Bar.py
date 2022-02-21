n = int(input())

drinks = ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]

cnt = 0
for i in range(n):
    data = input()
    if data.isdigit():
        if int(data) < 18:
            cnt += 1
    elif data in drinks:
        cnt += 1

print(cnt)