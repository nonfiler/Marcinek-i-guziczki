import pygame
import board_new
from letters import LetterGenerator

# Pewnie zapytacie "Co to do chuja wuja jest"
# Na co ja wam odpowiem - czy nudziło mi się w nocy? Być może
# Czy to działa? Nie, bo nie jest kompletne. Ale macie dzięki temu framework.
# Framework na zrobienie tego dobrze. Na tyle dobrze, że Oskarek izi zda.
# Nie musicie z tego korzystać, natomiast polecam. Pozwoli to trochę odspaghettowić ten kod.
# Wszystko co tutaj macie jest posortowane i w miarę uporządkowane.
# Podstawowe klasy zostały przerobione, żeby współgrały z nową klasą Game.
# Spokojnie, oryginały są nadal bezpiecznie schowane w swoich plikach.
# Także bawcie się rano dobrze, a ja idę spać.
# I nie Kacperek, odgruzowanie tego nie zajęło jakoś w chuj długo. Około 20 minut, więc jeżeliby
# odgruzować resztę (a wy dużo lepiej ode mnie wiecie jak to działa) to myślę, że w 2 godzinki udałoby się napisać
# zrefaktoryzowany kod, który byłby milion razy bardziej czytelny. A dużo bardziej czytelny kod, oznacza o wiele mniej
# debugowania i o wiele szybsze pisanie nowego kodu.


class StateManager:
    def __init__(self, game):
        self.game = game
        self.state_dict = {
            1: "MENU",
            2: "GAME",
            3: "RULES"
        }

    def change_state(self, state: int or str):
        if isinstance(state, str):
            self.game.state = state.upper()
        else:
            self.game.state = self.state_dict[state]


class Game:
    def __init__(self):
        pygame.init()

        self.button_width = 350
        self.button_height = 80
        self.button_margin = 25
        self.button_start_x = 700
        self.button_start_y = 300

        # Robimy ekran
        desktop_sizes = pygame.display.get_desktop_sizes()  # Zbiera rozmiary wszystkich ekranów
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = desktop_sizes[0][0], desktop_sizes[0][1]    # Korzystamy z wymiarów głównego ekranu systemu
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Scrabble")

        self.game_state = "MENU"
        self.STATE_MANAGER = StateManager(self)

        self.current_player = 1

        self.player_turn = True

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GRAY = (150, 150, 150)

        self.MENU = Menu(self)
        self.RULES = Rules(self)
        self.LETTERS = LetterGenerator()

        self.player1_let = []

        self.player2_let = []

        self.BOARD = board_new.Board(self.SCREEN, self.SCREEN_WIDTH, self.SCREEN_HEIGHT,
                                     self.BLACK, self.WHITE, self.player1_let,
                                     self.player2_let, self.current_player)

        self.player1_let = self.LETTERS.generate_letters(7)
        self.player2_let = self.LETTERS.generate_letters(7)

        for x in self.player1_let:
            x.set_board(self.BOARD)

        for x in self.player2_let:
            x.set_board(self.BOARD)

        self.main()

    def main(self):
        match self.game_state:

            case "MENU":
                self.menu()

            case "GAME":
                self.game_screen()

            case "RULES":
                self.rules_screen()


    # Generalnie tutaj najpierw chcecie wystartować od robienia updateów i ogarniania inputu
    # a dopiero potem chcecie strzelać rysowanie na ekranie.
    # Tak. Mówię o każdej z tych funkcji.
    def menu(self):
        self.MENU.draw()
        pygame.display.flip()
    def game_screen(self):
        pygame.display.flip()
    def rules_screen(self):
        self.RULES.draw()
        pygame.display.flip()


