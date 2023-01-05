import pygame

pygame.init()

#화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()

# 배경이미지 불러오기
background = pygame.image.load("C:/SHproject/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/SHproject/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

#이동속도
character_speed = 0.6

#이벤트 루프
running = True #게임이 진행중인가
while running:
    dt = clock.tick(60) #게임 화면의 초당 프레임 수를 설정



    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height



    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기!
    # screen.fill((0,0,255))
# PYGAME 종료
pygame.quit()