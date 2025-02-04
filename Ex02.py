class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
        
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)
            
    def extract_max(self):
        if not self.heap:
            return None
        max_val = self.heap[0]
        last = self.heap.pop() 
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return max_val
    
    def _heapify_down(self, index):
        n = len(self.heap)
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
            
if __name__ == '__main__':

    heap = MaxHeap()
    for num in [5, 3, 8, 1, 2, 7, 6, 4]:
        heap.insert(num)
    print("Initial Heap:", heap.heap)
    
    for i in range(3):
        removed = heap.extract_max()
        print(f"After deletion {i+1} ({removed}):", heap.heap)
