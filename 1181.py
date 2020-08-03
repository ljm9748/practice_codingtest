N=int(input())
mlist=set([])
for _ in range(N):
    tmp=input()
    mlist.add(tmp)

mlist=sorted(mlist, key= lambda x: (len(x),x))
for i in mlist:
    print(i)