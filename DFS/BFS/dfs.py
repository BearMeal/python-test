 #DFS
 
visited =[False]*9
print(visited)
#v is first vertex
def dfs(graph, v,visited):
  visited[v]=True
  #지나간노드를 프린트
  print(v,end=" ")
  for i in graph[v]:
    if visited[i]==False:
      dfs(graph,i,visited)

 
graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]


dfs(graph, 1, visited)