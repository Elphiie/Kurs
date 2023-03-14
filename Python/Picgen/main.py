
from game import Game

import pygame
import neat
import os
import time
import pickle
import math

class GoL:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.life_1 = self.game.life_1
        self.life_2 = self.game.life_2
        self.score_1 = self.game.score_1
        self.score_2 = self.game.score_2
        self.dur = self.game.dur
        self.fps = self.game.fps
        self.raw_dur = self.game.raw_dur
        self.food = self.game.food


    def test_ai(self, net):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            game_info = self.game.loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break


            output = net.activate(
                (self.life_1.x, abs(self.life_1.x - self.food.x), self.food.x, self.life_1.y, abs(self.life_1.y - self.food.y), self.food.y))
            decision = output.index(max(output))

            

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:    #move up
                self.game.move_life(left=False, up=True, right=False, down=False)
            elif keys[pygame.K_s]:  #move down
                self.game.move_life(left=False, up=False, right=False, down=True)
            elif keys[pygame.K_a]:  #move left
                self.game.move_life(left=True, up=False, right=False, down=False)
            elif keys[pygame.K_d]:  #move right
                self.game.move_life(left=False, up=False, right=True, down=False)

                #diagonal movement
            if keys[pygame.K_w] and keys[pygame.K_a]:  #move down and left
                self.game.move_life(left=True, up=True, right=False, down=False)
            elif keys[pygame.K_w] and keys[pygame.K_d]:  #move up and right
                self.game.move_life(left=False, up=True, right=True, down=False)

            elif keys[pygame.K_s] and keys[pygame.K_a]:  #move down and left
                self.game.move_life(left=True, up=False, right=False, down=True)
            elif keys[pygame.K_s] and keys[pygame.K_d]:  #move down and right
                self.game.move_life(left=False, up=False, right=True, down=True)

                #opposing keys
            if keys[pygame.K_w] and keys[pygame.K_s]:  #move down and left
                self.game.move_life(left=False, up=False, right=False, down=False)
            elif keys[pygame.K_a] and keys[pygame.K_d]:  #move up and right
                self.game.move_life(left=False, up=False, right=False, down=False)

        

            self.game.draw(True)
            pygame.display.update()


    def train_ai(self, genome1, genome2, config, duration, draw=False):
        run = True
        start_time = time.time()
        clock = pygame.time.Clock()

        life1 = self.life_1
        life2 = self.life_2     



        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
        self.genome1 = genome1
        self.genome2 = genome2

        while run:
            pygame.display.update()
            clock.tick(6000)
            raw_time = pygame.time.get_ticks()
            fps = clock.get_fps()
            duration = time.time() - start_time
            self.game.fps = round(fps, 2)
            self.game.raw_dur = round(raw_time/1000, 2)
            self.game.dur = round(duration, 2)

            game_info = self.game.loop(duration)

            self.move_ai(net1, net2)

            pos_l1_x = 0
            pos_l1_y = 0
            pos_l2_x = 0
            pos_l2_y = 0

            i = 0
            t_i = i/2

            if pos_l1_x < 1 and pos_l1_y < 1:                    
                pos_l1_x = life1.x
                pos_l1_y = life1.y

            if pos_l2_x < 1 and pos_l2_y < 1:                    
                pos_l2_x = life2.x
                pos_l2_y = life2.y

                if duration >= t_i:
                    
                    d = math.dist((life1.x, life1.y), (pos_l1_x, pos_l1_y))
                    d2 = math.dist((life2.x, life2.y), (pos_l2_x, pos_l2_y))

                    if d + life1.WIDTH <= 100:
                        self.score_1 -= 10
                        pos_l1_x *= 0
                        pos_l1_y *= 0
                                            
                    if d2 + life1.WIDTH <= 100:
                        self.score_2 -= 10
                        pos_l2_x *= 0
                        pos_l2_y *= 0

                    i += 1

                    print('i: ' + str(i) + '\n' + 't_i: ' + str(t_i) + '\n' + 'd1: ' + str(d) + '\n' + 'd2: ' + str(d2))        

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True       

            if draw:
                self.game.draw(draw_score=True)
     
            if game_info.score_1 >= 750 or game_info.score_2 >= 750 or game_info.score_1 <= -1000 or game_info.score_2 <= -1000:
                self.calculate_fitness(game_info, duration)
                break
                          
        return False

    def move_ai(self, net1, net2):
        players = [(self.genome1, net1, self.life_1, True), (self.genome2, net2, self.life_2, False)]
        for (genome, net, life, cum) in players:
            
            output = net.activate(
                (life.x,
                abs(life.x - self.food.x), 
                self.food.x,
                life.y,
                abs(life.y - self.food.y),
                self.food.y,
                math.dist((life.x, life.y), (self.food.x, self.food.y)),
                self.game.window_height,
                abs(life.y - self.game.window_height),
                abs(life.y + self.game.window_height),
                self.game.window_width,
                abs(life.x - self.game.window_width),
                abs(life.x + self.game.window_width),
                self.game.dur
                    )
                )
            decision = output.index(max(output))

            valid = True
            if decision == 0:  # Don't move
                valid = self.game.move_life(False, False, False, False, cum=cum)
                genome.fitness -= 1
                  # we want to discourage this
            elif decision == 1:  # Move up
                valid = self.game.move_life(False, True, False, False, cum=cum)
                genome.fitness += 1
            elif decision == 2:  # Move down
                valid = self.game.move_life(False, False, False, True, cum=cum)
                genome.fitness += 1
            elif decision == 3:  # Move left
                valid = self.game.move_life(True, False, False, False, cum=cum)
                genome.fitness += 1
            elif decision == 4:  # Move right
                valid = self.game.move_life(False, False, True, False, cum=cum)
                genome.fitness += 1
            elif decision == 5:  # Move up and left
                valid = self.game.move_life(True, True, False, False, cum=cum)
                genome.fitness += 1
            elif decision == 6:  # Move up and right
                valid = self.game.move_life(False, True, True, False, cum=cum)
                genome.fitness += 1
            elif decision == 7:  # Move down and left
                valid = self.game.move_life(True, False, False, True, cum=cum)
                genome.fitness += 1
            else:                # Move down and right
                valid = self.game.move_life(False, False, True, True, cum=cum)
                genome.fitness += 1
            if not valid:  # If the movement makes the paddle go off the screen punish the AI
                genome.fitness -= 1000
            

                        
                              
 

    def calculate_fitness(self, game_info, duration):
        self.genome1.fitness += game_info.score_1 - (duration * 20000)
        self.genome2.fitness += game_info.score_2 - (duration * 20000)

    


def eval_genomes(genomes, config):
    start_time = time.time()
    width, height = 1280, 720
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Ai-test")

    for i, (genome_id1, genome1) in enumerate(genomes):
        print(round(i/len(genomes) * 100), end=" ")
        genome1.fitness = 0
        gol = GoL(win, width, height)
        for genome_id2, genome2 in genomes[min(i+1, len(genomes) - 1):]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            

        force_quit = gol.train_ai(genome1, genome2, config, duration=time.time()-start_time, draw=True)
        if force_quit:
            quit()


def run_neat(config):
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-413')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(20))

    winner = p.run(eval_genomes, 10000)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)
    
def test(config):
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    width, height = 1280, 720
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")
    gol = GoL(win, width, height)
    gol.test_ai(winner_net)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    run_neat(config)
    test(config)