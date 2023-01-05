import pygame

pygame.init()

#화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경이미지 불러오기
background = pygame.image.load("C:/SHproject/pygame_basic/background.png")
#화면 타이틀 설정
pygame.display.set_caption("Nado Game")

#이벤트 루프
running = True #게임이 진행중인가
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False
    screen.blit(background, (0,0)) # 배경 그리기
    pygame.display.update() # 게임화면을 다시 그리기!
    # screen.fill((0,0,255))
# PYGAME 종료
pygame.quit()

