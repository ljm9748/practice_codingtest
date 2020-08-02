def solution(routes):
    answer = 0
    routes.sort(reverse=True, key=lambda x: x[1])
    while len(routes) > 0:
        cam = routes[-1][1]
        answer += 1
        routes.pop()
        for i in range(len(routes)-1, -1, -1):
    #        print(i)
            if routes[i][0]<= cam:
                del routes[i]
    #    print(routes)   
    #print(answer)
    
    
    return answer
solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])