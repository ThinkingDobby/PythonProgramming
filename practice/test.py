def count_partitions(n, k):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(k+1):
        dp[0][i] = 0

    for i in range(n+1):
        dp[i][1] = 1

    for i in range(2, n+1):
        for j in range(2, k+1):
            dp[i][j] = dp[i-1][j-1] + j*dp[i-1][j]

    return dp[n][k]

n = 6
k = 4
print(count_partitions(n, k))  # Output: 25
