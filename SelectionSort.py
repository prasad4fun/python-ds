class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)

        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                 if self.arr[j] < self.arr[min_idx]:
                     min_idx = j
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]

        return self.arr

if __name__ == "__main__":
    inp = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48]
    arr = SelectionSort(inp)
    sorted_arr = arr.sort()
    print(sorted_arr)
