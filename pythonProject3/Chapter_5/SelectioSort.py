def SelectionSort(lst):
    temp = []
    while len(lst) > 0:
        print(temp,lst)
        small = lst.index(min(lst))
        temp.append(lst[small])
        lst.pop(small)
    return temp

my_lst = [50,30,40,10,20]
print(SelectionSort(my_lst))