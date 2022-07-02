class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def merge_sort(self, p, r):
        if p < r:
            q = (p + r)//2
            self.merge_sort(p, q)
            self.merge_sort(q+1, r)
            self.merge(p, q, r)

    def merge(self, p, q, r):
        left = self.arr[p:q+1]
        right = self.arr[q+1:r+1]

        sorted_index = p
        i, j = 0, 0
        for k in range(r-p+1):
            if i> len(left)-1:
                self.arr[sorted_index] = right[j]
                j+=1
            elif j > len(right)-1:
                self.arr[sorted_index] = left[i]
                i+=1
            elif left[i] < right[j]:
                self.arr[sorted_index] = left[i]
                i+=1
            else:
                self.arr[sorted_index] = right[j]
                j+=1
            sorted_index += 1

    def sort(self):
        p = 0
        r = len(self.arr)-1
        self.merge_sort(p, r)
        return self.arr

if __name__ == "__main__":
    inp = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48]
    arr = MergeSort(inp)
    sorted_arr = arr.sort()
    print(sorted_arr)
