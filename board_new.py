import pygame
from buttons_on_board import GameControls
import enchant

BOARD_SIZE = 15
BOARD_POS_X = 50
BOARD_POS_Y = 50
BOARD_COLOR = (200, 200, 200)
TILE_COLOR = (255, 255, 255)
TILE_BORDER_COLOR = (0, 0, 0)

# Ustawienia kwadratu z literką
SQUARE_SIZE = 40
SQUARE_START_POS_X = 600
SQUARE_START_POS_Y = 50
SQUARE_COLOR = (255, 204, 102)
SQUARE_RESET_POS_X = 300
SQUARE_RESET_POS_Y = 300

class Board:
    def __init__(self, window, width, height, black, white, p1_let: list, p2_let: list, c_player):
        self.window = window
        self.width = width
        self.height = height
        self.WHITE = white
        self.BLACK = black
        self.player1_letters = p1_let
        self.player2_letters = p2_let       
        self.current_player = c_player
        self.player1_score = Score("Player 1")
        self.player2_score = Score("Player 2")

        self.game_controls = GameControls()
        self.game_controls.set_center(x=self.width - 155, y=self.height - 170)
        self.concede = Concede()
        self.concede.set_center(1000, 450)

        self.game_controls.add_button("Pass", x=self.width - 155, y=self.height - 295)
        self.game_controls.add_button("Check word", x=self.width - 155, y=self.height - 210)
        self.game_controls.add_button("Change letter", x=self.width - 155, y=self.height - 125)
        self.game_controls.add_button("Commence defeat", x=self.width - 155, y=self.height - 40)

        self.board_logic = [
            [[None, "3w"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2w"], [None, "3w"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "3w"]],
            [[None, "empty"], [None, "2w"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2w"], [None, "empty"]],
            [[None, "empty"], [None, "empty"], [None, "2w"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "2w"], [None, "empty"], [None, "empty"], [None, "empty"]],
            [[None, "2l"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "2l"]],
            [[None, "empty"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3w"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3w"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "empty"]],
            [[None, "empty"], [None, "3l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3l"], [None, "empty"]],
            [[None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2w"], [None, "empty"], [None, "2w"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"]],
            [[None, "2w"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "2w"]],
            [[None, "3w"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2w"], [None, "empty"], [None, "2w"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "3w"]],
            [[None, "empty"], [None, "3l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3l"], [None, "empty"]],
            [[None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2w"], [None, "empty"], [None, "2w"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"]],
            [[None, "empty"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3w"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3w"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "empty"]],
            [[None, "2l"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "2l"]],
            [[None, "empty"], [None, "empty"], [None, "2w"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "2w"], [None, "empty"], [None, "empty"], [None, "empty"]],
            [[None, "empty"], [None, "2w"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "3l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2w"], [None, "empty"]],
            [[None, "3w"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "empty"], [None, "2w"], [None, "3w"], [None, "empty"], [None, "empty"], [None, "2l"], [None, "empty"], [None, "empty"], [None, "3w"]]
        ]
        self.bonus_colors = {
            "2w": (255, 213, 0),   # Żółty
            "3w": (255, 96, 0),    # Czerwony
            "2l": (0, 186, 255),   # Niebieski
            "3l": (0, 98, 255)     # Ciemnoniebieski
        }

    def print_board(self):
        tile_size = 40  # Size of each tile on the board
        margin = 2  # Margin between tiles

        self.window.fill(self.WHITE)
        
        # Iterate over the board logic and draw each tile
        for row in range(len(self.board_logic)):
            for col in range(len(self.board_logic[row])):
                tile_x = col * (tile_size + margin)
                tile_y = row * (tile_size + margin)
                
                # Get the tile value and color
                tile_value = self.board_logic[row][col][1]
                tile_color = self.bonus_colors.get(tile_value, self.WHITE)
                
                # Draw the tile with margin
                pygame.draw.rect(self.window, self.BLACK, (tile_x, tile_y, tile_size, tile_size))
                pygame.draw.rect(self.window, tile_color, (tile_x + margin, tile_y + margin, tile_size - 2 * margin, tile_size - 2 * margin))

        self.game_controls.surface.fill((0, 0, 0))

        self.game_controls.draw(self.window)

        for button in self.game_controls.buttons:
            button.draw(self.window)
        self.player1_score.draw_score(self.window, (830, 120), self.current_player.current_player)
        self.player2_score.draw_score(self.window, (1040, 120), not self.current_player.current_player)


    def handle_event(self, event):
        for button in self.game_controls.buttons:
            string = button.handle_event(event, self.concede, self.window, self.current_player.current_player)
            if string:
                return string
    def search_words(self):
        word_list = []
        # Wyszukiwanie poziome
        for row in self.board_logic:
            word = ""
            for cell in row:
                if cell[0] is not None:
                    word += cell[0]
                else:
                    if word != "":
                        word_list.append(word)
                        word = ""
            if word != "":
                word_list.append(word)

        # Wyszukiwanie pionowe
        for col in range(len(self.board_logic[0])):
            word = ""
            for row in range(len(self.board_logic)):
                cell = self.board_logic[row][col]
                if cell[0] is not None:
                    word += cell[0]
                else:
                    if word != "":
                        word_list.append(word)
                        word = ""
            if word != "":
                word_list.append(word)

        word_list = [word for word in word_list if len(word) > 1]
                
        found_words = []
        english_dict = enchant.Dict("en_US")
        for word in word_list:
            if english_dict.check(word):
                found_words.append(word)
        return found_words

    def find_word(self, word):
        # Wyszukiwanie poziome
        for row in range(len(self.board_logic)):
            for col in range(len(self.board_logic[0])):
                found_word = ""
                for i in range(len(word)):
                    if col + i >= len(self.board_logic[0]):
                        break
                    cell = self.board_logic[row][col + i]
                    if cell[0] is None:
                        break
                    found_word += cell[0]
                if found_word == word:
                    return (row, col, "poziomo")

        # Wyszukiwanie pionowe
        for col in range(len(self.board_logic[0])):
            for row in range(len(self.board_logic)):
                found_word = ""
                for i in range(len(word)):
                    if row + i >= len(self.board_logic):
                        break
                    cell = self.board_logic[row + i][col]
                    if cell[0] is None:
                        break
                    found_word += cell[0]
                if found_word == word:
                    return (row, col, "pionowo")

        return None

class Square:
    def __init__(self, nr):
        self.nr = nr
        self.board = None
        self.letter = None
        self.color = SQUARE_COLOR
        self.is_dragging = False
        self.reset_pos = (SQUARE_RESET_POS_X, SQUARE_RESET_POS_Y)
 
    def __str__(self):
        return f"ID: {self.nr}\nLetter: {self.letter}\nCoords: {self.reset_pos}\n"

    def set_letter(self, letter):
        self.letter = letter

    def set_board(self, board):
        self.board = board
    
    def make_rect(self):
        self.font = pygame.font.Font(None, 30)
        self.rect = pygame.Rect(self.board.width - 80, 100 + self.nr * 40, 40, 40)
        self.rect.center = (self.board.width - 60, 120 + self.nr * 40)
        self.reset_pos = self.rect.center
        self.letter_text = self.font.render(self.letter, True, self.board.WHITE)
        
    def draw(self):
        pygame.draw.rect(self.board.window, self.board.BLACK, self.rect)
        self.board.window.blit(self.letter_text, (self.rect.centerx - self.letter_text.get_width() // 2, self.rect.centery - self.letter_text.get_height() // 2))

    def handle_event(self, event, board, p1_letters, p2_letters):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.is_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.is_dragging = False
            mouse_pos = pygame.mouse.get_pos()
            if (0 < self.rect.center[0] < (15 * 42)) and (0 < self.rect.center[1] < (16 * 42)):
                x = int(self.rect.center[0] / 42)
                y = int(self.rect.center[1] / 42)
                self.rect.center = (x * 42 + 20, y * 42 + 20)
                licznik = 0
                if board.board_logic[x][y][0] is None:
                    for letter in p1_letters:
                        if letter.rect.center == (x * 42 + 20, y * 42 + 20):
                            licznik += 1
                            if licznik == 2:
                                self.rect.center = self.reset_pos
                                return
                    licznik = 0
                    for letter in p2_letters:
                        if letter.rect.center == (x * 42 + 20, y * 42 + 20):
                            licznik += 1
                            if licznik == 2:
                                self.rect.center = self.reset_pos
                                return
                else:
                    self.rect.center = self.reset_pos
            else:
                # Jeśli kwadrat nie został umieszczony na planszy, resetuj jego pozycję
                self.rect.center = self.reset_pos
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if self.is_dragging:
                self.rect.center = mouse_pos
                
    #? sprawdzanie czy klocek jest na plasznzy po kliknięciu pass            
    def check_if_on_board(self):
        if self.rect.center[0] > 1700:
            return False
        else:
            return True


class Score(pygame.Surface):
    def __init__(self, player: str):
        super().__init__((250, 100))
        self.player = player.capitalize()
        self.rect = self.get_rect()
        self.font = pygame.font.Font(None, 50)
        self.score = 0

    def set_center(self, x, y):
        self.rect.center = x, y

    def draw_score(self, screen: pygame.display, screen_coords: tuple, is_current: bool):
        self.fill((255, 255, 255))

        if not is_current:
            color = (0, 0, 0)
        else:
            color = (150, 0, 0)

        player_name = self.font.render(self.player, True, color)
        player_name_rect = player_name.get_rect()
        player_name_rect.center = 100, 25

        self.blit(player_name, player_name_rect)

        score_text = self.font.render(str(self.score), True, color)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = 100, 75

        self.blit(score_text, score_text_rect)

        x, y = screen_coords
        self.rect.center = x, y

        screen.blit(self, self.rect)


class Concede(pygame.Surface):
    def __init__(self):
        super().__init__((300, 50))
        self.rect = self.get_rect()

    def set_center(self, x, y):
        self.rect.center = x, y

    def draw(self, window, current_player):
        self.fill((255, 255, 255))
        font = pygame.font.Font(None, 50)

        if current_player:
            text = font.render("Player 2 wins", True, (0, 0, 0))
        else:
            text = font.render("Player 1 wins", True, (0, 0, 0))

        text_rect = text.get_rect()
        text_rect.center = 150, 25

        self.blit(text, text_rect)

        window.blit(self, self.rect)