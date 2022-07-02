class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def shift_right_and_insert(self, key, i):
        while i > 0 and self.arr[i-1] > key:
            self.arr[i] = self.arr[i-1]
            i -= 1
        self.arr[i] = key

    def sort(self):
        for i, key in enumerate(self.arr):
            self.shift_right_and_insert(key, i)
        return self.arr


if __name__ == "__main__":
    inp = [2, 4, 4, 7, 2, 1]
    arr = InsertionSort(inp)
    sorted_arr = arr.sort()
    print(sorted_arr)
