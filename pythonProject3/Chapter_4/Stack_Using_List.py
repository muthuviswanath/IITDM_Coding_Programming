class Mouse:
    pass
number_stack= []

def push(number_stack,item):
    number_stack.append(item)

def pop(number_stack):
    if len(number_stack) != 0:
        return number_stack.pop()
    else:
        print("Stack is empty. cannot pop")

def is_Empty(number_stack):
    if len(number_stack) == 0:
        print("Stack is empty")
    else:
        print("Stack is not empty")
def displayStack_InReverse_1(number_stack):
    for i in range(len(number_stack)-1,-1,-1):
        print(number_stack[i])

def displayStack_InReverse_2(number_stack):
    print(number_stack[::-1])

def displayStack_Inforward1(number_stack):
    print(number_stack)

def displayStack_Inforward2(number_stack):
    for i in range (0,len(number_stack)):
        print(number_stack[i])

def displayStack_Inforward3(number_stack):
    for i in number_stack:
        print(i)

push(number_stack,123)
push(number_stack,"Laptop")
push(number_stack,5j+4)
push(number_stack,2343.45)
push(number_stack,True)
push(number_stack,Mouse())
displayStack_InReverse_1(number_stack)
displayStack_InReverse_2(number_stack)
