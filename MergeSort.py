def mergesort(lst):
  n = len(lst)
  if(n==1):
    return lst
  r = mergesort(lst[:n//2])
  l = mergesort(lst[n//2:])
  li=0
  ri=0
  m=[]
  while(len(l) > ri and len(r) > li):
    if(l[ri] > r[li]):
      m.append(r[li])
      li+=1
    else:
      m.append(l[ri])
      ri+=1
  m.extend(l[ri:])
  m.extend(r[li:])
  return m

l=[6,5,3,2,8,9]
print(mergesort(l))
