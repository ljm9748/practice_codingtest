n=int(input())#판크기
pan=[]
apple=[]
time=0
way=0
snake=[]
dy=[0, 1, 0, -1]
dx=[1, 0, -1, 0]
for i in range(n):
    pan.append([0]*n)   
k=int(input())#사과개수
for _ in range(k):
    y,x=map(int, input().split()) #여기서 맵???
    pan[y-1][x-1]=2
t=int(input())#방향개수
for _ in range(t):
    c, x=  input().split()
    c= int(c)
    apple.append([c,x])
play=True
snake.append([0,0])
pan[0][0]=4#뱀표시

while play:
    time +=1
    newy=snake[-1][0]+dy[way]
    newx=snake[-1][1]+dx[way]
    if newx>=0 and newy>=0 and newx<n and newy<n:
        if pan[newy][newx] == 4:#몸과 만남
            play=False
        elif pan[newy][newx] == 2:
            snake.append([newy,newx])
            pan[newy][newx] = 4
        else:
            snake.append([newy,newx])
            pan[newy][newx] = 4
            pan[snake[0][0]][snake[0][1]]=0
            del snake[0]
    
    else:#범위밖
        play=False
    if len(apple)>0:
        if time==apple[0][0]:
            if apple[0][1]=='D': way=(way+1)%4
            else: way= (way+3)%4
            del apple[0]
    #print(snake)
print(time)   



