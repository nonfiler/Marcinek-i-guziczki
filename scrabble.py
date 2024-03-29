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
    squares_on_board = []
    words_on_board = []
    scores = {}
    for k, v in {
            "AEIOULNRST": 1,
            "DG": 2,
            "BCMP": 3,
            "FHVWY": 4,
            "K": 5,
            "JX": 8,
            "QZ": 10
        }.items():
        scores.update({x: v for x in k})
        
    while True:
        #* rysowanie menu
        if menu_flag:
            menu.draw_menu()
        #* rysowanie planszy i rzeczy z nią związanych
        elif game_flag:
            board.print_board()
            for letter in squares_on_board:
                letter.draw()
            if current_player.current_player:
                for letter in player1_letters:
                    letter.draw()
            else:
                for letter in player2_letters:
                    letter.draw()
            pygame.display.flip()   
        #* rysowanie zasad 
        elif rules_screen:
            rules.draw_rules_screen()
            
        #* obsługa zdarzeń
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return
            #?obsługa klocków z literami poszczególnych graczy 
            if game_flag:
                if current_player.current_player:
                    for letter in player1_letters:
                        letter.handle_event(event, board, player1_letters, player2_letters)
                else:
                    for letter in player2_letters:
                        letter.handle_event(event, board, player1_letters, player2_letters)
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
                        
                #* sterowanie guziczków
                elif game_flag:
                    match board.handle_event(event):
                        case "Pass":
                            if current_player.current_player:
                                for letter in player1_letters:
                                    letter.rect.center = letter.reset_pos
                            else:
                                for letter in player2_letters:
                                    letter.rect.center = letter.reset_pos
                            current_player.current_player = not current_player.current_player
                        case "Check word":
                            if current_player.current_player:
                                new_letters = []
                                
                                #Jesli literka na planszy i nie ma tam innej literki to ją wpisujemy tymczasowo w to pole i zapisujemy jej indexy
                                for x in range (len(player1_letters)):
                                    if player1_letters[6 - x].check_if_on_board():
                                        index_x = int(player1_letters[6 - x].rect.center[1] / 42)
                                        index_y = int(player1_letters[6 - x].rect.center[0] / 42)
                                        if board.board_logic[index_x][index_y][0] is None:
                                            board.board_logic[index_x][index_y][0] = player1_letters[6 - x].letter
                                            new_letters.append((index_x,index_y))
                                            
                                #Szukamy słów w tablicy i usuwamy je jeśli już były użyte wcześniej
                                founded_words = board.search_words()
                                founded_words = [word for word in founded_words if word not in words_on_board]
                                
                                #Jeśli mamy conajmniej jedno słowo dodajemy literki na planszę na stałe i usuwamy ich koordy z miejsca po prawej
                                #jeśli nie to literki wracają na prawo i usuwamy na zapisanych indexach literki z tablicy
                                if len(founded_words) > 0:
                                    for x in range (len(player1_letters)):
                                        if player1_letters[6 - x].check_if_on_board():
                                            index_x = int(player1_letters[6 - x].rect.center[1] / 42)
                                            index_y = int(player1_letters[6 - x].rect.center[0] / 42)
                                            board.board_logic[index_x][index_y][0] = player1_letters[6 - x].letter
                                            player1_letters[6 - x].reset_pos = player1_letters[6 - x].rect.center
                                            squares_on_board.append(player1_letters.pop(6 - x))
                                            
                                    coords = board.find_word(founded_words[0])
                                    score = 0
                                    if coords[2] == "poziomo":
                                        for y in range(len(founded_words[0])):
                                            if board.board_logic[coords[0]][coords[1]+ y][1] == "empty":
                                                score += scores[board.board_logic[coords[0]][coords[1]+ y][0]]
                                            elif board.board_logic[coords[0]][coords[1]+ y][1] == "2l":
                                                score += (2 * scores[board.board_logic[coords[0]][coords[1]+ y][0]])
                                            elif board.board_logic[coords[0]][coords[1]+ y][1] == "3l":
                                                score += (3 * scores[board.board_logic[coords[0]][coords[1]+ y][0]])
                                            elif board.board_logic[coords[0]][coords[1]+ y][1] == "2w":
                                                score += (2 * len(founded_words[0]))
                                            elif board.board_logic[coords[0]][coords[1]+ y][1] == "3w":
                                                score += (3 * len(founded_words[0]))
                                    else:
                                        for x in range(len(founded_words[0])):
                                            if board.board_logic[coords[0] + x][coords[1]][1] == "empty":
                                                score += scores[board.board_logic[coords[0] + x][coords[1]][0]]
                                            elif board.board_logic[coords[0] + x][coords[1]][1] == "2l":
                                                score += (2 * scores[board.board_logic[coords[0] + x][coords[1]][0]])
                                            elif board.board_logic[coords[0] + x][coords[1]][1] == "3l":
                                                score += (3 * scores[board.board_logic[coords[0] + x][coords[1]][0]])
                                            elif board.board_logic[coords[0] + x][coords[1]][1] == "2w":
                                                score += (2 * len(founded_words[0]))
                                            elif board.board_logic[coords[0] + x][coords[1]][1] == "3w":
                                                score += (3 * len(founded_words[0]))
                                    board.player1_score.score += score
                                        
                                else:
                                    for coords in new_letters:
                                        board.board_logic[coords[0]][coords[1]][0] = None
                                
                                #Generuje brakujące literki
                                missing_squares = 7 - len(player1_letters)
                                list_of_squares = letters1.generate_letters(missing_squares)
                                
                                #Dodaje wygenerowane literki
                                for square in list_of_squares:
                                    player1_letters.append(square)
                                for letter in player1_letters:
                                    letter.set_board(board)
                                    letter.nr = player1_letters.index(letter)
                                    letter.make_rect()
                                    
                            else:
                                new_letters = []
                                for x in range (len(player2_letters)):
                                    if player2_letters[6 - x].check_if_on_board():
                                        index_x = int(player2_letters[6 - x].rect.center[1] / 42)
                                        index_y = int(player2_letters[6 - x].rect.center[0] / 42)
                                        if board.board_logic[index_x][index_y][0] is None:
                                            board.board_logic[index_x][index_y][0] = player2_letters[6 - x].letter
                                            new_letters.append((index_x,index_y))
                                            
                                            
                                founded_words = board.search_words()
                                founded_words = [word for word in founded_words if word not in words_on_board]
                                
                                if len(founded_words) > 0:
                                    for x in range (len(player2_letters)):
                                        if player2_letters[6 - x].check_if_on_board():
                                            index_x = int(player2_letters[6 - x].rect.center[1] / 42)
                                            index_y = int(player2_letters[6 - x].rect.center[0] / 42)
                                            board.board_logic[index_x][index_y][0] = player2_letters[6 - x].letter
                                            player2_letters[6 - x].reset_pos = player2_letters[6 - x].rect.center
                                            squares_on_board.append(player2_letters.pop(6 - x))
                                            
                                    coords = board.find_word(founded_words[0])
                                    score = 0
                                    if coords[2] == "poziomo":
                                        for y in range(len(founded_words[0])):
                                            if board.board_logic[coords[0]][coords[1]+ y][1] == "empty":
                                                score += scores[board.board_logic[coords[0]][coords[1]+ y][0]]
                                            elif board.board_logic[coords[0]][coords[1]+ y][1] == "2l":
                                                score += (2 * scores[board.board_logic[coords[0]][coords[1]+ y][0]])
                                            elif board.board_logic[coords[0]][coords[1]+ y][1] == "3l":
                                                score += (3 * scores[board.board_logic[coords[0]][coords[1]+ y][0]])
                                            elif board.board_logic[coords[0]][coords[1]+ y][1] == "2w":
                                                score += (2 * len(founded_words[0]))
                                            elif board.board_logic[coords[0]][coords[1]+ y][1] == "3w":
                                                score += (3 * len(founded_words[0]))
                                    else:
                                        for x in range(len(founded_words[0])):
                                            if board.board_logic[coords[0] + x][coords[1]][1] == "empty":
                                                score += scores[board.board_logic[coords[0] + x][coords[1]][0]]
                                            elif board.board_logic[coords[0] + x][coords[1]][1] == "2l":
                                                score += (2 * scores[board.board_logic[coords[0] + x][coords[1]][0]])
                                            elif board.board_logic[coords[0] + x][coords[1]][1] == "3l":
                                                score += (3 * scores[board.board_logic[coords[0] + x][coords[1]][0]])
                                            elif board.board_logic[coords[0] + x][coords[1]][1] == "2w":
                                                score += (2 * len(founded_words[0]))
                                            elif board.board_logic[coords[0] + x][coords[1]][1] == "3w":
                                                score += (3 * len(founded_words[0]))
                                    board.player2_score.score += score
                                                
                                missing_squares = 7 - len(player2_letters)
                                list_of_squares = letters1.generate_letters(missing_squares)
                                
                                for square in list_of_squares:
                                    player2_letters.append(square)
                                for letter in player2_letters:
                                    letter.set_board(board)
                                    letter.nr = player2_letters.index(letter)
                                    letter.make_rect()
                            
                            current_player.current_player = not current_player.current_player
      
run_game()