class HeapSort:
    # self
    # array for heapification
    # size of array
    # root of heap
    def heapify(self, arr, n, i):
        m = i
        l = 2*i + 1
        r = 2*i + 2
        if ((l < n) and (arr[l] < arr[m])):
            m = l
        if ((r < n) and (arr[r] < arr[m])):
            m = r
        if m != i:
            arr[m], arr[i] = arr[i], arr[m]
            heapify(self, arr, n, i)
        return arr

    # array to be sorted
    def sort(self, arr):
        for i in xrange(-1, Math.floor(len(arr)/2)):
            print i

    def main():
        self.sort([1,2,3])

    if __name__ == "__main__":
        main()
