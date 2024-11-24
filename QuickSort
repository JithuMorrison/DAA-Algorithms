def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

def output(array,n):
  quicksort(array,0,len(array)-1)
  return array[n-1]
s=[11,2,9,7,5,3]
quicksort(s,0,len(s)-1)
print(s)
print(output(s,3))
