T = int(input())

for i in range(T):
    N = int(input())
    S = input().split(" ")
    S = [int(s) for s in S]

    diff = []
    for j in range(N-1):
        diff.append(S[j+1] - S[j])

    # print(diff)

    ctu = 1
    maxi = 1
    for j in range(N-2):
        if diff[j] == diff[j+1]:
            ctu += 1
        else:
            if j+2 < N-2:
                x = max(diff[j+1], diff[j+2])
                y = min(diff[j+1], diff[j+2])
                if (x - y) % 2 == 0:
                    if x - ((x - y) / 2) == diff[j]:
                        ctu += 2
                        if j+3 < N-2:
                            for k in range(j+3, N-2):
                                if diff[k] == diff[j]:
                                    ctu += 1
                                else:
                                    maxi = max(maxi, ctu)
                                    ctu = 1
                                    break
                else:
                    maxi = max(maxi, ctu+1)
                    ctu = 1
            else:
                maxi = max(maxi, ctu+1)
                ctu = 1

print("Case #"+str(i+1)+": "+str(maxi))
