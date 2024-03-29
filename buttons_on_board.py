import pygame
from time import sleep
BOARD_SIZE = 15
BOARD_POS_X = 50
BOARD_POS_Y = 50
BOARD_COLOR = (200, 200, 200)
TILE_COLOR = (255, 255, 255)
TILE_BORDER_COLOR = (0, 0, 0)

BUTTON_BACKGROUND_COLOR = (0, 0, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)

class GameControls:

    def __init__(self, w=310, h=340, x=0, y=0):
        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect()
        self.rect.center = x, y
        self.surface.fill((0, 0, 0))
        self.buttons = []

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    def add_button(self, text, w=300, h=80, x=0, y=0):
        self.buttons.append(Button(text, w, h, x, y))

    def set_center(self, x, y):
        self.rect.center = x, y


class Button:
    def __init__(self, text, w=300, h=80, x=0, y=0):
        self.surface = pygame.Surface((w, h))
        self.surface.fill((150, 150, 150))
        self.rect = self.surface.get_rect()
        self.rect.center = x, y
        self.text = text

    def set_center(self, coords: tuple):
        self.rect.center = coords

    def draw(self, surface):
        font = pygame.font.Font(None, 32)
        text = font.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text.get_rect(center=self.rect.center)
        text_rect.center = self.rect.w // 2, self.rect.h // 2
        self.surface.blit(text, text_rect)
        surface.blit(self.surface, self.rect)

    def handle_event(self, event, concede, window, current_player):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                return self.action(concede, window, current_player)
        return False

    def action(self, concede, window, current_player):
        match self.text:
            case "Pass":
                return "Pass"

            case "Check word":
                return "Check word"

            case "Change letter":
                self.button_change_letter()

            case "Commence defeat":
                self.button_commence_defeat(concede, window, current_player)

    def button_change_letter(self):
        # Implement the action for the "Change Random Letter" button
        print("Change Random Letter Button Pressed")
        print("Letter Changed, Score Updated, and Player Switched")

    def button_commence_defeat(self, concede, window, current_player):
        # Implement the action for the "Commence Defeat" button
        print("Commence Defeat Button Pressed, Game over")
        concede.draw(window, current_player)
        pygame.display.flip()
        sleep(3)
        pygame.quit()
