# In bubble sort,  it compares adjacent items and exchanges those that are out of order
# In list of n elements, there are n-1 passes
# algorithm can be improved with check for sorting i.e break if already sorted.


def bubble_sort(l):
    switch = True
    m = len(l)
    while m >= 0 and switch:
        switch = False
        n = m
        for i in range(n-1):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
                switch = True
        m -= 1
        print(l)
    return l


li = [2, 5, 6, 1, 86, 34, 23, 54, 22, 12, 4]
sorted_li = bubble_sort(li)