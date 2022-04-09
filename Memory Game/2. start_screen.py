import pygame

#시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, white, start_button.center, 60, 5)
    #스크린에다가 흰색으로 동그라미를 그리는데 중심좌표는 start_button의 중심좌표고 반지름은 60, 선 두꼐는 5로 함
    
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

#게임루프 
running = True #게임 실행중?
while running:
    #이벤트루프
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트인가?
            running = False #그렇다면 게임 실행 아님
    screen.fill(black)

    #시작화면 표시
    display_start_screen()
    
    #화면 업데이트
    pygame.display.update()

            
pygame.quit() #게임 종료