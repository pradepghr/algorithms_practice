# Time Complexity: O(n*2)
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