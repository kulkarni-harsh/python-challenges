for _ in [z:=input]*int(z()):a=z();print(*[a[i]*int(a[i-1])for i in range(1,len(a),2)],sep='')
