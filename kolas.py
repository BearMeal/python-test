import matplotlib.pyplot as plt

print('안녕하세요. 콜라스의 추측 자동 계산기입니다. 원하는 숫자를 입력해주십시오.')
print("원하는 숫자 :",end=" ")
x=int(input())

a=[]
a.append(x)
while True:
    if x%2 == 1:
        print('홀수입니다. 곱하기 3 합니다')
        x= x*3
        if x%2 ==1 :
            print('다시 홀수입니다. 더하기 1 합니다')
            x+=1
            print(x)
            a.append(x)
            if x==1:
                break
        
    if x%2 == 0:
        print('짝수입니다. 나누겠습니다.')
        x/=2
        print(x)
        a.append(x)
        if x==1:
            break
            
plt.plot(a,'.')
plt.xlabel('횟수')
plt.show()