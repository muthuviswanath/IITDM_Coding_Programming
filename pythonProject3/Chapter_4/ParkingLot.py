Entry_List = [2,3,1,4,5]
Parking_List =[]
Exit_List =[]
for i in range (len(Entry_List)-1,-1,-1):
    entry_list_min = min(Entry_List)
    # if the last element is greater than the minimum element in the Entry list, then push it to Parking_list
    if Entry_List[i] > Entry_List[i-1] and Entry_List[i] > entry_list_min:
        Parking_List.append(Entry_List[i])
        print(f"Parking Lot: {Parking_List}")
    # else push it to the Exitlist
    else:
        Exit_List.append(Entry_List[i])
        print(f"Exit Lot: {Exit_List}")
# After done with the entry list data, iterate the parking list and pop things out to exit list

for i in range (0,len(Parking_List)):
    Exit_List.append(Parking_List.pop())
    print(f"Exit Lot: {Exit_List}")

print("-----------------------------")
print(f"Final Entry List: {Entry_List}")
print(f"Final Parking List: {Parking_List}")
print(f"Final Exit List: {Exit_List}")
print("-----------------------------")