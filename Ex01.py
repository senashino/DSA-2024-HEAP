class MaxHeap:
    def __init__(self):
        self.heap = []
    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] < self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break

if __name__ == '__main__':
    heap = MaxHeap()
    for num in [5, 3, 8, 1, 2, 7, 6, 4]:
        heap.insert(num)
    print("Max Heap :", heap.heap)
