def minval(key,mst,graph,n):
  min = 9999
  min_index = -1
  for i in range(n):
    if key[i] < min and mst[i] == False:
      min = key[i]
      min_index = i
  return min_index

def prims(graph,n):
  key = [999] * n
  parent = [None] * n
  mst = [False] * n
  key[0] = 0
  parent[0] = -1
  for i in range(n):
    u = minval(key,mst,graph,n)
    mst[u] = True
    for v in range(n):
      if key[v] > graph[u][v] and graph[u][v] > 0 and mst[v] == False:
        key[v] = graph[u][v]
        parent[v] = u
  for i in range(1,n):
    print(parent[i],i,graph[i][parent[i]])

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
prims(graph,5)
