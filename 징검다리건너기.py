def solution(stones, k):
    answer = 0
    #print(stones)
    slen=len(stones)
    for i in range(slen):
        if k<=i:
            stones[i]=min(stones[i], max(stones[i-k:i]))
            #print(stones)
    answer=max(stones[slen-k:slen])
    #print(answer)
    return answer
solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)