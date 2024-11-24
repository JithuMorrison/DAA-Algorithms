def bin_search(lst, key, l, h):
    if (h < l):
        return None
    mid = l + (h - l) // 2
    if mid > -1 and lst[mid] == key:
        return mid
    elif key > lst[mid]:
        return bin_search(lst, key, mid + 1, h)
    elif key < lst[mid]:
        return bin_search(lst, key, l, mid - 1)
