n,m=map(int, input().split())

inpList=[]
mymap=[]
for _ in range(n):
    inpList.append(list(map(int, input().split())))
    mymap.append([False]*m)
    
#벽세우기 
def build(howmany):
    if howmany == 3:
        print("howmany는 3!")
        print(inpList)
        #안전영역 탐색
    else:
        for i in range(n):
            for j in range(m):
                #엔과 엠을 이용해 벽을 세우고 벽이 3이면 bfs함수를 실행?!
                if inpList[i][j]==0:
                    inpList[i][j]=1
                    build(howmany +1)
                    inpList[i][j]=0

build(0)        
print(inpList)
print(mymap)

