# 20240313
# dp

C = int(input())
dp = [0] * (C+1)

if C == 0:
    print(0)
elif C == 1:
    print(1)
elif C == 2:
    print(0+1)
else:
    dp[:2] = [0, 1]
    for i in range(2, C+1):
        dp[i] = sum(dp[i-2:i])
    print(dp[-1])