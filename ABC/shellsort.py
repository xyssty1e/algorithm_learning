# -*- encoding:utf-8 -*-
# shell sort 

class Solution:
    def shell_sort(self, lst):
        step = len(lst) // 2
        while step > 0:
            for i in range(step, len(lst)):
                j = i
                tmp = lst[j]
                while j >= step and lst[j-step] > tmp:
                    lst[j] = lst[j-step]
                    j -= step
                lst[j] = tmp
            step = step // 2
            
lst = [5,1,8,4,3,0,9,2,7,6]
s = Solution()
s.shell_sort(lst)
print(lst)
