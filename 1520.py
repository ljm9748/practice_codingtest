import sys
#sys.readline()
#tmp=copy.deepcopy(원래꺼)->완전한 복사를 위해 사용

def dfs(x, y):
    global ans
    if x==n-1 and y== m-1:
        ans +=1
        return;
    for i in range(4):
        newx= x+dx[i]
        newy= y+dy[i]
        if 0<=newx<n and 0<=newy<m:
            if mymap[newx][newy]==0 and li[x][y]>li[newx][newy]:
                mymap[newx][newy]=1
                dfs(newx, newy)
                mymap[newx][newy]=0
                
ans=0
dx=[-1, 0, 1, 0]
dy=[0, -1, 0, 1]
n, m= map(int, input().split())
li=[]
mymap=[]
for i in range(n):
    tmp=map(int, input().split())
    li.append(list(tmp))
    mymap.append([0]*m)
print(li)
print(mymap)

dfs(0,0)
print(ans)

