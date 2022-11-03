import matplotlib.pyplot as plt

t=[i for i in range(1,101)]

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