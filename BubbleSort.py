class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for n in range(len(self.arr)-1, 0, -1):
            swapped = False
            for i in range(n):
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    swapped = True
            if not swapped:
                return self.arr
        return self.arr

if __name__ == "__main__":
    inp = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48]
    arr = BubbleSort(inp)
    sorted_arr = arr.sort()
    print(sorted_arr)
