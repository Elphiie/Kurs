from game import Game

import pygame


class TheGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)

    def play(self):
        """
        Test the AI against a human player by passing a NEAT neural network
        """
        clock = pygame.time.Clock()
        run = True
        while run:

            clock.tick(60)
            fps=clock.get_fps()
            self.game.fps = round(fps, 0)
            game_info = self.game.loop()

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    run = False
                    break
            

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:    #move up
                self.game.move_life(left=False, up=True, right=False, down=True)
            elif keys[pygame.K_s]:  #move down
                self.game.move_life(left=False, up=False, right=False, down=True)
            elif keys[pygame.K_a]:  #move left
                self.game.move_life(left=True, up=False, right=False, down=True)
            elif keys[pygame.K_d]:  #move right
                self.game.move_life(left=False, up=False, right=True, down=True)

                #diagonal movement
            if keys[pygame.K_w] and keys[pygame.K_a]:  #move down and left
                self.game.move_life(left=True, up=True, right=False, down=True)
            elif keys[pygame.K_w] and keys[pygame.K_d]:  #move up and right
                self.game.move_life(left=False, up=True, right=True, down=True)

            elif keys[pygame.K_s] and keys[pygame.K_a]:  #move down and left
                self.game.move_life(left=True, up=False, right=False, down=True)
            elif keys[pygame.K_s] and keys[pygame.K_d]:  #move down and right
                self.game.move_life(left=False, up=False, right=True, down=True)

                #opposing keys
            if keys[pygame.K_w] and keys[pygame.K_s]:  #move down and left
                self.game.move_life(left=False, up=False, right=False, down=True)
            elif keys[pygame.K_a] and keys[pygame.K_d]:  #move up and right
                self.game.move_life(left=False, up=False, right=False, down=True)

            else:
                self.game.move_life(left=False, up=False, right=False, down=True)

        

            self.game.draw(True)
            self.game.draw_floor()
            pygame.display.update()

def test():
    width, height = 1280, 720
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game")
    game = TheGame(win, width, height)
    game.play()

if __name__ == '__main__':
    test()