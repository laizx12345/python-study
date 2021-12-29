# 每个物品无限个
w = [0,2,3,4,7]   #每个物品的重量
c = [0,1,3,5,9]   #每个物品的价值
m=10       #背包最大容量
n=4        #物品种数

# dp1 = [0 for _ in range(m+1)]
# for i in range(1,n+1):
#     for j in range(m,0,-1):   #这里需要先对大的值进行判断，所以从后面进行遍历
#         k=0
#         while k<=int(j/w[i]):
#             dp1[j]=max(dp1[j],dp1[j-k*w[i]]+k*c[i])
#             # print(dp1)
#             k+=1
# print(dp1[m])

dp2 = [0 for _ in range(m+1)]
for i in range(1,n+1):
    for j in range(w[i],m+1):   
        dp2[j]=max(dp2[j],dp2[j-w[i]]+c[i])
print(dp2[m])

