class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[i//2]
                self.heaplist[i//2] = tmp
            i = i // 2

    def insert(self, k):
        self.heaplist.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def minChild(self, i):
        if 2 * i + 1 > self.currentSize:
            return 2 * i
        else:
            if self.heaplist[2 * i] < self.heaplist[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def delMin(self):
        delmin = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.percDown(1)
        return delmin

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize += len(alist)
        self.heaplist.extend(alist)
        while i > 0:
            self.percDown(i)
            i -= 1


bh = BinHeap()
n = int(input())
for i in range(n):
    ope = list(map(int, input().split()))
    if ope[0] == 1:
        bh.insert(ope[1])
    if ope[0] == 2:
        print(bh.delMin())
