import matplotlib.pyplot as plt

print("안녕하세요.콜라스의 추측게산기 최대값 그래프입니다. 원하는 n~k 범위의 값을 넣으면 최대 높이들을 볼 수 있습니다.")
print('원하는 범위 : '); n,k=map(int,input().split())

t=[i for i in range(n,k+1)]

a=[]
a.append(x) 
for x in t:
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
                print('콜라츠의 추측이 맞습니다.')
                break

            
plt.plot(a,'-')
plt.xlabel('account')
plt.ylabel('Number')
plt.show()