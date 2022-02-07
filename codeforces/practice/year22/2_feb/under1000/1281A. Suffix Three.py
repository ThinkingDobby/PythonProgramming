for _ in range(int(input())):
    data = input()

    if data[-2:] == 'po':
        print("FILIPINO")
    elif len(data) >= 4 and (data[-4:] == 'desu' or data[-4:] == 'masu'):
        print("JAPANESE")
    else:
        print("KOREAN")