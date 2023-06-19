import pygame
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
    BEIGE = (255, 204, 102)
    def draw_board(self):
        self.window.fill(self.WHITE)

        tile_size = 48  # Rozmiar pojedynczego pola planszy
        board_size = tile_size * 15  # Rozmiar planszy

        # Definiowanie bonusów na planszy
        bonus_tiles = {
            (0, 0): "3xWS",  # Potrójne słowo - Start
            (7, 7): "2xWS",  # Podwójne słowo - Środek planszy
            (0, 3): "2xLS",  # Podwójne litera
            (2, 6): "3xLS",  # Potrójne litera
            (0, 7): "3xWS",  # Potrójne słowo
            (0, 11): "2xLS",  # Podwójne litera
            (1, 5): "3xLS",  # Potrójne litera
            (1, 9): "3xLS",  # Potrójne litera
            (2, 2): "2xWS",  # Podwójne słowo
            (2, 8): "2xWS",  # Podwójne słowo
            (3, 0): "2xLS",  # Podwójne litera
            (3, 7): "2xLS",  # Podwójne litera
            (3, 14): "2xLS",  # Podwójne litera
            (5, 1): "3xLS",  # Potrójne litera
            (5, 5): "3xLS",  # Potrójne litera
            (5, 9): "3xLS",  # Potrójne litera
            (5, 13): "3xLS",  # Potrójne litera
            (6, 2): "2xWS",  # Podwójne słowo
            (6, 6): "3xLS",  # Potrójne litera
            (6, 8): "3xLS",  # Potrójne litera
            (6, 12): "2xWS",  # Podwójne słowo
            (7, 3): "2xLS",  # Podwójne litera
            (7, 11): "2xLS",  # Podwójne litera
            (8, 2): "2xWS",  # Podwójne słowo
            (8, 6): "3xLS",  # Potrójne litera
            (8, 8): "3xLS",  # Potrójne litera
            (8, 12): "2xWS",  # Podwójne słowo
            (9, 1): "3xLS",  # Potrójne litera
            (9, 5): "3xLS",  # Potrójne litera
            (9, 9): "3xLS",  # Potrójne litera
            (9, 13): "3xLS",  # Potrójne litera
            (11, 0): "2xLS",  # Podwójne litera
            (11, 7): "2xLS",  # Podwójne litera
            (11, 14): "2xLS",  # Podwójne litera
            (12, 2): "2xWS",  # Podwójne słowo
            (12, 6): "3xLS",  # Potrójne litera
            (12, 8): "3xLS",  # Potrójne litera
            (12, 12): "2xWS",  # Podwójne słowo
            (13, 5): "3xLS",  # Potrójne litera
            (13, 9): "3xLS",  # Potrójne litera
            (14, 3): "2xLS",  # Podwójne litera
            (14, 11): "2xLS"  # Podwójne litera
        }


        # Kolory pól specjalnych
        bonus_colors = {
            "2xWS": (255, 213, 0),   # Żółty
            "3xWS": (255, 96, 0),    # Czerwony
            "2xLS": (0, 186, 255),   # Niebieski
            "3xLS": (0, 98, 255)     # Ciemnoniebieski
        }

        # Wyznaczanie pozycji planszy na ekranie
        board_x = 0
        board_y = self.height // 2 - board_size // 2

        # Rysowanie planszy
        for row in range(15):
            for col in range(15):
                tile_rect = pygame.Rect(board_x + col * tile_size, board_y + row * tile_size, tile_size, tile_size)

                # Ustalanie grubości obwódki w zależności od położenia pola
                border_width = 1
                if row == 0 or row == 14 or col == 0 or col == 14:
                    border_width = 2

                pygame.draw.rect(self.window, self.BLACK, tile_rect, border_width)  # Obwódka czarna

                # Rysowanie pól specjalnych
                if (row, col) in bonus_tiles:
                    bonus = bonus_tiles[(row, col)]
                    bonus_color = bonus_colors[bonus]

                    pygame.draw.rect(self.window, bonus_color, tile_rect)
                    pygame.draw.rect(self.window, self.BLACK, tile_rect, border_width)  # Obwódka czarna

                    font = pygame.font.Font(None, 20)
                    text_render = font.render(bonus, True, self.BLACK)
                    text_rect = text_render.get_rect(center=tile_rect.center)
                    self.window.blit(text_render, text_rect)
        
        
        font = pygame.font.Font(None, 30)
        player_letters = self.player1_letters if self.current_player == 1 else self.player2_letters
        for i, letter in enumerate(player_letters):
            letter_rect = pygame.Rect(self.width - 80, 100 + i * 50, 50, 50)
            pygame.draw.rect(self.window, self.BLACK, letter_rect)
            letter_text = font.render(letter, True, self.WHITE)
            self.window.blit(letter_text, (letter_rect.centerx - letter_text.get_width() // 2, letter_rect.centery - letter_text.get_height() // 2))
    
        
        
        pygame.display.update()            