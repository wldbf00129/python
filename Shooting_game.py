import pygame
import sys
pygame.init()
###
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
yellow=(255,255,0)
blue=(0,0,255)
pink=(255,133,215)
orange=(240,155,89)
###




w=480
h=640

pad= pygame.display.set_mode((w,h))# 화면생성
pygame.display.set_caption("Shotting game") #제목 설정

pad.fill((193,208,234))



pygame.draw.line(pad,red,(240,0),(240,640),5)       #선그리기  
pygame.draw.line(pad,red,(0,200),(480,200),5)
pygame.draw.circle(pad,blue,(100,100),50,0)   #원그리기
pygame.draw.circle(pad,blue,(360,100),50,0)


pygame.draw.circle(pad,blue,(100,50),50,0)  
pygame.draw.circle(pad,blue,(360,50),50,0)



pygame.draw.rect(pad,pink,(70,400,330,200),0) #사각형그리기
pygame.draw.polygon(pad,yellow,((100,100),(340,200),(480,200))) #다각형 그리기
pygame.draw.ellipse(pad,orange,(300,300,100,50),0) #타원그리기
pygame.draw.ellipse(pad,orange,(100,300,100,50),0)




pygame.display.update()#화면 업데이트


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
