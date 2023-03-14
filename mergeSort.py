# merge sort


import math
class Solution:
    def merge(self, lst1, lst2):
        n = len(lst1) + len(lst2)
        lst1.append(math.inf)
        lst2.append(math.inf)
        lst = []
        i, j = 0, 0
        while i+j < n:
            if lst1[i] < lst2[j]:
                lst.append(lst1[i])
                i += 1
            else:
                lst.append(lst2[j])
                j += 1
        return lst
    
    def merge_sort(self, lst):
        n = len(lst)
        if n == 1:
            return lst
        lst1 = lst[:n//2]
        lst2 = lst[n//2:]
        sorted_lst1 = self.merge_sort(lst1)
        sorted_lst2 = self.merge_sort(lst2)
        return self.merge(sorted_lst1, sorted_lst2)

lst = [3,0,5,7,1,9,2,6,4,8]
s = Solution()
lst = s.merge_sort(lst)
print(lst)
