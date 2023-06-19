import pygame
import buttons_on_board
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


# BUTTON_BACKGROUND_COLOR = (0, 0, 0)
# BUTTON_TEXT_COLOR = (255, 255, 255)

# class Button:
#     def __init__(self, rect, text, action):
#         self.rect = pygame.Rect(rect)
#         self.text = text
#         self.action = action

#     def draw(self, surface):
#         pygame.draw.rect(surface, BUTTON_BACKGROUND_COLOR, self.rect)
#         font = pygame.font.Font(None, 25)
#         text = font.render(self.text, True, BUTTON_TEXT_COLOR)
#         text_rect = text.get_rect(center=self.rect.center)
#         surface.blit(text, text_rect)

#     def handle_event(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             mouse_pos = pygame.mouse.get_pos()
#             if self.rect.collidepoint(mouse_pos):
#                 self.action()

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
        self.board_logic = [
            [(False, "3w"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2w"), (False, "3w"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "3w")],
            [(False, "empty"), (False, "2w"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2w"), (False, "empty")],
            [(False, "empty"), (False, "empty"), (False, "2w"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "2w"), (False, "empty"), (False, "empty"), (False, "empty")],
            [(False, "2l"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "2l")],
            [(False, "empty"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3w"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3w"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "empty")],
            [(False, "empty"), (False, "3l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3l"), (False, "empty")],
            [(False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2w"), (False, "empty"), (False, "2w"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty")],
            [(False, "2w"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "2w")],
            [(False, "3w"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2w"), (False, "empty"), (False, "2w"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "3w")],
            [(False, "empty"), (False, "3l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3l"), (False, "empty")],
            [(False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2w"), (False, "empty"), (False, "2w"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty")],
            [(False, "empty"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3w"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3w"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "empty")],
            [(False, "2l"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "2l")],
            [(False, "empty"), (False, "empty"), (False, "2w"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "2w"), (False, "empty"), (False, "empty"), (False, "empty")],
            [(False, "empty"), (False, "2w"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "3l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2w"), (False, "empty")],
            [(False, "3w"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "empty"), (False, "2w"), (False, "3w"), (False, "empty"), (False, "empty"), (False, "2l"), (False, "empty"), (False, "empty"), (False, "3w")]
        ]
        self.bonus_colors = {
            "2w": (255, 213, 0),   # Żółty
            "3w": (255, 96, 0),    # Czerwony
            "2l": (0, 186, 255),   # Niebieski
            "3l": (0, 98, 255)     # Ciemnoniebieski
        }
        
    #     button_width = 350
    #     button_height = 80
    #     button_margin = 25
    #     button_start_x = 700
    #     button_start_y = 300

    #     self.buttons = [
    #         Button((button_start_x, button_start_y, button_width, button_height), "Pass", self.button_pass),
    #         Button((button_start_x, button_start_y + button_height + button_margin, button_width, button_height), "Check Word", self.button_check_word),
    #         Button((button_start_x, button_start_y + 2 * (button_height + button_margin), button_width, button_height), "Change Letter", self.button_change_letter),
    #         Button((button_start_x, button_start_y + 3 * (button_height + button_margin), button_width, button_height), "Commence Defeat", self.button_commence_defeat)
    #     ]
        
    # def draw_buttons(self):
    #     for button in self.buttons:
    #         button.draw(self.window)

    # def handle_button_events(self, event):
    #     for button in self.buttons:
    #         button.handle_event(event)

    # def button_pass(self):
    #     # Implement the action for the "Pass" button
    #     print("Pass Button Pressed")
    #     print("Score Updated and Player Switched")

    # def button_check_word(self):
    #     # Implement the action for the "Check Word" button
    #     print("Check Word Button Pressed")
    #     print("Word Checked, Score Updated, and Player Switched")

    # def button_change_letter(self):
    #     # Implement the action for the "Change Random Letter" button
    #     print("Change Random Letter Button Pressed")
    #     print("Letter Changed, Score Updated, and Player Switched")

    # def button_commence_defeat(self):
    #     # Implement the action for the "Commence Defeat" button
    #     print("Commence Defeat Button Pressed")
    #     print("Score Reset and Player Switched")
        
    # def print_board(self):
    #     tile_size = 40  # Size of each tile on the board
    #     margin = 2  # Margin between tiles
        
    #     # Clear the window
    #     self.window.fill(self.WHITE)
        
    #     # Iterate over the board logic and draw each tile
    #     for row in range(len(self.board_logic)):
    #         for col in range(len(self.board_logic[row])):
    #             tile_x = col * (tile_size + margin)
    #             tile_y = row * (tile_size + margin)
                
    #             # Get the tile value and color
    #             tile_value = self.board_logic[row][col][1]
    #             tile_color = self.bonus_colors.get(tile_value, self.WHITE)
                
    #             # Draw the tile
    #             pygame.draw.rect(self.window, tile_color, (tile_x, tile_y, tile_size, tile_size))
    def print_board(self):
        tile_size = 40  # Size of each tile on the board
        margin = 2  # Margin between tiles
        margin_color = (0, 0, 0)  # Color of the margin
        
        # Clear the window
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
        buttons_on_board.draw_buttons()
        
        
        
class Square:
    def __init__(self, nr):
        self.nr = nr
        self.board = None
        self.letter = None
        self.color = SQUARE_COLOR
        self.is_dragging = False
        #self.start_pos = (x, y)
        self.reset_pos = (SQUARE_RESET_POS_X, SQUARE_RESET_POS_Y)
        # self.surface = pygame.Surface((40, 40))
        # self.rect = self.surface.get_rect(center=(20, 20))
        
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
                print(self.rect)