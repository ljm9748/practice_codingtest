sangg=[False]*20000000
N= int(input())
sang=input().split()
for i in sang:
    sangg[int(i)+10000000]=True
M= int(input())
find=input().split()
for i in find:
    if sangg[int(i)+10000000]==True:
        print('1', end=' ')
    else:
        print('0', end=' ')
    