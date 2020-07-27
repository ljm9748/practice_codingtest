def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    check=[False for _ in range(n)]
    check[0]=True
    #clen=len(costs)
    while False in check:
        for i in range(len(costs)):
            if (check[costs[i][0]] == False and check[costs[i][1]] == True) or (check[costs[i][0]] == True and check[costs[i][1]] == False):
                answer += costs[i][-1]
                check[costs[i][0]]=True
                check[costs[i][1]]=True
                del costs[i]
                break
            
    
    
    print(costs)
    print(check)
    print(answer)
    return answer

solution(5, [[0,1,1],[1,2,2],[3,2,50],[3,4,1]])