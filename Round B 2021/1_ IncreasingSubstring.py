T = int(input())

for i in range(T):
    N = int(input())
    S = input()
    count = 1
    print("Case #"+str(i+1)+": 1", end='')
    for j in range(N-1):
        if S[j] < S[j+1]:
            count = count + 1
        else:
            count = 1
        print(" "+str(count), end='')

    print("")
