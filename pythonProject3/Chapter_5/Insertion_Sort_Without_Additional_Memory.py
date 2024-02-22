def InsertionSort(lst):
    for i in range(1,len(lst)):
        print(lst)
        x = lst[i]
        j = i-1
        while j>=0 and lst[j] > x:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = x

my_lst = [50, 30, 40, 10, 20]
InsertionSort(my_lst)
print(my_lst)
