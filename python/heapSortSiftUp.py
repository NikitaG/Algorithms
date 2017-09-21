import random

n = 10
arr = random.sample(range(0,n), n)

def heapSort(arr):
    def _heapify(arr, end):
        current = 1
        while current <= end:
            _siftUp(arr, 0, current)
            current += 1
    def _siftUp(arr, start, end):
        child = end
        while child > start:
            parent = (child - 1) // 2
            if arr[parent] < arr[child]:
                arr[parent], arr[child] = arr[child], arr[parent]
                child = parent
            else:
                return
    end = len(arr)-1
    _heapify(arr, end)

    while end >= 0:
        arr[0], arr[end] = arr[end], arr[0]
        end -= 1
        _heapify(arr, end)

heapSort(arr)
print(arr)