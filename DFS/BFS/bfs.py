from collections import deque
st= int(input())
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

visited=[False]*9

def bfs(graph,st,visited):
  visited[st]=True
  queue=deque([st])
  while queue:
    v= queue.popleft()
    print(v,end=" ")
    for i in graph[v]:
      if visited[i]==False:
        visited[i]=True
        queue.append(i)

bfs(graph,st,visited)