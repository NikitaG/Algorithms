import random

n = 100
arr = random.sample(range(0,n), n)

def heapSort(arr):
    def _leftChild(el):
        return el*2+1

    def _parent(el):
        if el > 0:
            return (el - 1) // 2
        else:
            return None

    def _heapify(arr, end):
        start = _parent(end)

        while start >= 0:
            _siftDown(arr, start, end)
            start -= 1

    def _siftDown(arr, start, end):
        root = start

        while _leftChild(root) <= end:
            left = _leftChild(root)
            swap = root

            if arr[left] > arr[swap]:
                swap = left
            if left+1 <= end and arr[left+1] > arr[swap]:
                swap = left+1

            if swap == root:
                return
            else:
                arr[swap], arr[root] = arr[root], arr[swap]
                root = swap

    end = len(arr) - 1
    _heapify(arr, end)

    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]

        end -= 1
        _siftDown(arr, 0, end)

heapSort(arr)
print(arr)