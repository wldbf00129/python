#제어문 반복문for-문자열 리스트 변수range
#구구단 찍기
"""
print("구구단 2 단 출력")
for i in range(1,10):#i 1~9
    print(f"2*{i}={2*i}")

print("구구단 8 단 출력")
for i in range(1,10):#i 1~9
    print(f"8*{i}={8*i}")

#구구단4단 홀수만 찍기 4*1 4*3 4*5 ..4*9
print("구구단4 단홀수 출력")
for i in range(1,10,2):#i 1~9
    print(f"4*{i}={4*i}")    


print("구구단 2 단 출력")
for i in range(1,10):#i 1~9
    print(f"2*{i}={2*i}",end="")

#중복 for
for i in range(1,6):
    #print("i값은",i
    for j in range(1,6): #j 1 2 3 4 5 
        print(j)
  
#구구단 2~9단 찍기
for i in range(2,10):#단 2 3 4 5 6 7 8 9
    for j in range(1,10):
        print(f"{i}*{j}={i*j:>2}",end="")
    print() #다음줄로 내려주는 효과
#print 포매팅 정렬

name="백지율"

print(f"{name:<10}")#왼쪽 정렬
print(f"{name:^10}")#가운데 정렬
print(f"{name:>10}")#오른쪽정렬

for i in range(1,10):
    print()
    for j in range(2,10):
        print(f"{j:>2}*{i:>2}={i*j:>2}",end="")

#반복 별찍기

for i in range(1,6,):
    print("★"*i)

for i in range(5,0,-1):
    print("★"*i)
    
for i in range(5):
    for j in range(0,i+1):
        print("★",end="")
    print()
"""
for i in range(10):
    print(f"{"★"*i:^10}")

    














