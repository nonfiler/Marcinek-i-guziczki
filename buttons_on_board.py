import pygame
BOARD_SIZE = 15
BOARD_POS_X = 50
BOARD_POS_Y = 50
BOARD_COLOR = (200, 200, 200)
TILE_COLOR = (255, 255, 255)
TILE_BORDER_COLOR = (0, 0, 0)

BUTTON_BACKGROUND_COLOR = (0, 0, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)

class Button:
    def __init__(self, rect, text, action):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.action = action
        

        
        
# buttons = [
#     Button((button_start_x, button_start_y, button_width, button_height), "Pass", button_pass),
#     Button((button_start_x, button_start_y + button_height + button_margin, button_width, button_height), "Check Word", self.button_check_word),
#     Button((button_start_x, button_start_y + 2 * (button_height + button_margin), button_width, button_height), "Change Letter", self.button_change_letter),
#     Button((button_start_x, button_start_y + 3 * (button_height + button_margin), button_width, button_height), "Commence Defeat", self.button_commence_defeat)
# ]

    def draw(self, surface):
        pygame.draw.rect(surface, BUTTON_BACKGROUND_COLOR, self.rect)
        font = pygame.font.Font(None, 25)
        text = font.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.action()
                


        
    def draw_buttons(self):
        for button in self.buttons:
            button.draw(self.window)

    def handle_button_events(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def button_pass(self):
        # Implement the action for the "Pass" button
        print("Pass Button Pressed")
        print("Score Updated and Player Switched")

    def button_check_word(self):
        # Implement the action for the "Check Word" button
        print("Check Word Button Pressed")
        print("Word Checked, Score Updated, and Player Switched")

    def button_change_letter(self):
        # Implement the action for the "Change Random Letter" button
        print("Change Random Letter Button Pressed")
        print("Letter Changed, Score Updated, and Player Switched")

    def button_commence_defeat(self):
        # Implement the action for the "Commence Defeat" button
        print("Commence Defeat Button Pressed")
        print("Score Reset and Player Switched")