# 每个物品只有一个
w = [0,2,3,4,7]   #每个物品的重量
c = [0,1,3,5,9]   #每个物品的价值
m=10       #背包最大容量
n=4        #物品种数



dp = [ [0 for _ in range(m+1) ] for i in range(n+1)]



for i in range(1,n+1):
    for j in range(1,m+1):
        # 当前状态只与上一个状态有关
        if j<w[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+c[i])



# 通过状态转移方程，对dp数据进行压缩
dp1 = [0 for _ in range(m+1)]
for i in range(1,n+1):
    for j in range(m,0,-1):   #这里需要先对大的值进行判断，所以从后面进行遍历
        if j<w[i]:
            dp1[j]=dp1[j]
        else:
            dp1[j]=max(dp1[j],dp1[j-w[i]]+c[i])



for i in dp1:
    print(i)
print(dp1[m])