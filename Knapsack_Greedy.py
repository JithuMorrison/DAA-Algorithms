def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),knapSack(W, wt, val, n-1))

weight = [2, 3, 4, 5, 9]
profit = [10, 7, 7, 8, 13]
W = 13
n = len(profit)
print(knapSack(W, weight, profit, n))
