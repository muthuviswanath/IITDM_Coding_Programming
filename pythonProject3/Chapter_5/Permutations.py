def Permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    result = []
    for i in range (len(lst)):
        temp = lst[i]
        re_lst = lst[:i] + lst[i+1:]
        for permutation in Permutations(re_lst):
            result.append([temp]+permutation)
    return result

my_data_lst = [1,2,3]
print(f"Given list: \n {my_data_lst}")
print()
res = Permutations(my_data_lst)
print("Permutations are: \n",res)
