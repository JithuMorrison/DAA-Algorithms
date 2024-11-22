def long_pal(s):
    n = len(s)
    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2,n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i]==s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
    print("\nTable :")
    for row in dp:
        for val in row:
            print(val, end = ' ')
        print()

    return dp[0][n-1]


s = input("Enter a word : ")
x = long_pal(s)
print("longest palindromic subsequence =", x)
