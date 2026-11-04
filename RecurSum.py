def recurSum(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + recurSum(arr, n - 1)

arr = [1,2,3,4,5]
n = len(arr)
print(recurSum(arr, n))