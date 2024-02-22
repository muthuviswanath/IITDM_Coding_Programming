def Selection_Sort(lst):
    for i in range(len(lst)-1):
        print(lst)
        small = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[small]:
                small = j
        lst[i], lst[small] = lst[small],lst[i]

my_lst = [50, 30, 40, 10, 20]
print(Selection_Sort(my_lst))