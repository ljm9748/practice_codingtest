# myList=[set([]) for _ in range(9) ]
# answer=-1

# def makeList(N, now, number): #나눠야하는 수, 자리수
#     tmp=0
#     for _ in range(now):
#         tmp=tmp*10+N
#     if tmp == number:
#         return now
#     myList[now].add(tmp)
    
    
#     for i in myList[now-1]:
#         if i*N == number:
#             return now
#         myList[now].add(i*N)
#         if N > i:
#             if N-i == number:
#                 return now
#             myList[now].add(N-i)
#         if i> N:
#             if i-N == number:
#                 return now            
#             myList[now].add(i-N)
#         if N != 0:
#             if int(i/N) == number:
#                 return now           
#             myList[now].add(int(i/N))
#         if i != 0:
#             if int(N/i) == number:
#                 return now 
#             myList[now].add(int(N/i))
#     return -1  
# def solution(N, number):
#     global answer
#     myList[1].add(N)
#     if N == number:
#         answer=1
#         return
#     for i in range(2,9):
#         answer=makeList(N, i, number)
#         print("answer: ", answer)
#         if answer != -1:
#             break
#     for i in range(9):
#         print(myList[i])
#     print("answer: ", answer)
    
    
#     return answer

# solution(5, 40)
def solution(N, number):
    S = [0, {N}]
    for i in range(2, 9):
        case_set = {int(str(N)*i)} #이 방법 배우기
        for i_half in range(1, i//2+1):  # S[i_half] S[1]
            for x in S[i_half]:
                for y in S[i-i_half]:
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x) # y-x 케이스 추가
                    case_set.add(x*y)
                    if x != 0:
                        case_set.add(y//x)
                    if y != 0:
                        case_set.add(x//y)
        if number in case_set:
            return i
        S.append(case_set)
    return -1


print(solution(2, 11))