# -*- encoding:utf-8 -*-
# bubble sort

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
                
lst = 
bubble_sort(lst)
print(lst)
