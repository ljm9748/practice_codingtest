def solution(s):
    answer = 0
    stack=[]
    stack.append(s[0])
    for i in range(1, len(s)):
        if len(stack)>0:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
        #print(stack)
        
    if len(stack)==0:
        answer=1
    #print(answer)
    return answer

solution('baabaa')