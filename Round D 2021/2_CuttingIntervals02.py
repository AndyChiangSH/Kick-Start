# 2
import sys


class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
                                            self.Heap[fpos])

    # Function to heapify the node at pos
    def maxHeapify(self, pos):
        # If the node is a non-leaf node and smaller
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                # Swap with the left child and heapify
                # the left child
                if (self.Heap[self.leftChild(pos)] >
                        self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] >
               self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return popped

    def printHeap(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) +
                  " LEFT CHILD : " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))


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
    maxheap = MaxHeap(limit*2)
    for i in range(minStart+1, maxEnd):
        countIn = 0
        for j in inters:
            if i > j[0] and i < j[1]:
                countIn += 1

        print(f"countIn = {countIn}")
        maxheap.insert(countIn)

    maxheap.printHeap()

    for i in range(limit):
        print(f"max = {maxheap.extractMax()}")

    maxheap.printHeap()

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
