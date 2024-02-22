from random import randint
def RandomPartition(S,low,high):
    rand= randint(low,high)
    S[low],S[rand] = S[rand],S[low]
    pivot,left,right = S[low], low, high
    print(S,left, right,"pivot = ",  pivot)
    while left < right:
        while left < high and S[left] <= pivot:
            left += 1
        while right > low and pivot <= S[right]:
            right -= 1
        if left < right:
            S[left],S[right] = S[right],S[left]
    S[low],S[right] = S[right],S[low]
    return right

def QucikSort(lst, first, last):
    if first < last:
        print(lst)
        pivotpoint = RandomPartition(lst, first, last)
        QucikSort(lst, first, pivotpoint - 1)
        QucikSort(lst, pivotpoint + 1, last)

mylst = [26, 23, 19, 14, 12, 11, 9]
QucikSort(mylst,0,len(mylst)-1)
print(mylst)