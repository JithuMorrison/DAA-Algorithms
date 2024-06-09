def subset_sum(s,v,n,f=[],sum=0,i=0):
  if i>n-1:
    if sum==v:
      final.append(f)
      return True
    return False
  if sum == v:
    final.append(f)
    return True
  st = subset_sum(s,v,n,f+[s[i]],sum+s[i],i+1)
  vt = subset_sum(s,v,n,f,sum,i+1)
  return st or vt
final=[]
s=[1,4,3,5]
v=9
print(subset_sum(s,v,len(s)))
print(final)
