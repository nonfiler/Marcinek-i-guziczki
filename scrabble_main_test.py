import pygame
from menu import Menu
import board_new
from rules import Rules
from letters import LetterGenerator


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
            self.game.game_state = state.upper()
        else:
            self.game.game_state = self.state_dict[state]


class Game:
    def __init__(self):
        pygame.init()

        self.button_width = 350
        self.button_height = 80
        self.button_margin = 25
        self.button_start_x = 700
        self.button_start_y = 300

        desktop_sizes = pygame.display.get_desktop_sizes()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = desktop_sizes[0][0], desktop_sizes[0][1]
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Scrabble")

        self.game_state = "MENU"
        self.STATE_MANAGER = StateManager(self)

        self.current_player = 1
        self.player_turn = True

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GRAY = (150, 150, 150)

        self.MENU = Menu( self.SCREEN, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.BLACK, self.WHITE)
        self.RULES = Rules(self.SCREEN, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.BLACK, self.WHITE)
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

    def handle_event(self, event):
        if self.game_state == "GAME":
            if self.player_turn:
                for letter in self.player1_let:
                    letter.handle_event(event)
            else:
                for letter in self.player2_let:
                    letter.handle_event(event)

    def handle_mouse_input(self, mouse_pos, mouse_clicked):
        if self.game_state == "MENU":
            play_rect = pygame.Rect(self.SCREEN_WIDTH // 2 - 75, 250, 150, 50)
            rules_rect = pygame.Rect(self.SCREEN_WIDTH // 2 - 75, 350, 150, 50)
            exit_rect = pygame.Rect(self.SCREEN_WIDTH // 2 - 75, 450, 150, 50)

            if play_rect.collidepoint(mouse_pos) and mouse_clicked[0]:
                self.STATE_MANAGER.change_state("GAME")
            elif rules_rect.collidepoint(mouse_pos) and mouse_clicked[0]:
                self.STATE_MANAGER.change_state("RULES")
            elif exit_rect.collidepoint(mouse_pos) and mouse_clicked[0]:
                pygame.quit()

        elif self.game_state == "RULES":
            return_button_rect = pygame.Rect(self.SCREEN_WIDTH - 200, self.SCREEN_HEIGHT - 80, 150, 50)

            if return_button_rect.collidepoint(mouse_pos) and mouse_clicked[0]:
                self.STATE_MANAGER.change_state("MENU")

    def update(self):
        if self.game_state == "GAME":
            if self.player_turn:
                for letter in self.player1_let:
                    letter.update()
            else:
                for letter in self.player2_let:
                    letter.update()

    def render(self):
        if self.game_state == "MENU":
            self.MENU.draw_menu()
        elif self.game_state == "GAME":
            self.BOARD.print_board()
            if self.player_turn:
                for letter in self.player1_let:
                    letter.draw()
            else:
                for letter in self.player2_let:
                    letter.draw()
        elif self.game_state == "RULES":
            self.RULES.draw_rules_screen()

        pygame.display.flip()


def run_game():
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

            game.handle_event(event)

        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()
        game.handle_mouse_input(mouse_pos, mouse_clicked)

        game.update()
        game.render()

run_game()