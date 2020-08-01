def solution(triangle):
    answer = 0
    dx=[1,1]
    dy=[0, 1]
    tlen=len(triangle)
    mylist= []
    for i in range(tlen):
        mylist.append([0]*(i+1))
    
    mylist[0][0]=triangle[0][0]
    for i in range(tlen-1):
        for j in range(i+1):
            mylist[i+dx[0]][j+dy[0]]= max(mylist[i][j]+triangle[i+dx[0]][j+dy[0]], mylist[i+dx[0]][j+dy[0]])
            mylist[i+dx[1]][j+dy[1]]= max(mylist[i][j]+triangle[i+dx[1]][j+dy[1]], mylist[i+dx[1]][j+dy[1]])
            #print("i: ", i, " j: ",j)
            #print(mylist)
    #print(mylist)
    answer=max(mylist[tlen-1])
    #print(answer)
    
    return answer

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])