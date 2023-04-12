def linear_search(values, target):
   n = len(values)
   for i in range(n):
       if values[i] == target:
           return i

   return -1
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            #print("found")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # target not found in arr
# def binary_search(values,target):
