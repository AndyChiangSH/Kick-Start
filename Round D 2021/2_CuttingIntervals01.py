# 2
T = int(input())

for t in range(T):
    row = input().split(" ")
    N = int(row[0])
    C = int(row[1])

    dic = dict()

    for n in range(N):
        row = input().split(" ")
        start = int(row[0])
        end = int(row[1])

        # print(f"{start}, {end}")

        for i in range(start+1, end):
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1

    values = sorted(list(dic.values()))
    # print(values)

    count = N
    limit = min(len(values), C)
    for i in range(len(values)-1, len(values)-limit-1, -1):
        count += values[i]
        # print(f"i = {i} , values[i] = {values[i]}")

    print(f"Case #{t+1}: {count}")

"""
1
3 3
1 3
2 4
1 4

1
5 2
0 3
1 5
2 6
3 5
4 5
"""
