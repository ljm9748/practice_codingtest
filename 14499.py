mydiceB=[0]*6
mydiceA=[0]*6
order=[]
mymap=[]
dx=[0, 0, 0, -1, 1]
dy=[0, 1, -1, 0, 0]
way=0

n, m, x, y, k= map(int, input().split())
for _ in range(n):
    mymap.append(list(map(int, input().split())))
order=list(map(int, input().split()))
print(order)



def movedice(way):
    global mydiceA, mydiceB
    if way== 1:#동
        mydiceA=[mydiceB[4],mydiceB[1],mydiceB[5],mydiceB[3],mydiceB[2],mydiceB[0]]
        mydiceB=mydiceA[:]
    elif way == 2:#서
        mydiceA=[mydiceB[5],mydiceB[1],mydiceB[4],mydiceB[3],mydiceB[0],mydiceB[2]]
        mydiceB=mydiceA[:]
    elif way == 3:#북
        mydiceA=[mydiceB[3],mydiceB[0],mydiceB[1],mydiceB[2],mydiceB[4],mydiceB[5]]
        mydiceB=mydiceA[:]
    else:#남
        mydiceA=[mydiceB[1],mydiceB[2],mydiceB[3],mydiceB[0],mydiceB[4],mydiceB[5]]
        mydiceB=mydiceA[:]
        
for ord in order:
    x += dx[ord]
    y += dy[ord]
    if (0 <= x < n) and (0<= y < m):
        movedice(ord)
        if mymap[x][y]==0:
            mymap[x][y]=mydiceA[2]
        else:
            mydiceB[2]=mymap[x][y]
        print(mydiceB[0])
    else:
        x -= dx[ord]
        y -= dy[ord]
        
            