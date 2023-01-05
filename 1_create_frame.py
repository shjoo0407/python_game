import pygame

pygame.init()

#화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")

#이벤트 루프
running = True #게임이 진행중인가
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False

# PYGAME 종료
pygame.quit()
