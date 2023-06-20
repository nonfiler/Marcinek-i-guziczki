import pygame
from buttons_on_board import GameControls

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
    def __init__(self, window, width, height, black, white, p1_let, p2_let, c_player):
        self.window = window
        self.width = width
        self.height = height
        self.WHITE = white
        self.BLACK = black
        self.player1_letters = p1_let
        self.player2_letters = p2_let       
        self.current_player = c_player

        self.game_controls = GameControls()
        self.game_controls.set_center(x=self.width - 155, y=self.height - 170)

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



    def handle_event(self, event):
        for button in self.game_controls.buttons:
            return button.handle_event(event, self.current_player)

class Square:
    def __init__(self, nr):
        self.nr = nr
        self.board = None
        self.letter = None
        self.color = SQUARE_COLOR
        self.is_dragging = False
        self.reset_pos = (SQUARE_RESET_POS_X, SQUARE_RESET_POS_Y)
 
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

    def handle_event(self, event):
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
            else:
                # Jeśli kwadrat nie został umieszczony na planszy, resetuj jego pozycję
                self.rect.center = self.reset_pos
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if self.is_dragging:
                self.rect.center = mouse_pos
                
    #? sprawdzanie czy klocek jest na plasznzy po kliknięciu pass            
    def check_if_on_board(self):
        if self.rect.centerx > 1800:
            return False
        else:
            return True