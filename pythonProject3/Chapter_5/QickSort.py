def partition(lst, first, last):
    pivot = lst[first]
    left, right = first + 1, last
    while left < right:
        print(lst)
        while left <= right and lst[left] <= pivot:
            left += 1
        while left <= right and lst[right] >= pivot:
            right -= 1
        if left < right:
            lst[left], lst[right] = lst[right], lst[left]
    pivotpoint = right
    lst[first], lst[pivotpoint] = lst[pivotpoint], lst[first]
    return pivotpoint


def QucikSort(lst, first, last):
    if first < last:
        print(lst)
        pivotpoint = partition(lst, first, last)
        QucikSort(lst, first, pivotpoint - 1)
        QucikSort(lst, pivotpoint + 1, last)


my_lst = [26,23,19,14,12,11,9]
QucikSort(my_lst, 0, len(my_lst) - 1)
