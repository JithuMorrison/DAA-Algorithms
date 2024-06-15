def bestSearch(arr, x, l, h):
    n = h - l + 1

    if n <= 2:
        if arr[l] == x or arr[h] == x:
            return i
        return -1

    if x < arr[l] or x > arr[h]:
        return -1

    mid = l + int((x / (arr[l] + arr[h])) * n)
    lid = l + n // 2
    mid = max(l, min(mid, h))  

    if arr[mid] == x or arr[lid] == x:
        return mid
    elif arr[mid] < x:
        if arr[lid] < x:
            mid = lid
        return bestSearch(arr, x, mid + 1, h)
    else:
        if arr[lid] < x:
            mid = lid
        return bestSearch(arr, x, l, mid - 1)

arr = [5, 7, 12, 14, 16, 25, 33, 36, 44]
x = 12
result = bestSearch(arr, x, 0, len(arr) - 1)
print(result)
