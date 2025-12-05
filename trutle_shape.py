import turtle as t
import random
"""
#다각형 그리기
n=int(input("몇 각형을 그릴까요?"))
for i in range(n):
    t.forward(100)
    t.left(360/n)

#다각형 그리기 입력한 각형-> 삼각형까지 그리기
n=int(input("몇 각형부터  그릴까요?"))
for i in range(n,2,-1):
    for j in range(i):
    t.forward(i)
    t.left(360/i)
    
#다각형 그리고 색칠하기
color=["ren","gerrn","purple","blue","brown","yellow","navy","gray","pink","orange"]
n=int(input("몇 각형부터  그릴까요?"))
t.shape("turtle")
t.speed(1)#빠르기 순서 0 10 9 8 7 6 5 4 3 2 1

for i in range(n,2,-1):
    t.color(color[i])
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()

#다각형 그리고 랜덤 색칠하기
color=["ren","gerrn","purple","blue","brown","yellow","navy","gray","pink","orange"]
n=int(input("몇 각형부터  그릴까요?"))
t.shape("turtle")
t.speed(1)#빠르기 순서 0 10 9 8 7 6 5 4 3 2 1

for i in range(n,2,-1):
    #t.color(random.choice(color))### 색 랜덤 으로 고르기
    random.shuffle(color)
    t.color(color[i])
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()


color=["red","green","purple","blue","brown","yellow","navy","gray","pink","orange"]
n=int(input("몇 각형부터  그릴까요?"))
t.shape("turtle")
t.speed(1)#빠르기 순서 0 10 9 8 7 6 5 4 3 2 1

for i in range(n,2,-1):
    now_color=random.choice(color)
    print(now_color)#
    t.color(now_color)
    color.remove(now_color)
    print(color)#
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()
    """
# 세가지 색깔이 계속 중복되어서 칠해지록
# 각형제한 없게
color=["red","yellow"]
count=0
n=int(input("몇 각형부터  그릴까요?"))
for i in range(n,2,-1):
    t.color(color[count])
    count=count+1
    if count==2:
        count=0
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()













