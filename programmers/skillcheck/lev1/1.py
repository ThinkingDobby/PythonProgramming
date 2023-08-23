def solution(numbers, hand):
    lnow = [3, 0]
    rnow = [3, 2]

    data = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]

    ans = ''
    for n in numbers:
        x = y = -1
        for i in range(4):
            for j in range(3):
                if data[i][j] == str(n):
                    x = i
                    y = j

        if y == 0:
            lnow = [x, y]
            ans += 'L'
        elif y == 2:
            rnow = [x, y]
            ans += 'R'
        else:
            lv = abs(x - lnow[0]) + abs(y - lnow[1])
            rv = abs(x - rnow[0]) + abs(y - rnow[1])
            if lv > rv:
                rnow = [x, y]
                ans += 'R'
            elif lv < rv:
                lnow = [x, y]
                ans += 'L'
            else:
                if hand == 'left':
                    lnow = [x, y]
                    ans += 'L'
                else:
                    rnow = [x, y]
                    ans += 'R'

    return ans



ans = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
print(ans)