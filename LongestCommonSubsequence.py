def LCS(s1,s2,n1,n2):
  if n1==0 or n2==0:
    return ""
  elif s1[0]==s2[0]:
    return s1[0]+LCS(s1[1:],s2[1:],n1-1,n2-1)
  else:
    v1=LCS(s1[1:],s2,n1-1,n2)
    v2=LCS(s1,s2[1:],n1,n2-1)
    return v1 if len(v1)>len(v2) else v2

s1='ADACA'
s2='ACDA'
print(LCS(s1,s2,len(s1),len(s2)))
