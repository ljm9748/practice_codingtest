def solution(number, k):
    answer = ''
    #number=list(number)
    #nlen=len(number)
    intList = [int(x) for x in number]
    ansList=[]
    fromnum=0
    for i in range(len(number)-k):
        maxnum=0
        #if(i+k+1 < nlen):
        #     tonum= i+k+1
        # else: tonum=nlen
        tonum=min(i+k+1, len(number))
        for j in range (fromnum, tonum):
            if maxnum < intList[j]:
                fromnum=j+1
                maxnum=intList[j]
        ansList.append(str(maxnum))
            
    
    
    print(''.join(ansList))
    
    
    return answer

solution("87654321",3)