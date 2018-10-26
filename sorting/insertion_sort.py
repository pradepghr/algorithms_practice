"""
When people manually sort cards in a bridge hand, most use a method that is similar to insertion sort.
Time Complexity: O(n*2)
Stable; i.e., does not change the relative order of elements with equal keys
"""

def insertion_sort(l):
    m = len(l)
    i = 0
    while i < m:
        j = i+1
        while j < m:
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
            j += 1
        i += 1
        print(l)
    return l


li = [24, 32, 10, 7, 5, 6, 1, 86, 34, 23, 54, 22, 12, 4]

sorted_li = insertion_sort(li)