class Menu:
    def __init__(self, game):
        self.window = game.SCREEN
        self.width = game.SCREEN_WIDTH
        self.height = game.SCREEN_HEIGHT
        self.WHITE = game.WHITE
        self.BLACK = game.BLACK
        self.game = game

        font = pygame.font.Font(None, 50)
        self.title_text = font.render("Scrabble", True, (0, 0, 0))
        font = pygame.font.Font(None, 30)
        self.play_text = font.render("Graj", True, self.WHITE)
        self.rules_text = font.render("Zasady", True, self.WHITE)
        self.exit_text = font.render("Wyjdź", True, self.WHITE)

    def draw(self):
        self.window.fill(self.WHITE)

        self.window.blit(self.title_text, (self.width // 2 - self.title_text.get_width() // 2, 100))

        play_rect = pygame.Rect(self.width // 2 - 75, 250, 150, 50)
        rules_rect = pygame.Rect(self.width // 2 - 75, 350, 150, 50)
        exit_rect = pygame.Rect(self.width // 2 - 75, 450, 150, 50)

        pygame.draw.rect(self.window, self.BLACK, play_rect)
        pygame.draw.rect(self.window, self.BLACK, rules_rect)
        pygame.draw.rect(self.window, self.BLACK, exit_rect)

        self.window.blit(self.play_text, (play_rect.centerx - self.play_text.get_width() // 2, play_rect.centery - self.play_text.get_height() // 2))
        self.window.blit(self.rules_text, (rules_rect.centerx - self.rules_text.get_width() // 2, rules_rect.centery - self.rules_text.get_height() // 2))
        self.window.blit(self.exit_text, (exit_rect.centerx - self.exit_text.get_width() // 2, exit_rect.centery - self.exit_text.get_height() // 2))


class Rules:
    def __init__(self, game):
        self.window = game.SCREEN
        self.width = game.SCREEN_WIDTH
        self.height = game.SCREEN_HEIGHT
        self.WHITE = game.WHITE
        self.BLACK = game.BLACK
        self.game = game

    def draw(self):
        self.window.fill(self.WHITE)

        font = pygame.font.Font(None, 40)
        title_text = font.render("Zasady gry Scrabble", True, self.BLACK)
        self.window.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 100))

        rules_text = [
            "Scrabble to gra słowna dla dwóch do czterech graczy.",
            "Celem gry jest ułożenie jak największej liczby słów",
            "na planszy za pomocą posiadanych liter.",
            "Gracze mogą budować słowa pionowo lub poziomo,",
            "łącząc litery ze sobą.",
            "Punkty są przyznawane za wartość liter oraz bonusy",
            "za użycie pól premiowych na planszy.",
            # Wprowadź tutaj pozostałe zasady gry Scrabble
        ]

        y_offset = 200
        for rule in rules_text:
            text = font.render(rule, True, self.BLACK)
            self.window.blit(text, (self.width // 2 - text.get_width() // 2, y_offset))
            y_offset += 50

        return_button_rect = pygame.Rect(self.width - 200, self.height - 80, 150, 50)
        pygame.draw.rect(self.window, self.BLACK, return_button_rect)

        return_button_text = font.render("Powrót", True, self.WHITE)
        self.window.blit(return_button_text, (return_button_rect.centerx - return_button_text.get_width() // 2, return_button_rect.centery - return_button_text.get_height() // 2))


class Board:
    def __init__(self, game):
        self.window = game.SCREEN
        self.width = game.SCREEN_WIDTH
        self.height = game.SCREEN_HEIGHT
        self.WHITE = game.WHITE
        self.BLACK = game.BLACK
        self.player1_letters = game.player1_let
        self.player2_letters = game.player2_let
        self.current_player = game.current_player
        self.game = game

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
            "2xWS": (255, 213, 0),  # Żółty
            "3xWS": (255, 96, 0),  # Czerwony
            "2xLS": (0, 186, 255),  # Niebieski
            "3xLS": (0, 98, 255)  # Ciemnoniebieski
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
            self.window.blit(letter_text, (
            letter_rect.centerx - letter_text.get_width() // 2, letter_rect.centery - letter_text.get_height() // 2))