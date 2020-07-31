myList=[set([]) for _ in range(9) ]
answer=-1

def makeList(N, now, number): #나눠야하는 수, 자리수
    tmp=0
    for _ in range(now):
        tmp=tmp*10+N
    if tmp == number:
        return now
    myList[now].add(tmp)
    
    
    for i in myList[now-1]:
        if i*N == number:
            return now
        myList[now].add(i*N)
        if N > i:
            if N-i == number:
                return now
            myList[now].add(N-i)
        if i> N:
            if i-N == number:
                return now            
            myList[now].add(i-N)
        if N != 0:
            if int(i/N) == number:
                return now           
            myList[now].add(int(i/N))
        if i != 0:
            if int(N/i) == number:
                return now 
            myList[now].add(int(N/i))
    return -1  
def solution(N, number):
    global answer
    myList[1].add(N)
    if N == number:
        answer=1
        return
    for i in range(2,9):
        answer=makeList(N, i, number)
        print("answer: ", answer)
        if answer != -1:
            break
    for i in range(9):
        print(myList[i])
    print("answer: ", answer)
    
    
    return answer

solution(5, 40)