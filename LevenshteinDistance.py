def edit_dist(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    print("\nTable :")
    for row in dp:
        for val in row:
            print(val, end = ' ')
        print()

    return dp[m][n]

s1 = input("Enter word1 : ")
s2 = input("Enter word2 : ")

x = edit_dist(s1,s2)
print("\nEdit distance =",x)
