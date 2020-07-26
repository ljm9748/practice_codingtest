def solution(people, limit):
    answer = 0
    front=0
    back=len(people)-1
    
    people.sort()

    while front < back:
        if people[front]+people[back]>limit:
            answer +=1
            back -=1
        else:
            answer +=1
            front += 1
            back -=1

    if front == back:
        answer +=1
    
    print(people)
    print(answer)
    return answer

solution([10, 70, 50, 80, 50, 60, 70, 90, 20, 30], 100)