def binary_search_iteration(nums,element):
    low, high = 0, len(nums)-1
    while low <= high:
        mid =(low+high)//2
        if nums[mid] == element:
            return mid
        elif nums[mid] > element:
            high = mid -1
        else:
            low = mid +1
    return -1

my_lst = [1,7,3,6,2,9]
inp = sorted(my_lst)
print(binary_search_iteration(inp,6))

def binary_search_dandc(lst, element, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) //2
        if lst[mid] == element:
            return mid
        elif lst[mid] > element:
            return binary_search_dandc(lst,element,low, mid -1)
        else:
            return binary_search_dandc(lst, element, mid+1,high)


my_lst = [1,7,3,6,2,9]
inp = sorted(my_lst)
print(binary_search_dandc(inp,6,0,5))
