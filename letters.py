import random
from board_new import Square
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
            for x in range(num_letters):
                letter = random.choice(list(self.available_letters.keys()))
                square = Square(x)
                square.set_letter(letter)
                letters.append(square)
                self.available_letters[letter] -= 1
                if self.available_letters[letter] == 0:
                    del self.available_letters[letter]
            self.generated_letters = True
        return letters
