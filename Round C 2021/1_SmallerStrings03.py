T = int(input())

for i in range(T):
    string = input().split(" ")
    N = int(string[0])
    K = int(string[1])
    S = input()

    s = [0]*N
    for index, j in enumerate(S):
        s[index] = ord(j)-ord('a')

    isPlusOne = False
    count = 0
    mid = int((N-1)/2)

    if N == 1 and s[0] > (K-1):
        isPlusOne = True
    if N == 2 and (s[0]+s[1]) > (K-1)*2:
        isPlusOne = True
    for j in range(mid+1):
        count += (min(s[j], K-1))*pow(K, mid-j)
        if s[N-1-j] > s[j]:
            isPlusOne = True

    if isPlusOne:
        count += 1

    print(f"Case #{i+1}: {count}")
