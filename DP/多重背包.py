# 每个物品有n[i]个
w = [0, 80, 40, 30, 40, 20]  # 每个物品的重量
c = [0, 20, 50, 50, 30, 20]  # 每个物品的价值
s = [0, 4, 9, 7, 6, 1]       # 每个物品的个数
m = 1000  # 背包最大容量
n = 5  # 物品种数

dp1 = [0 for _ in range(m+1)]
for i in range(1,n+1):
    for j in range(m,0,-1):   
        k=0
        while k<=s[i] and j>=k*w[i]:
            dp1[j] = max(dp1[j],dp1[j-k*w[i]]+k*c[i])
            k+=1


print(dp1[m])