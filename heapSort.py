# heap sort


class Solution:
    def heapify(self, lst, n, i):
        largest = i
        left = i*2+1
        right = i*2+2
        if left < n and lst[left] > lst[largest]:
            largest = left
        if right < n and lst[right] > lst[largest]:
            largest = right
        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            self.heapify(lst, n, largest)

    def heap_sort(self, lst):
        n = len(lst)
        for i in range(n//2, -1, -1):
            self.heapify(lst, n, i)
        for i in range(n-1, 0, -1):
            lst[i], lst[0] = lst[0], lst[i]
            self.heapify(lst, i, 0)

lst = [3,0,5,7,1,9,2,6,4,8]
s = Solution()
s.heap_sort(lst)
print(lst)
