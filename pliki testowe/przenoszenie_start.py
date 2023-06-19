import pygame

# Inicjalizacja biblioteki Pygame
pygame.init()

# Ustawienia planszy
BOARD_SIZE = 15
TILE_SIZE = 50
BOARD_POS_X = 50
BOARD_POS_Y = 50
BOARD_COLOR = (200, 200, 200)
TILE_COLOR = (255, 255, 255)
TILE_BORDER_COLOR = (0, 0, 0)

# Ustawienia kwadratu z literką
SQUARE_SIZE = 50
SQUARE_START_POS_X = 600
SQUARE_START_POS_Y = 50
SQUARE_COLOR = (255, 0, 0)
SQUARE_RESET_POS_X = 100
SQUARE_RESET_POS_Y = 100

# Ustalanie rozmiarów okna
WINDOW_WIDTH = BOARD_POS_X + BOARD_SIZE * TILE_SIZE + 200
WINDOW_HEIGHT = BOARD_POS_Y + BOARD_SIZE * TILE_SIZE

# Inicjalizacja okna gry
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Przenoszenie kwadratów")

# Klasa reprezentująca pole na planszy
class Tile:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.color = TILE_COLOR
        self.border_color = TILE_BORDER_COLOR
        self.is_occupied = False

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)
        pygame.draw.rect(window, self.border_color, self.rect, 1)

# Klasa reprezentująca kwadrat z literką
class Square:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
        self.color = SQUARE_COLOR
        self.is_dragging = False
        self.start_pos = (x, y)
        self.reset_pos = (SQUARE_RESET_POS_X, SQUARE_RESET_POS_Y)

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                self.is_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.is_dragging = False
            # Sprawdzanie, czy kwadrat jest na planszy i stawianie go na najbliższym polu
            for tile in board:
                if tile.rect.collidepoint(self.rect.center) and not tile.is_occupied:
                    self.rect.center = tile.rect.center
                    tile.is_occupied = True
                    break
            else:
                # Jeśli kwadrat nie został umieszczony na planszy, resetuj jego pozycję
                self.rect.center = self.reset_pos
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if self.is_dragging:
                self.rect.center = mouse_pos

# Tworzenie planszy
board = []
for row in range(BOARD_SIZE):
    for col in range(BOARD_SIZE):
        x = BOARD_POS_X + col * TILE_SIZE
        y = BOARD_POS_Y + row * TILE_SIZE
        tile = Tile(x, y)
        board.append(tile)

# Tworzenie kwadratu z literką
square = Square(SQUARE_START_POS_X, SQUARE_START_POS_Y)

# Główna pętla gry
while True:
    window.fill(BOARD_COLOR)

    for tile in board:
        tile.draw()

    # Rysowanie kwadratu z literką
    square.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        square.handle_event(event)

    # Sprawdzanie, czy kwadrat jest poza planszą
    if not square.rect.colliderect(pygame.Rect(BOARD_POS_X, BOARD_POS_Y, BOARD_SIZE * TILE_SIZE, BOARD_SIZE * TILE_SIZE)):
        square.rect.center = square.reset_pos

    pygame.display.update()
