n=str.split
for _ in[z:=input]*int(z()):a,b=map(int,n(z()));x=[n(z())for i in range(a)];s=set();[s.add(((*x[i][j:j+2],),(*x[i+1][j:j+2],)))for j in range(b-1)for i in range(a-1)];print(len(s))