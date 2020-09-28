
n=int(input())
myinp=[]
for _ in range(n):
    myinp.append(list(map(int, input().split())))
dp=[0]*(n)

for i in range(n):
    day=myinp[i][0]
    val=myinp[i][1]
    if i+day-1<=(n-1):
        for j in range(i+day-1, n):
            dp[j]=max(dp[j], dp[i+day-2]+val)
print(dp[n-1])