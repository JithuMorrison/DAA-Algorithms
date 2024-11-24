def shell_sort(l, n):
    incr = n // 2
    while(incr > 0):
        for i in range(incr, n):
            j = i - incr
            while(j > 0):
                if (l[j] > l[j + incr]):
                    l[j], l[j + incr] = l[j + incr], l[j]
                j -= 1
            else:
                j = 0
        incr //= 2
    return l
