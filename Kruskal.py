def find(i,parent):
  if parent[i] == i:
    return i
  else:
    parent[i] = find(parent[i],parent)
    return parent[i]

def union(x,y,rank,parent):
  u = find(x,parent)
  v = find(y,parent)
  if rank[u]<rank[v]:
    parent[u] = v
  elif rank[u]>rank[v]:
    parent[v] = u
  else:
    parent[v] = u
    rank[u] +=1

def kruskal(graph):
  n = len(graph)
  arr = []
  for  i in range(n):
    for j in range(n):
      if graph[i][j]!=0:
        arr.append([i,j,graph[i][j]])

  arr.sort(key = lambda x:x[2])
  rank=[0 for i in range(n)]
  parent = [i for i in range(n)]

  mst=0
  for edge in arr:
    x,y,w = edge
    u = find(x,parent)
    v = find(y,parent)

    if(u!=v):
      mst+=w
      union(u,v,rank,parent)
  return mst
  
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
print(kruskal(graph))
