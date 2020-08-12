roomnum=int(input())
people=input().split()
main, sub= input().split()
main=int(main)
sub=int(sub)   
ans=0 
for peop in people:
    #print(ans)
    ans += 1
    if int(peop)<=main:
        continue
    else:
        peop=int(peop)-main
        if peop%sub != 0:
            ans += 1
        ans += peop//sub
print(ans)