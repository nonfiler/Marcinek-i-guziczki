#lets make a change, user will have squares on the right side of the table and he can drag them to the board
#we will have to make a class for the squares and then make a list of them

import pygame

class Board:
    def __init__(self, window, width, height, black, white):
        self.window = window
        self.width = width
        self.height = height
        self.WHITE = white
        self.BLACK = black
        self.BEIGE = (255, 204, 102)
        self.tile_size = 48  # Rozmiar pojedynczego pola planszy
        self.board_size = self.tile_size * 15  # Rozmiar planszy
        self.board_x = 0
        self.board_y = self.height // 2 - self.board_size // 2
        self.bonus_tiles = {
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
        self.bonus_colors = {
            "2xWS": (255, 213, 0),   # Żółty
            "3xWS": (255, 96, 0),    # Czerwony
            "2xLS": (0, 186, 255),   # Niebieski
            "3xLS": (0, 98, 255)     # Ciemnoniebieski
            # Dodaj tutaj inne kolory, jeśli są potrzebne
        }

        self.selected_square = None  # Wybrany kwadrat
        self.selected_square_row = None  # Wiersz wybranego kwadratu
        self.selected_square_col = None  # Kolumna wybranego kwadratu

    def draw_board(self):
        self.window.fill(self.BEIGE)

        # Rysowanie planszy
        for row in range(15):
            for col in range(15):
                tile_rect = pygame.Rect(self.board_x + col * self.tile_size,
                                        self.board_y + row * self.tile_size,
                                        self.tile_size, self.tile_size)

                # Ustalanie grubości obwódki w zależności od położenia pola
                border_width = 1
                if row == 0 or row == 14 or col == 0 or col == 14:
                    border_width = 2

                pygame.draw.rect(self.window, self.BLACK, tile_rect, border_width)  # Obwódka czarna

                # Rysowanie pól specjalnych
                if (row, col) in self.bonus_tiles:
                    bonus = self.bonus_tiles[(row, col)]
                    bonus_color = self.bonus_colors[bonus]

                    pygame.draw.rect(self.window, bonus_color, tile_rect)
                    pygame.draw.rect(self.window, self.BLACK, tile_rect, border_width)  # Obwódka czarna

                    font = pygame.font.Font(None, 20)
                    text_render = font.render(bonus, True, self.BLACK)
                    text_rect = text_render.get_rect(center=tile_rect.center)
                    self.window.blit(text_render, text_rect)

        pygame.display.update()

    def get_tile_coordinates(self, row, col):
        x = self.board_x + col * self.tile_size
        y = self.board_y + row * self.tile_size
        return x, y

    def draw_square_on_tile(self, row, col):
        tile_x, tile_y = self.get_tile_coordinates(row, col)
        square_rect = pygame.Rect(tile_x, tile_y, self.tile_size, self.tile_size)
        pygame.draw.rect(self.window, self.WHITE, square_rect)
        pygame.display.update()

    def handle_click(self, mouse_pos):
        click_x, click_y = mouse_pos
        # Sprawdzanie, czy kliknięcie mieści się na planszy
        if (self.board_x <= click_x <= self.board_x + self.board_size and
                self.board_y <= click_y <= self.board_y + self.board_size):
            # Obliczanie indeksów pola planszy na które kliknięto
            col = (click_x - self.board_x) // self.tile_size
            row = (click_y - self.board_y) // self.tile_size
            if self.selected_square is None:
                # Jeśli nie ma wybranego kwadratu, zapisujemy kliknięte pole jako wybrany kwadrat
                self.selected_square = pygame.Rect(self.get_tile_coordinates(row, col), (self.tile_size, self.tile_size))
                self.selected_square_row = row
                self.selected_square_col = col
                pygame.draw.rect(self.window, self.WHITE, self.selected_square)
            else:
                # Jeśli jest już wybrany kwadrat, przenosimy go na nowe pole
                selected_square_copy = self.selected_square.copy()
                self.draw_square_on_tile(self.selected_square_row, self.selected_square_col)
                self.selected_square = pygame.Rect(self.get_tile_coordinates(row, col), (self.tile_size, self.tile_size))
                self.selected_square_row = row
                self.selected_square_col = col
                pygame.draw.rect(self.window, self.WHITE, self.selected_square)
                pygame.display.update()
        else:
            # Kliknięcie poza planszą, czyścimy wybrany kwadrat
            if self.selected_square is not None:
                self.draw_square_on_tile(self.selected_square_row, self.selected_square_col)
                self.selected_square = None
                self.selected_square_row = None
                self.selected_square_col = None

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Plansza z kwadratem")

# Kolory
black = (0, 0, 0)
white = (255, 255, 255)

# Utworzenie obiektu planszy
board = Board(window, window_width, window_height, black, white)

# Rysowanie planszy
board.draw_board()

# Pętla zdarzeń Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            board.handle_click(mouse_pos)

pygame.quit()
