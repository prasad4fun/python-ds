class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def partition(self, strt_idx, end_idx):
        """Swap elements less than pivot to left and rest to right"""
        pivot = self.arr[strt_idx]
        low = strt_idx
        for i, high in enumerate(range(strt_idx+1, end_idx+1)):
            if self.arr[high] <= pivot:
                low += 1
                self.swap(low, high)

        #update pivot to last low value
        self.swap(strt_idx, low)
        return low

    # tmp_idx = 0
    def sort(self, strt_idx, end_idx):
        if strt_idx < end_idx:
            pivot_idx = self.partition(strt_idx, end_idx)
            #break and solve subarray on left and ride side of pivot idx
            self.sort(strt_idx, pivot_idx-1)
            self.sort(pivot_idx+1, end_idx)
        return self.arr


if __name__ == "__main__":
    inp = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48]
    arr = QuickSort(inp)
    sorted_arr = arr.sort(0, len(inp)-1)
    print(sorted_arr)
