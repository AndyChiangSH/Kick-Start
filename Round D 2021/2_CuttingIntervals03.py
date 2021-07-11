# 2
import sys


class MaxHeap:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.front = 0
        self.heap = [0]*(self.maxSize + 1)
        self.heap[0] = sys.maxsize

    def swim(self, k):
        while k > 1 and self.heap[int(k/2)] < self.heap[k]:
            print(f"k = {k}, int(k/2) = {int(k/2)}")
            self.swap(k, int(k/2))
            k = int(k/2)

    def sink(self, k):
        while 2*k <= N:
            j = 2*k
            if j < self.maxSize and self.heap[j] < self.heap[j+1]:
                j += 1
            if not (self.heap[k] < self.heap[j]):
                break
            self.swap(k, j)
            k = j

    def push(self, x):
        self.front += 1
        self.heap[self.front] = x
        self.swim(self.front)

    def pop(self):
        Max = self.heap[1]
        self.swap(1, self.front)
        self.front -= 1
        self.sink(1)

        return Max

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp


T = int(input())

for t in range(T):
    row = input().split(" ")
    N = int(row[0])
    C = int(row[1])

    inters = list()
    minStart = sys.maxsize
    maxEnd = 1

    for n in range(N):
        row = input().split(" ")
        start = int(row[0])
        end = int(row[1])

        # print(f"{start}, {end}")

        if start+1 != end:
            inters.append([start, end])
            if start < minStart:
                minStart = start
            if end > maxEnd:
                maxEnd = end

    limit = min(maxEnd-minStart-1, C)
    maxheap = MaxHeap(limit)
    for i in range(minStart+1, maxEnd):
        countIn = 0
        for j in inters:
            if i > j[0] and i < j[1]:
                countIn += 1

        print(f"push = {countIn}")
        maxheap.push(countIn)

    for i in range(limit):
        print(f"max = {maxheap.pop()}")

    # print(f"Case #{t+1}: {count}")


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
