def are_brackets_balanced(s):
  stack=[]
  for ch in s:
    if ch=='(':
      stack.append(ch)
    else:
      if stack and stack[-1]=='(' and ch==')':
        stack.pop()
      else:
        return False
  return not stack

def balance(s,i=0,sk=0):
  if are_brackets_balanced(s):
    return sk,s
  if len(s)<=i:
    return 999,s
  dv=s[:i]+s[i+1:]
  lk=balance(dv,i,sk+1)
  fk=balance(s,i+1,sk)
  if(lk[0]<fk[0]):
    return lk
  else:
    return fk

s='()())(())))'
print(balance(s))
