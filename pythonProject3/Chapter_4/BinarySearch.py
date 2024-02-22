def binary_search(lst,ele):
    first = 0
    last = len(lst)-1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if lst[mid] == ele:
            found = True
        else:
            if ele < lst[mid]:
                last = mid -1
            else:
                first = mid + 1
    return found

numlst = [12, 23, 34, 45, 56, 98, 67, 78, 87]
numlst.sort()
print(f"Given List: \n {numlst}")
print()
ele = int(input("Enter the element to be found"))
Found = binary_search(numlst, ele)
print(f"Element {ele} is found: {Found}")