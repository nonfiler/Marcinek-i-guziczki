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
