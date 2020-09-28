answer=0
def solution(numbers, target):
    global answer
    dfs(0+numbers[0], 0, target, numbers)
    dfs(0-numbers[0], 0, target, numbers)
    print(answer)
    return answer

def dfs(now, cnt, target, numbers):
    global answer
    
    if cnt==len(numbers)-1:
        if now==target:
            answer += 1
            return
        else:
            return
    else:
        print(now+numbers[cnt+1],cnt+1,target, numbers)
        print(now-numbers[cnt+1],cnt+1,target, numbers)
        dfs(now+numbers[cnt+1],cnt+1,target, numbers)
        dfs(now-numbers[cnt+1],cnt+1,target, numbers)

solution([1, 1, 1, 1, 1], 3)