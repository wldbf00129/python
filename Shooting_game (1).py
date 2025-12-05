#배경 그림 넣기 
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

####배경화면 캐릭터 넣기 ####
bg=pygame.image.load("images/background.jpg")#상대적
pad.blit(bg,(0,0))
p=pygame.image.load("images/ironman.png")
px= w /2-40/2
py=h -45
pad.blit(p,(px,py))



pygame.display.update()#화면 업데이트


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()






