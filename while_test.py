#제어문 선택문 반복문
#반복문 for,range 문자열 리스트 변수

"""
i=1
while i<=5:
    print(i,"안녕하세요")
    i=i+1
print("끝")



for i range(1,6):
    print(i,"안녕하세요")
print("끝")

i=1
sum=0
while i<=10:
    sum+=i
    i+=1
print("1부터 10까지의합:",sum)

#무한반복

while True:
    jumsu=int(input("희망영어 점수를 입력하세요(점수범위:0~100점):"))
    if jumsu>0 and jumsu<=100:
        break
print("너는 영어시험에서",jumsu,"점을 받을거야")

while True:
    i= int(input("수 하나 입력하세요.(종료시4입력):"))
    if i ==4:
        break
    else:
        print("당신이 입력한 수는",i,"입니다")
"""
fruit=["사과","용과","포도","망고"]
for i in fruit:
    print(i)

i=0
while i<len(fruit):
    print(fruit[i])
    i=+1














              
