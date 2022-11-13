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

#0번리스트는 안쓴다.1번부터 8번 리스트 사용
#방문한 노드를 출력한다.
#방문하지 않은 리스트를 확인해서 방문하도록한다

#방문한 리스트 visited, 시작노드는 1
#각 노드가 방문된 자료형을 준비
n=int(input())
visited =[False]*9
visited[n]=True
print(visited)
print(n,end=" ")
# for i in graph[n]:
#   if visited[i]==False :
#     visited[i]=True
#     print(i,end=" ")
#     for j in graph[i]:
#       if visited[j] == False:
#         visited[j] = True
#         print(j,end=" ")
#         ##유한한 DFS

# print(visited)

#n=1

while True:
  for i in graph[n]:
    if visited[i]==False:
      visited[i]=True
      print(i,end=" ")
      n=n+1
      #다음 n이 i 즉 인접한 노드로 탐색해서 dfs이다다

print(visited)
