position = 0


def linear_search(lst, ele):
    ffound = False
    global position
    for i in range(len(lst)):
        if lst[i] == ele:
            ffound = True
            position = i
            break
    return ffound


numlst = [12, 23, 34, 45, 56, 98, 67, 78, 87]
element= int(input("Enter an element to be found"))
found = linear_search(numlst, element)
if found:
    print(f"Element {element} is found: {found} and at the position :{position}")
else:
    print(f"The element {element} is not found")
