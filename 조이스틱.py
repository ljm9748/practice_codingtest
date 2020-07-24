def solution(name):
    answer = 0
    slen=len(name)
    mylist=[False for _ in range(slen)]
    findcnt=0
    for i in range(slen):
        if name[i]=='A':
            mylist[i]=True
            findcnt +=1
    #print("answer1: ", answer)
    now=0
    #print(mylist)
    if mylist[0]==False:
        mylist[now]=True
        tmp= ord(name[now])-ord('A')
    #    print("??", tmp) 
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
            if(mylist[tmp1%slen]==True):
                tmp1 +=1
            else: 
                play=False
                findcnt +=1
                answer += tmp1-now
                now=tmp1%slen
                break
            if(mylist[tmp2+slen]==True):
                tmp2 -=1
                
            else: 
                play=False
    #            print(tmp2)
                findcnt +=1
                answer += now-tmp2
                now=slen+tmp2
                break
        
        mylist[now]=True
        tmp= ord(name[now])-ord('A')
    #    print("??", tmp) 
        if tmp<13:
            answer +=tmp
        else:
            answer+=(26-tmp)
        

            

#    print (mylist)
#    print("answer: ", answer)
    return answer

solution("JEROEN")