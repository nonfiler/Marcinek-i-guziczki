import pygame
from menu import Menu
import board_new
from rules import Rules
from letters import LetterGenerator


button_width = 350
button_height = 80
button_margin = 25
button_start_x = 700
button_start_y = 300

# Inicjalizacja biblioteki Pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ustalanie rozmiarów okna
screen_info = pygame.display.get_desktop_sizes()
WIDTH, HEIGHT = screen_info[0][0], screen_info[0][1]

#? Inicjalizacja okna gry
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrabble")


#? Tworzenie obiektów klas
menu = Menu(window, WIDTH, HEIGHT, BLACK, WHITE)
rules = Rules(window, WIDTH, HEIGHT, BLACK, WHITE)
letters1 = LetterGenerator()
letters2 = LetterGenerator()
class play_state:
    def __init__(self):
        self.current_player = True
        
current_player = play_state()
#? ustawienia liter, graczy

player1_letters = []
player2_letters = []

board = board_new.Board(window, WIDTH, HEIGHT, BLACK, WHITE, player1_letters, player2_letters, current_player)
player2_letters = letters2.generate_letters(7)
player1_letters = letters1.generate_letters(7)

for x in player1_letters:
    x.set_board(board) 
for x in player2_letters:
    x.set_board(board)

for letter in player1_letters:
    letter.make_rect()
for letter in player2_letters:
    letter.make_rect()
    
print("Player1 letters:", player1_letters)
print("Player2 letters:",player2_letters)
play_rect = pygame.Rect(WIDTH // 2 - 75, 250, 150, 50)
rules_rect = pygame.Rect(WIDTH // 2 - 75, 350, 150, 50)
exit_rect = pygame.Rect(WIDTH // 2 - 75, 450, 150, 50)

#? Główna pętla gry
def run_game():
    #? falgi do sterowania funkcjami w grze
    menu_flag = True
    game_flag = False
    rules_screen = False

    global play_rect, rules_rect, exit_rect

    while True:
        #* rysowanie menu
        if menu_flag:
            menu.draw_menu()
        #* rysowanie planszy i rzeczy z nią związanych
        elif game_flag:
            board.print_board()
            if current_player.current_player:
                for letter in player1_letters:
                    letter.draw()
            else:
                for letter in player2_letters:
                    letter.draw()
                    # print(letter.rect.center())
            pygame.display.flip()   
        #* rysowanie zasad 
        elif rules_screen:
            rules.draw_rules_screen()
            
        #* obsługa zdarzeń
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return
            if game_flag:
                for letter in player1_letters:
                    letter.handle_event(event)
                for letter in player2_letters:
                    letter.handle_event(event)
            #* sczytywanie pozycji dla myszki
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                #* ryowanie menu
                if menu_flag:

                    #*obsługa przycisków w menu i ustawianie flag
                    if play_rect.collidepoint(mouse_pos):
                        menu_flag = False
                        game_flag = True   
                    elif rules_rect.collidepoint(mouse_pos):
                        menu_flag = False
                        rules_screen = True
                    elif exit_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        return
                
                elif rules_screen:
                    return_button_rect = pygame.Rect(WIDTH - 200, HEIGHT - 80, 150, 50)
                    if return_button_rect.collidepoint(mouse_pos):
                        rules_screen = False
                        menu_flag = True

                elif game_flag:
                    board.handle_event(event)

run_game()