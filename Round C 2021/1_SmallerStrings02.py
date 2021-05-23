def overRange(pld, s, K):
    for i in range(len(pld)):
        if pld[0] >= K:
            return True
        if pld[i] > s[i]:
            return True
        elif pld[i] < s[i]:
            return False
        else:
            pass
    return True


T = int(input())

for i in range(T):
    string = input().split(" ")
    N = int(string[0])
    K = int(string[1])
    S = input()

    s = [0]*N
    for index, j in enumerate(S):
        s[index] = ord(j)-ord('a')
    pld = [0]*N

    mid = int((N-1)/2)
    count = 0
    while True:
        if overRange(pld, s, K):
            break
        ptr = mid
        count += 1

        # print(pld)  # DEBUG

        if N % 2 == 0:
            pld[ptr] += 1
            pld[N-1-ptr] += 1
        else:
            pld[ptr] += 1

        if pld[ptr] >= K and N > 2:
            if N % 2 == 0:
                pld[ptr] = 0
                pld[N-1-ptr] = 0
            else:
                pld[ptr] = 0

            while True:
                if ptr < 1:
                    break
                ptr -= 1
                pld[ptr] += 1
                pld[N-1-ptr] += 1
                if pld[ptr] >= K:
                    if ptr-1 >= 0:
                        pld[ptr] = 0
                        pld[N-1-ptr] = 0
                    continue
                else:
                    break

    print(f"Case #{i+1}: {count}")
