# the maximum number of item that can be stored in the heap
CAPACITY = 10

class Heap(object):

    def __init__(self):
        # create an array with as many slot as the capacity
        self.heap = [0]*CAPACITY
        # we want to track the size
        self.heap_size = 0

    def insert(self, item):

        # if not able to insert more items than the value of the CAPACITY
        if CAPACITY == self.heap_size:
            return

        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size + 1

        # if the heap properties are violated
        self.fix_up(self.heap_size - 1)

    def fix_up(self, index):
        parent_index = (index - 1) // 2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def get_max(self):
        return self.heap[0]

    #method to remove a item ( delete node)
    def poll(self):
        max = self.get_max()
        self.swap(0, self.heap_size - 1)
        self.heap_size = self.heap_size - 1
        self.fix_down(0)
        return max

    def fix_down(self, index):

        index_left = 2 * index + 1
        index_right = 2 * index  + 2
        index_largest = index

        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            index_largest = index_left

        if index_right < self.heap_size and self.heap[index_right] > self.heap[index]:
            index_largest = index_right

        if index != index_largest:
            self.swap(index, index_largest)
            self.fix_down(index_largest)
    # sorting method is a O(N) complexity because of loop but for each iteration finding max (refer to the poll method)
    # having O(log N) complexity .
    # overall complexity of heap_sort = O(N*LogN)
    def heap_sort(self):

        size = self.heap_size
        for i in range(0, size):
            max = self.poll()
            print(max)

if __name__ == "__main__":
    heap = Heap()
    heap.insert(10)
    heap.insert(8)
    heap.insert(12)
    heap.insert(20)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(1)
    heap.insert(321)

    heap.heap_sort()
    print('\n')


# Heap implementation using the python liabraries
from heapq import heapify, heappop, heappush
heap = []
nums = [12, 3, -2, 6, 4, 8, 9]
for num in nums:
    heappush(heap, num)
    
while heap:
    print(heappop(heap))
print('\n')

heapify(nums)
print(nums)
