from Chapter_4.Stack_Using_Class import Stack


def paranthesis_check(expr):
    open = "[{(<"
    close = "]})>"
    st = Stack()
    for char in expr:
        if char in open:
            st.push(char)
        elif char in close:
            if st.is_empty():
                return False
            if open.index(st.pop()) != close.index(char):
                return False
    return st.is_empty()

st = input("Enter an expression containing Brackets")
print("valid" if paranthesis_check(st) else "Invalid")

