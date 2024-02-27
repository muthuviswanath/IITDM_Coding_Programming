def maxSum(lst, window):
    n = len(lst)
    if n < window:
        print("Invalid operation")
        return -1
    max_sum = sum(lst[:window])
    window_sum = max_sum
    for i in range(n - window):
        window_sum = window_sum - lst[i] + lst[i + window]
        max_sum = max(max_sum, window_sum)
    return max_sum

lst = [2,1,3,8,4,6,3,8]
window = 3
print(maxSum(lst, window))