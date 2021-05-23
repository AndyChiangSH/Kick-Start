T = int(input())

for i in range(T):
    G = int(input())

    count = 1
    if G != 1:
        for k in range(1, (int)((G+1)/2)+1):
            n = 1
            total = k
            while True:
                if total > G:
                    break
                elif total == G:
                    count += 1
                    break
                else:
                    total += (k+n)
                    n += 1

    print(f"Case #{i+1}: {count}")
