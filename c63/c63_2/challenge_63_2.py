def e(s,k):
 k=int(k)
 if len(s)<k:return 0
 w=min(set(s),key=s.count)
 if s.count(w)>=k:return len(s)
 return max(e(q,k)for q in s.split(w))
for _ in[i:=input]*int(i()):print(e(*i().split()))