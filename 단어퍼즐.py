def dfs( ans, ind):
    global answer
    if ind == len(gt):
        #print (min(answer, ans),"dd")
        answer= min(answer, ans)
        return
    elif ind>len(gt):
        return
    else:
        for i in gstrs:
            if i == gt[ind:ind+len(i)]:
                dfs( ans+1, ind+len(i))
        return
        
        
def solution(strs, t):
    global gt, gstrs, answer
    gstrs= strs
    gt=t
    answer=20005
    dfs(0,0)

    if answer==20005:
        answer=-1
    #print(answer)
    return answer
#solution(["ba","an","nan","ban","n"], "banana")
#print(gt,gstrs)