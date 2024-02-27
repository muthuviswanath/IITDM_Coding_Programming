def power(b,exp):
    res = b
    for i in range (1,exp):
        res = res * b
    return res