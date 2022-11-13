#상하좌우
n= int(input()) #2차원 맵 크기

while True:
  x,y=0,0 #0,0에서 시작 1로 해도됨

  plans = input().split()

  # LRUD에 따른 이동방향
  dx = [0,0,-1,1]
  dy = [-1,1,0,0]
  move_types = ['L','R','U','D']

  #이동계획을 하나씩 확인
  for plan in plans:
    #이동후 좌표 구하기
    for i in range(len(move_types)):
      if plan == move_types[i]:
        nx= x+dx[i]
        ny = y+dy[i]
    #공간을 벗어나는 경우 무시
    if nx<0 or ny<0 or nx>n or ny>n:
      continue #무시하고 다음명령 수행
    #이동수행완료
    x,y = nx,ny

  print(x,y)

  # 하나넣고 하나이동하는식으로 만들어 보기
