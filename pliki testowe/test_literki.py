import pygame
from pygame.locals import *
import random
import sys

class LetterGenerator:
    def __init__(self):
        self.available_letters = {
            'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2,
            'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, 'Blank': 2
        }
        self.generated_letters = False

    def generate_letters(self, num_letters):
        letters = []
        if not self.generated_letters:
            for _ in range(num_letters):
                letter = random.choice(list(self.available_letters.keys()))
                letters.append(letter)
                self.available_letters[letter] -= 1
                if self.available_letters[letter] == 0:
                    del self.available_letters[letter]
            self.generated_letters = True
        return letters

if __name__ == '__main__':
    # Inicjalizacja Pygame
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Wylosowane litery")

    # Inicjalizacja generatora liter
    generator = LetterGenerator()
    num_letters = 7
    letters = generator.generate_letters(num_letters)

    # Główna pętla gry
    running = True
    while running:
        screen.fill((255, 255, 255))

        # Wyświetlanie wylosowanych liter
        font = pygame.font.Font(None, 36)
        text = font.render("Wylosowane litery:", True, (0, 0, 0))
        screen.blit(text, (20, 20))

        letter_spacing = 40
        x = 20
        y = 60

        previous_is_blank = False
        for i, letter in enumerate(letters):
            if letter == "Blank":
                if previous_is_blank:
                    x += 0
                else:
                    x += letter_spacing
            

                letter_text = font.render(letter, True, (0, 0, 0))
                previous_is_blank = True
            else:
                if previous_is_blank:
                    x += letter_spacing

                letter_text = font.render(letter, True, (0, 0, 0))
                previous_is_blank = False

            screen.blit(letter_text, (x, y))
            x += letter_spacing

        pygame.display.flip()

        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

    # Zakończenie programu
    pygame.quit()
