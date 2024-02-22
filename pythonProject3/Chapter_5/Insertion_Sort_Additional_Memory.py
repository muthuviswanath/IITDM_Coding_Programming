def InsertionSort(lst):
    temp = []
    while len(lst) > 0:
        print(temp, lst)
        a = lst.pop(0)
        b = len(temp) - 1
        while b >= 0 and temp[b] > a:
            b -=1
        temp.insert(b+1,a)
    return temp

my_lst = [50, 30, 40, 10, 20]
print(InsertionSort(my_lst))

# temp [50][30,40,10,20]
# temp [50][30,40,10,20]