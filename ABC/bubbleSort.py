# -*- encoding:utf-8 -*-
# bubble sort

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
                

lst = [5,1,8,4,3,0,9,2,7,6]
bubble_sort(lst)
print(lst)
