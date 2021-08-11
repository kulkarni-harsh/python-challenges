for _ in[i:=input]*int(i()):z=i();b,c='20','02';print(bool(len(z)>3 and[[0,[z[-1:-4:-1]=='0'+b,[z[-1:-3:-1]==c,z[-1]=='0'][z[2]=='2']][z[:2]==b]][z[0]=='2'],1][z[:4]==b*2 or z[-1:-5:-1]==c*2]))

#PythonAddict
#for i in[i:=input]*int(i()):n=i();m="2020";print(any([n.startswith(m[:j])and n.endswith(m[j:])for j in range(5)])and len(n)>4or n==m)

#Rick
#for I in[I:=input]*int(I()):K=I();L=len(K);print(any('2020'==K[:4-l]+K[L-l:]for l in range(5))and 3<L)