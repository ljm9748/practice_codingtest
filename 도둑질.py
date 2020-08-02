def solution(money):
    answer = 0
    mlen=len(money)
    mylist=[]
    mylist2=[]
    for _ in range(mlen):
        mylist.append([0,0])
        mylist2.append([0,0])
    
    for i in range(1,mlen): #첫집 안감
        mylist[i][0]=mylist[i-1][1]+money[i]
        mylist[i][1]=max(mylist[i-1][0], mylist[i-1][1])
    print(mylist)
    mylist2[1][1]=money[0]
    for i in range(2,mlen):
        mylist2[i][0]=mylist2[i-1][1]+money[i]
        mylist2[i][1]=max(mylist2[i-1][0], mylist[i-1][1])
    print(mylist2)
    answer=max(mylist2[mlen-1][1], mylist[mlen-1][1], mylist[mlen-1][0])
    print(answer)
    
    
    return answer
solution([1,2,3,1])

