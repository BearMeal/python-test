,#넓이 n
n= int(input())

print(n)#공간의 크기확인
#원하는 이동을 넣을 때 마다 결과 출력
while True:
  #시작위치 설정
  x,y = 1,1
  #원하는 이동 입력 L,R,U,D
  for _ in range(3):
    plans =input().split()
    
    #원하는 이동을 저장된 리스트에서 확인
    move_types=['L','R','U','D']
    #이동할량
    dx= [0,0,-1,1]
    dy = [-1,1,0,0]

    for plan in plans:
      for i in range(len(move_types)):
        if plan == move_types[i]:
          nx= x+dx[i]
          ny=y+dy[i]

        else:
          print('이동불가한 값입니다.')
          continue
      if ny<0 or nx<0 or nx>n or ny>n:
        print('범위를 벗어났습니다.')
        continue
      x,y= nx,ny
      print(x,y)