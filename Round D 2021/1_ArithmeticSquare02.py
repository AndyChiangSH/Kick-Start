# 1
T = int(input())

for i in range(T):
    row1 = input().split(" ")
    row2 = input().split(" ")
    row3 = input().split(" ")
    array = [[0] * 3 for j in range(3)]
    for j in range(3):
        array[0][j] = int(row1[j])
        array[2][j] = int(row3[j])
    array[1][0] = int(row2[0])
    array[1][2] = int(row2[1])

    avgs = dict()
    sm = array[0][0] + array[2][2]
    if sm % 2 == 0:
        avg = int(sm/2)
        if avg in avgs.keys():
            avgs[avg] += 1
        else:
            avgs[avg] = 1

    sm = array[0][1] + array[2][1]
    if sm % 2 == 0:
        avg = int(sm/2)
        if avg in avgs.keys():
            avgs[avg] += 1
        else:
            avgs[avg] = 1

    sm = array[0][2] + array[2][0]
    if sm % 2 == 0:
        avg = int(sm/2)
        if avg in avgs.keys():
            avgs[avg] += 1
        else:
            avgs[avg] = 1

    sm = array[1][0] + array[1][2]
    if sm % 2 == 0:
        avg = int(sm/2)
        if avg in avgs.keys():
            avgs[avg] += 1
        else:
            avgs[avg] = 1

    Max = 0
    for avg in avgs.values():
        if avg > Max:
            Max = avg

    if array[0][2] - array[0][1] == array[0][1] - array[0][0]:
        Max += 1
    if array[2][2] - array[2][1] == array[2][1] - array[2][0]:
        Max += 1
    if array[2][0] - array[1][0] == array[1][0] - array[0][0]:
        Max += 1
    if array[2][2] - array[1][2] == array[1][2] - array[0][2]:
        Max += 1

    print(f"Case #{i+1}: {Max}")
