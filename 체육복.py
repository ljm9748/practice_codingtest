def solution(n, lost, reserve):
    answer = n
    mlist=[1 for _ in range(n+2)]
    mlist[0]=0
    mlist[-1]=0
    for reservep in reserve:
        mlist[reservep] += 1
    for lostp in lost:
        mlist[lostp] -=1
    for i in range(n):
        if mlist[i+1] ==0:
            if mlist[i]==2:
                mlist[i]=1
            elif mlist[i+2]==2:
                mlist[i+2]=1
            else:
                answer -= 1
        
    
    #print(answer)    
    return answer

solution(8,[4,5],[5,6])
# 초기화 하지 않고 찾는 경우 여분가져온 친구가 도둑맞았는데 그걸 나중에 확인해서 먼저 앞 친구한테 빼앗겨 버리는 상황이 생김