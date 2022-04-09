import pygame

#시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, white, start_button.center, 60, 5)
    #스크린에다가 흰색으로 동그라미를 그리는데 중심좌표는 start_button의 중심좌표고 반지름은 60, 선 두꼐는 5로 함

#게임 화면 보여주기
def display_game_screen():
    print("Start Game")

#pos 에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True
    
#초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

#시작버튼  
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

#색깔
black = (0, 0, 0)
white = (255, 255, 255)

#게임 시작 여부
start = False

#게임루프 
running = True #게임 실행중?
while running:
    click_pos = None
    #이벤트루프
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트인가?
            running = False #그렇다면 게임 실행 아님
        elif event.type == pygame.MOUSEBUTTONUP: #사용자가 마우스를 클릭했을떄
            click_pos = pygame.mouse.get_pos()
            print(click_pos)
    #화면 전체를 까맣게 채움
    screen.fill(black)
    
    if start:
        display_game_screen() #게임 화면 표시
    else:
        display_start_screen() #스타트 화면 표시
    #사용자가 클릭한 좌표값이 있다면
    if click_pos:
        check_buttons(click_pos)
    
    #화면 업데이트
    pygame.display.update()

            
pygame.quit() #게임 종료