def solution(m, n, puddles):
    answer = 0
    mylist=[]
    for _ in range(n+1):
        mylist.append([0]*(m+1))
    for x, y in puddles:
        mylist[y][x]=-1

    mylist[1][1]=1
    for i in range(1,n+1):
        for j in range(1, m+1):
            if mylist[i][j] != -1:
                if mylist[i-1][j] != -1:
                    mylist[i][j] = ((mylist[i][j])%1000000007+mylist[i-1][j]%1000000007)%1000000007
                if mylist[i][j-1] != -1:
                    mylist[i][j] = (mylist[i][j]%1000000007+mylist[i][j-1]%1000000007)%1000000007

    print(mylist)

    return mylist[n][m]

solution(4,3,[[2, 2]])