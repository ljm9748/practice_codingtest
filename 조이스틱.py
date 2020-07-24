def solution(name):
    answer = 0
    name=list(name)
    slen=len(name)
    findcnt=0
    now=0
    #print(mylist)
    for i in range(slen):
        if name[i]=='A':
            findcnt+=1
    
    if name[now]!='A':
        tmp= ord(name[now])-ord('A')
        if tmp<13:
            answer +=tmp
        else:
            answer+=(26-tmp)
        findcnt+=1

    while(findcnt<slen):
        #print("answer: ", answer, "now: ", now)
        #print(mylist)
        play=True
        tmp1= now+1
        tmp2= now-1
        while play:
            if(name[tmp1%slen]=='A'):
                tmp1 +=1
            else: 
                play=False
                findcnt +=1
                answer += tmp1-now
                now=tmp1%slen
                break
            if(name[tmp2+slen]=='A'):
                tmp2 -=1
                
            else: 
                play=False
    #            print(tmp2)
                findcnt +=1
                answer += now-tmp2
                now=slen+tmp2
                break
        
        tmp= ord(name[now])-ord('A')
        name[now]='A'
    #    print("??", tmp) 
        if tmp<13:
            answer +=tmp
        else:
            answer+=(26-tmp)
        

            

#    print (mylist)
    print("answer: ", answer)
    return answer

solution("JEROEN")