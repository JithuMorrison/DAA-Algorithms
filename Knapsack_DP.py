def dp_knapsack(arr, W):
    m = len(arr)
    n = W + 1
    dp = [[0] * n for _ in range(m + 1)]
    selected_items = [[False] * n for _ in range(m + 1)]

    for i in range(1, m + 1):
        w, v = arr[i - 1]
        for j in range(n):
            if j >= w:
                if dp[i - 1][j] > v + dp[i - 1][j - w]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = v + dp[i - 1][j - w]
                    selected_items[i][j] = True
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[m][W])

c_knapsack = [[2,10],[3,7],[4,7],[5,8],[9,13]]
W=13
dp_knapsack(c_knapsack,W)
