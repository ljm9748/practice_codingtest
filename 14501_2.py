
n=int(input())
myinp=[[0,0]]
for _ in range(n):
    myinp.append(list(map(int, input().split())))
dp=[0]*(n+1)
 
for i in range(1, n+1):
    #print("i는",i)
    if(dp[i-1]>dp[i]):
        dp[i]=dp[i-1]
    #print(dp)
    if((i-1+myinp[i][0])<n+1):
        if(dp[i-1+myinp[i][0]]<dp[i-1]+myinp[i][1]):
            dp[i-1+myinp[i][0]]=dp[i-1]+myinp[i][1]
    
    #print(dp)
    
print(dp[n])