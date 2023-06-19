import pygame
class Rules:
    def __init__(self, window, width, height, black, white):
        self.window = window
        self.width = width
        self.height = height
        self.active = False
        self.white = white
        self.black = black

    def draw_rules_screen(self):
        self.window.fill(self.white)

        font = pygame.font.Font(None, 40)
        title_text = font.render("Zasady gry Scrabble", True, self.black)
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
            text = font.render(rule, True, self.black)
            self.window.blit(text, (self.width // 2 - text.get_width() // 2, y_offset))
            y_offset += 50

        return_button_rect = pygame.Rect(self.width - 200, self.height - 80, 150, 50)
        pygame.draw.rect(self.window, self.black, return_button_rect)

        return_button_text = font.render("Powrót", True, self.white)
        self.window.blit(return_button_text, (return_button_rect.centerx - return_button_text.get_width() // 2, return_button_rect.centery - return_button_text.get_height() // 2))

        pygame.display.update()