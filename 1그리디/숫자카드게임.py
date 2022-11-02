n,m = map(int,input().split())

result= 0

#한줄씩 입력받기
for i in range(n):
  data= list(map(int,input().split()))
  #줄에서 가장 적은수 찾기 
  min_value = min(data)
  #가장 작은 수들 중에서 가장 큰수 찾기
  result=max(result,min_value) #두개가 들어왔을때 큰수를 반환한다.

print(result)