def insertionSort(arr,n):
    i=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr[n-1]
s=[1,2,9,7,5,3]
n=eval(input("enter k: "))
print(n,"th ancestor: ",insertionSort(s,n))
print(s)
