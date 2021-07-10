y,g=int,input
for _ in"e"*y(g()):
 t,q,w="false",[],0;x,n=map(y,g().split());a,b=map(y,g().split())
 for i in range(a+2):
  for o,p in enumerate(g()):
   if p=='*':q+=[(i,o)]   
   if p=='A':w=(i,o)
 for z in q:
  if abs(z[0]-w[0])+abs(z[1]-w[1])<=x*n*10:t="true"
 print(t)