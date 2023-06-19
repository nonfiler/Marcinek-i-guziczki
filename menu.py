import pygame
# import sys
# from board import Game
# from rules import Rules

class Menu:
    def __init__(self, window, width, height, black, white):
        self.window = window
        self.width = width
        self.height = height
        self.active = True
        self.WHITE = white
        self.BLACK = black

    def draw_menu(self):
        self.window.fill(self.WHITE)

        font = pygame.font.Font(None, 50)
        title_text = font.render("Scrabble", True, (0, 0, 0))
        self.window.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 100))

        font = pygame.font.Font(None, 30)
        play_text = font.render("Graj", True, self.WHITE)
        rules_text = font.render("Zasady", True, self.WHITE)
        exit_text = font.render("Wyjdź", True, self.WHITE)

        play_rect = pygame.Rect(self.width // 2 - 75, 250, 150, 50)
        rules_rect = pygame.Rect(self.width // 2 - 75, 350, 150, 50)
        exit_rect = pygame.Rect(self.width // 2 - 75, 450, 150, 50)

        pygame.draw.rect(self.window, self.BLACK, play_rect)
        pygame.draw.rect(self.window, self.BLACK, rules_rect)
        pygame.draw.rect(self.window, self.BLACK, exit_rect)

        self.window.blit(play_text, (play_rect.centerx - play_text.get_width() // 2, play_rect.centery - play_text.get_height() // 2))
        self.window.blit(rules_text, (rules_rect.centerx - rules_text.get_width() // 2, rules_rect.centery - rules_text.get_height() // 2))
        self.window.blit(exit_text, (exit_rect.centerx - exit_text.get_width() // 2, exit_rect.centery - exit_text.get_height() // 2))

        pygame.display.update()

    # def handle_mouse_click(self, mouse_pos):
    #         play_rect = pygame.Rect(self.width // 2 - 75, 250, 150, 50)
    #         rules_rect = pygame.Rect(self.width // 2 - 75, 350, 150, 50)
    #         exit_rect = pygame.Rect(self.width // 2 - 75, 450, 150, 50)

    #         if play_rect.collidepoint(mouse_pos):
    #             self.active = False
    #             Game.active = True
    #         elif rules_rect.collidepoint(mouse_pos):
    #             self.active = False
    #             Rules.active = True
    #         elif exit_rect.collidepoint(mouse_pos):
    #             pygame.quit()

    #             sys.exit()
