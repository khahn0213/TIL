# 2024/03/12 - Nota
# ref: n9095 baekjoon

dp = [0] * 12
dp[1:4] = [1, 2, 4]
for i in range(4, 12):
    dp[i] = sum(dp[i-3:i])
    
TC = int(input())
for _ in range(TC):
    N = int(input())
    print(dp[N])


    
