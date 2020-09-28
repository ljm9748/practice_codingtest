from queue import Queue

def solution(numbers, target):
    answer = 0
    mq=[0]
    #mq.put(0) 
    now=1   
    for i in range(len(numbers)):
        for _ in range(now):
            if i==len(numbers)-1:
                tmp=mq.pop(0)
                if tmp+numbers[i]==target: 
                    answer+=1
                if tmp-numbers[i]==target: 
                    answer+=1
                mq.append(tmp+numbers[i])
                mq.append(tmp-numbers[i])
            else:
                tmp=mq.pop(0)
                mq.append(tmp+numbers[i])
                mq.append(tmp-numbers[i])
        now *= 2  
        #print(mq)
    #print(answer)
    return answer
solution([1, 1, 1, 1, 1],3)