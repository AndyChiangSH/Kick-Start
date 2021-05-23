T = int(input())

for i in range(T):
    string = input().split(" ")
    N = int(string[0])
    K = int(string[1])
    S = input()

    pld = ""
    for j in range(N):
        pld += "a"

    mid = int((N-1)/2)
    ptr = mid
    count = 0
    while True:
        if pld >= S or len(pld) > N:
            break
        ptr = mid
        count += 1

        # print(pld)  # DEBUG

        newChar = chr(ord(pld[ptr])+1)
        if N % 2 == 0:
            pld = pld[:ptr] + newChar + \
                pld[ptr+1:N-1-ptr] + newChar + pld[N-ptr:]
        else:
            pld = pld[:ptr] + newChar + pld[ptr+1:]

        if ord(pld[ptr])-ord("a") >= K:
            if N % 2 == 0:
                pld = pld[:ptr] + "a" + \
                    pld[ptr+1:N-1-ptr] + "a" + pld[N-ptr:]
            else:
                pld = pld[:ptr] + "a" + pld[ptr+1:]

            while True:
                ptr -= 1
                newChar = chr(ord(pld[ptr])+1)
                pld = pld[:ptr] + newChar + \
                    pld[ptr+1:N-1-ptr] + newChar + pld[N-ptr:]
                if ord(pld[ptr])-ord("a") < K:
                    break
                pld = pld[:ptr] + "a" + pld[ptr+1:N-1-ptr] + "a" + pld[N-ptr:]

    print(f"Case #{i+1}: {count}")
