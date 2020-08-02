from collections import deque
n, m= input().split()
n=int(n)
m=int(m)
inputList=[]
check=[]
myqueue=deque()
answer=0
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
for _ in range(n):
    tmp=input()
    inputList.append(list(tmp))
for _ in range(n):
    check.append([False]*m)
    
for i in range(n):
    for j in range(m):
        if inputList[i][j]=='L':
            myqueue.append([i, j, 0])
            check[i][j]=True
            while len(myqueue)>0:
                for k in range(4):
                    newn=myqueue[0][0]+dx[k]
                    newm=myqueue[0][1]+dy[k]
                    if newn>=0 and newn<n and newm>=0 and newm<n:
                        if check[newn][newm]==False and inputList[newn][newm]=='L':
                            check[newn][newm]=True
                            myqueue.append([newn, newm, myqueue[0][2]+1])
                            answer=max(answer, myqueue[0][2]+1)
                #del myqueue[0]
                myqueue.popleft()
                #print("myqueue: ", myqueue, "x y:", i, j)
            check=[]
            for _ in range(n):
                check.append([False]*m)
            
        
        
print(answer)
        