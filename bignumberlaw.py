#어떤 배열에서 큰 수를 만드는 누군가의 법칙

n, m, k= map(int,input().split())

data=list(map(int,input().split()))
data.sort()

bn=0

while True:
    for a in range(k):
        if m==0 :
            break
        bn+= data[-1]
        m += -1
    
    if m==0 :
        break
    bn += data[-2]
    m+= -1

print(bn)
    
        
        
        
