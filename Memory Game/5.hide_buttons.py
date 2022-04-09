import pygame
from random import *
#레벨에 맞게 난이도 조절
def setup(level):
    
    global display_time
    
    display_time = 5 - level // 3
    display_time = max(1, display_time)
    
    number_count = level // 3 + 5
    number_count = min(number_count, 20)
    
    #실제 화면에 그리드 만들어서 배치
    shuffle_grid(number_count)

#제일 중요한 숫자 섞기 
def shuffle_grid(number_count):
    rows = 5
    columns = 9
    
    cell_size = 130
    button_size = 110
    screen_left_margin = 55
    screen_top_margin = 20
    
    grid = [[0 for col in range(columns)] for row in range(rows)]
    
    number = 1 #시작넘버
    
    while number <= number_count:
        row_i = randrange(0, rows) # 행에 해당하는 인덱스 추출
        col_i = randrange(0, columns) # 열에 해당하는 인덱스 추출
        
        if grid[row_i][col_i] == 0:
            grid[row_i][col_i] = number
            number += 1
            
            #정해진 셀 인덱스를 가지고 셀 버튼 구현
            center_x = screen_left_margin + col_i * cell_size + cell_size / 2
            center_y = screen_top_margin + row_i * cell_size + cell_size / 2
            
            #버튼 그리기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)
            
            number_buttons.append(button)
        

#시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, white, start_button.center, 60, 5)
    #스크린에다가 흰색으로 동그라미를 그리는데 중심좌표는 start_button의 중심좌표고 반지름은 60, 선 두꼐는 5로 함

#게임 화면 보여주기
def display_game_screen():
    global hidden
    
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time > display_time:
            hidden = True
            
    for i, rect in enumerate(number_buttons, start = 1):
        if hidden:
            pygame.draw.rect(screen, white, rect)
        else:
        #숫자 텍스트
            cell_text = game_font.render(str(i), True, white)
            text_rect = cell_text.get_rect(center = rect.center)
            screen.blit(cell_text, text_rect)

#pos 에 해당하는 버튼 확인
def check_buttons(pos):
    global start, start_ticks
    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks() #타이머 시작
        
#눌러야 할 버튼 잘 눌렀는지 확인
def check_number_buttons(pos):
    global hidden
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                print("correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                print("wrong")
            break
    
#초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120) #폰트 정의

#시작버튼  
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

#색깔
black = (0, 0, 0)
white = (255, 255, 255)
gray = (50, 50, 50)
#넘버 버튼 리스트
number_buttons = []
display_time = None #숫자 보여주는 시간
start_ticks = None #시간 계산

#게임 시작 여부
start = False

#숫자 숨김 여부
hidden = False

#게임 시작 전에 게임 설정 함수 수행
setup(1)

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