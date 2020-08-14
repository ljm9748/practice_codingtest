maxval=0
mymap=[]
dx=[0,-1,0,1] #좌 상 우 하
dy=[-1,0,1,0]
ex=[[0, -1, -2, -1], [0, -1, -2, -1], [0, -1, -1, -1], [0, 0, 0, -1]]
ey=[[0, 0, 0, 1], [0, 0, 0, -1], [0, -1, 0, 1], [0, 1, 2, 1]]
check=[]

n, m=map(int, input().split())
for _ in range(n):
    mymap.append(list(map(int, input().split())))
    check.append([False]*m)
    
def dfs(cnt, value, x, y):
    global check, maxval
    if cnt == 3:
        maxval=max(maxval, value)
    else:
        for i in range(4):
            newx=x+dx[i]
            newy=y+dy[i]  
            if 0<=newx<n and 0<=newy<m:
                if check[newx][newy]==False:
                    check[newx][newy]=True
                    dfs(cnt+1, value+mymap[newx][newy], newx, newy)
                    check[newx][newy]=False
def findexept(x, y):
    global maxval
    for i in range(4):
        tmp=0
        for j in range(4):
            if 0<=x+ex[i][j]<n and 0<=y+ey[i][j]<m:
                tmp += mymap[x+ex[i][j]][y+ey[i][j]]
                if j == 3:
                    maxval=max(maxval, tmp)
            else:
                break        
    
for i in range(n):
    for j in range(m):
        check[i][j]=True
        dfs(0, mymap[i][j], i, j)
        check[i][j]=False
        findexept(i, j)
        
    
print(maxval)        
