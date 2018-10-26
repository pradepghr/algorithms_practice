"""
Uses divide and conquer approach.
A quick sort first selects a value, which is called the pivot value (to assist with splitting the list).
Although there are many different ways to choose the pivot value, we will simply use the first item in the list.

1. choose first element as pivot.
2. choose leftmark (element after pivot) and rightmark(last element)
3. begin with leftmark, if next element is less than or equal to pivot  then move leftmark to right else stop and
   begin from rightmark if greater than pivot then move rightmark to left else stop
   exchange leftmark and rightmark.
4. continue leftmark and rightmark until rightmark < leftmark i.e split point found then
    exchange pivot and rightmark
5. split list into two group (< pivot and > pivot) without pivot element
6. repeat 1-5 for each group

"""


def quick_sort(alist):
    sort(alist, 0, len(alist)-1)


def sort(alist, first, last):
    # print("first:{}, last:{}, list:{} ".format(first, last, alist))
    if first < last:
        split_point = partition(alist, first, last)
        sort(alist, first, split_point-1)
        sort(alist, split_point+1, last)


def partition(alist, first, last):
    split_point = 1
    pivot = alist[first]
    left_mark = first + 1
    right_mark = last
    stop = False
    while not stop:
        print("pivot:{}, lm:{}, rm:{}, list:{} ".format(pivot, alist[left_mark], alist[right_mark] , alist))
        print('begin with left mark')
        while left_mark <= right_mark and alist[left_mark] <= pivot:
            print("pivot:{}, lm:{}, rm:{}, list:{} ".format(pivot, alist[left_mark], alist[right_mark], alist))
            left_mark += 1
        print('stop: {} greater than {}'.format(alist[left_mark],pivot))
        print("pivot:{}, lm:{}, rm:{}, list:{} ".format(pivot, alist[left_mark], alist[right_mark] , alist))
        print('begin with right mark')
        while alist[right_mark] >= pivot and right_mark >=left_mark:
            print("pivot:{}, lm:{}, rm:{}, list:{} ".format(pivot, alist[left_mark], alist[right_mark], alist))
            right_mark -= 1
        # check  rightmark < leftmark i.e split point found
        print('stop: {} less than {}'.format(alist[right_mark], pivot))
        if right_mark < left_mark:
            print('stop since right mark{} < left mark{}'.format(right_mark,left_mark))
            stop = True
        else:
            # exchange elements
            print('exchange {} and {}'.format(alist[left_mark],alist[right_mark]))
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
    #  Since split point found exchange pivot and rightmark
    alist[first], alist[right_mark] = alist[right_mark], alist[first]
    split_point = right_mark
    return split_point


arr = [2, 5, 6, 1, 86, 34, 23, 54, 22, 12, 4]
quick_sort(arr)
