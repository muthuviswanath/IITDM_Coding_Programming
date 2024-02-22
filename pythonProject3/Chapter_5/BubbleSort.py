my_lst = [50,30,40,10,20]
print(f"List Before Bubble Sort:\n {my_lst}")
for i in range (0, len(my_lst)):
    for j in range(i+1,len(my_lst)):
        if  my_lst[i] > my_lst[j]:
            temp = my_lst[i]
            my_lst[i] = my_lst[j]
            my_lst[j] = temp

print(f"List after Bubble Sort:\n {my_lst}")

my_lst = [50,30,40,10,20]
def bubble_sort(lst):
    for i in range(len(lst)):
        print(lst)
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1],lst[j]

bubble_sort(my_lst)