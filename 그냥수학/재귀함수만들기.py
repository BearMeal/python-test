#재귀 함수는 스택과 구조가 같다.
#재귀함수를 이용해 팩토리얼을 만들어 볼수있다.

while True:
  a =int(input())
  b=a+1
  def fac(a):
    if a==1:
      c=1
      print(f"{a} =",end=" ")
      for i in range(1,b):
        c*=i
      print(c) 
      return
    print(f"{a}X", end="")

    a-=1
    fac(a)

  fac(a)
