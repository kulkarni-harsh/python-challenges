#1 case doesnt work 
for _ in range(int(input())):
  s,n=input().split()
  n=int(n)
  ans=0
  array=[0]
  count=0
  for i in s:
    if i.isalpha():
      array+=[array[-1]+1]
    else:
      array+=[array[-1]*int(i)]
  array=array[1:]
  ans=n-1
  for i in array[::-1]:
    if(n%i==0):
      ans=i;break
    n=n%i
  if ans>0:ans-=1
  while(ans>len(array)-1 or s[ans].isdigit()  ):
    ans-=1
  print(s[ans])



