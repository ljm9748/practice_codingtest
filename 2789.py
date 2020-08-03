camb=list("CAMBRIDGE")
ans=input()
ans=list(ans)
for i in ans:
    if i not in camb:
        print(i, end='')
