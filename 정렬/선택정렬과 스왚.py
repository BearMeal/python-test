#선택 정렬: 순서없이 나열된 자료들중 기준을 잡고 하나를 골라 정렬한다. 젤작은숫자만 골라 맨앞에거랑 바꾼다.
#아이디어: 숫자를 작은것부터 뽑아서 정렬할 리스트의 값들이랑 비교해서 맨앞거보다 값이 작으면 스왑한다.

array =[7,5,9,0,3,1,6,2,4,8]
#배열의 길이 크기는 10
print(len(array))
for i in range(len(array)):
  min_index =i #가장작은 숫자를 고름 0~9까지 i로
  for j in range(i+1,len(array)):
    if array[min_index] > array[j]:
      min_index =j
  array[i], array[min_index] =array[min_index], array[i] # i와 min_index 스왚

print(array)
