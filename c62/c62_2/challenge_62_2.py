for _ in range(int(input())):
    a=input();b=input()
    count=0
    ans="yes"
    for i in range(len(b)):
        if count>len(a)-1:
            ans="no";break
        if b[i]==a[count]:
            if count==len(a)-1:
                continue
            count+=1;continue
        if b[i]!=a[count-1]:ans="no";break
    print(ans)
        
        