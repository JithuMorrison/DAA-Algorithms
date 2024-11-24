def sum_subset(s,v,n,sum=0,i=0):
  if i>n-1:
    return sum==v
  if sum == v:
    return True
  st = sum_subset(s,v,n,sum+s[i],i+1)
  vt = sum_subset(s,v,n,sum,i+1)
  return st or vt
s=[1,4,3,5]
v=9
print(sum_subset(s,v,len(s)))
