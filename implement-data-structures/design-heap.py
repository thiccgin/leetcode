class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.bubble_up(len(self.heap) - 1)

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        elif len(self.heap) == 2:
            return self.heap.pop()

        to_pop = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.bubble_down(1)
        return to_pop

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in range(len(self.heap) // 2 + 1, 0, -1):
            self.bubble_down(i)

    def bubble_up(self, i):
        while i > 1:
            pi = i // 2
            if self.heap[pi] > self.heap[i]:
                self.heap[i], self.heap[pi] = self.heap[pi], self.heap[i]
                i = pi
            else:
                break

    def bubble_down(self, i):
        child = 2 * i
        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child+1] < self.heap[child]:
                child += 1
            
            if self.heap[child] >= self.heap[i]:
                return
            self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child
            child = 2 * i
        
        