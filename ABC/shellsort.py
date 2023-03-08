# shell sort 

class Solution:
    def shell_sort(lst):
        step = len(lst) // 2
        while step > 0:
            for i in range(step, len(lst)):
                j = i
                tmp = lst[j]
                while j >= step and lst[j-step] > tmp:
                    lst[j] = lst[j-stem]
                    j -= step
                lst[j] = tmp
            step = step // 2
            

            s = Solution()
