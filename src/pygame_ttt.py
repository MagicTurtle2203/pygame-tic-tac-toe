import pygame
import ttt


class TicTacToeGame:
    def __init__(self):
        self._ttt = ttt.TicTacToe()
        self.running = True

    def main(self):
        pygame.init()

        display_surface = pygame.display.set_mode((300 + 20, 350 + 20))

        ttt_surface = pygame.Surface((300, 300))

        b_list = [ttt_surface.blit(pygame.Surface((100, 100)), (x, y)) for y in [0, 100, 200] for x in [0, 100, 200]]

        pygame.draw.line(ttt_surface, (255, 255, 255), (100, 0), (100, 300), 5)
        pygame.draw.line(ttt_surface, (255, 255, 255), (200, 0), (200, 300), 5)
        pygame.draw.line(ttt_surface, (255, 255, 255), (0, 100), (300, 100), 5)
        pygame.draw.line(ttt_surface, (255, 255, 255), (0, 200), (300, 200), 5)

        display_surface.blit(ttt_surface, (10, 10))

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self._ttt.winner is None:
                        pos = pygame.mouse.get_pos()

                        for i in range(len(b_list)):
                            if b_list[i].collidepoint(pos):
                                try:
                                    self._ttt.add_move(i)
                                    self._ttt.display_board()
                                except ttt.SpotAlreadyTaken as e:
                                    print(e)
                                    continue

            self._draw_board()

        pygame.quit()

    def _draw_board(self):
        display_surface = pygame.display.get_surface()

        font = pygame.font.Font('freesansbold.ttf', 32)
        text_surface = pygame.Surface((300, 50))

        if self._ttt.winner is None:
            text = font.render(f"{self._ttt.turn.upper()}'s turn", True, (255, 255, 255))
            text_surface.blit(text, (93, 15))
        elif self._ttt.winner == 'tie':
            text = font.render("Tie!", True, (255, 255, 255))
            text_surface.blit(text, (122, 15))
        else:
            text = font.render(f"{self._ttt.winner.upper()} is the winner!", True, (255, 255, 255))
            text_surface.blit(text, (25, 15))

        display_surface.blit(text_surface, (10, 300))

        pygame.display.flip()


if __name__ == '__main__':
    TicTacToeGame().main()
