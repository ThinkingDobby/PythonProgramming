array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array) - 1):
    mv = array[i]
    idx = i
    for j in range(i + 1, len(array)):
        if mv > array[j]:
            mv = array[j]
            idx = j
    array[i], array[idx] = array[idx], array[i]

print(array)