for _ in[z:=input]*int(z()):
 a=[];n,f=z().split(' || ')
 for i in range(int(n)):
  p=1;c,v=z().split(': ')
  for q,w in zip(f.split(', '),c.split(', ')):
   if q!=w and q!='?':p=0
  if p:a+=[v]
 print(', '.join(a))
