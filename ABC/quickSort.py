# -*- encoding:utf-8 -*-
# quick sort


class Solution:
    def partition(self, lst, left, right):
        tmp = lst[right]
        while left < right:
            while left < right and lst[left] < tmp:
                left += 1
            lst[right] = lst[left]
            while left < right and lst[right] > tmp:
                right -= 1
            lst[left] = lst[right]
        lst[left] = tmp
        return left
            
    def quick_sort(self, lst, left, right):
        if left < right:
            mid = self.partition(lst, left, right)
            self.quick_sort(lst, left, mid-1)
            self.quick_sort(lst, mid+1, right)

lst = [5,1,8,4,3,0,9,2,7,6]
s = Solution()
s.quick_sort(lst, 0, len(lst)-1)
print(lst)
