def solution(g, f, x):
    curPro = 2
    curTime = g / 2
    while 1:

        nextPro = curPro + f
        nextTime = g/curPro + x/nextPro
        
        if nextTime > curTime :
            break;
        else:
            curPro = nextPro
    
    print(curTime)
    return curTime
    
solution(30, 2, 100)   
    
