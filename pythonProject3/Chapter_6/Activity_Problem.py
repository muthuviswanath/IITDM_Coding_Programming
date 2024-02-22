def allocate_conference_hall(start,finish):
    r = []
    i = 0 #i=0
    r.append(i)
    for j in range(1,len(start)):
        if finish[i] <= start[j]:
            r.append(j)
            i = j
    return r

start = [1,3,2,0,5,8,5]
complete = [3,4,8,9,10,12,7]
allocation = allocate_conference_hall(start, complete)
maxi = len(allocation)
print(allocation, maxi)