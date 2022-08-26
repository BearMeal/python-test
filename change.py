#거스름돈을 줄 때 최소의 동전갯수
print('거스름돈을 입력하시오 :',end=" ")
n = int(input())

print(f'{n}원이 입력되었습니다.')
count=0

if str(n)[-1] != '0':
    print('셀 수 없는 단위입니다.')
    quit()
#동전의 종류는 500,100,50,10
a= n//500
b= n%500
c= b//100
d= b%100
e= d//50
f= d%50
g= f//10


print(f'최소동전 갯수는{count+a+c+e+g}개 입니다.')