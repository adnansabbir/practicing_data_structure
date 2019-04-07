class BinaryHeap:

    def __init__(self):
        self.heap_list = [0]
        self.currentsize = 0

    def insert(self, object):
        self.heap_list.append(object)
        self.currentsize += 1
        self.percolation(self.currentsize)

    def delete_min(self):
        if self.currentsize < 1:
            return None

        min_value = self.heap_list[1]
        self.heap_list[1], self.heap_list[self.currentsize] = self.heap_list[self.currentsize], self.heap_list[1]
        self.heap_list.pop()
        self.currentsize -= 1

        i = 1
        while i*2 <= self.currentsize:
            mci = self.min_child_index(i)

            if self.heap_list[i] > self.heap_list[mci]:
                self.heap_list[i], self.heap_list[mci] = self.heap_list[mci], self.heap_list[i]
            i = mci

        return min_value

    def min_child_index(self, i):
        if i*2+1 > self.currentsize:
            return i*2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i*2
            return i*2+1

    def percolation(self, i):
        while i//2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
                i = i//2

    def __str__(self):
        return "{}".format(self.heap_list)
