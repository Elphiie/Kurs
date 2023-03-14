from game import Game

import pygame
import neat
import os
import time
import pickle
import math
import visualize

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


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True       

            if draw:
                self.game.draw(draw_score=True)


            if game_info.score_1 >= 100 or game_info.score_2 >= 100 or game_info.score_1 <= -100 or game_info.score_2 <= -100:
                self.calculate_fitness(game_info, duration)
                break
                          
        return False

    def move_ai(self, net1, net2):
        players = [(self.genome1, net1, self.life_1, True), (self.genome2, net2, self.life_2, False)]
        
        for (genome, net, life, cum) in players:
            dist_food = math.dist((life.x, life.y), (self.food.x, self.food.y)) - (self.food.RADIUS * 2)
            output = net.activate(
                (
                life.x,
                dist_food,
                life.y,
                    )
                )
            decision = output.index(max(output))

            valid = True
            if decision == 0:  # Don't move
                valid = self.game.move_life(False, False, False, False, cum=cum)
                genome.fitness -= 100
                life.NRG -= 1
                  # we want to discourage this
            elif decision == 1:  # Move up
                valid = self.game.move_life(down=False, up=True, right=False, left=False, cum=cum)
                life.NRG -= 2
            elif decision == 2:  # Move down
                valid = self.game.move_life(up=False, right=False, left=False, down=True, cum=cum)
                life.NRG -= 2
            elif decision == 3:  # Move left
                valid = self.game.move_life(left=True, up=False, down=False, right=False, cum=cum)
                life.NRG -= 2
            elif decision == 4:  # Move right
                valid = self.game.move_life(up=False, down=False, right=True, left=False, cum=cum)
                life.NRG -= 2

            if not valid:  # If the movement makes the paddle go off the screen punish the AI
                genome.fitness -= 100  

            if life.NRG <= 0:
                genome.fitness -= 500

                       
            if dist_food <= life.WIDTH + (self.food.RADIUS * 2.5):
                genome.fitness += 5
            elif dist_food <= life.WIDTH + (self.food.RADIUS * 3):
                genome.fitness += 1   
            

                        
                              
 

    def calculate_fitness(self, game_info, duration):
        self.genome1.fitness += game_info.score_1 + duration
        self.genome2.fitness += game_info.score_2 + duration

    


def eval_genomes(genomes, config):
    start_time = time.time()
    width, height = 1280, 720
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Ai-test")

    node_names = {
                -7: 'energy',
                -6: 'pos x',
                -5: 'food rel x',
                -4: 'food y',
                -3: 'pos y',
                -2: 'food rel y',
                -1: 'food x',
                0: 'stop',
                1: 'up',
                2: 'down',
                3: 'left',
                4: 'right'
                }

    for i, (genome_id1, genome1) in enumerate(genomes):
        print(round(i/len(genomes) * 100), end=" ")
        genome1.fitness = 0
        gol = GoL(win, width, height)
        for genome_id2, genome2 in genomes[min(i+1, len(genomes) - 1):]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            

        force_quit = gol.train_ai(genome1, genome2, config, duration=time.time()-start_time, draw=True)
        if force_quit:
            # visualize.draw_net(config, genome1, True, '1', node_names=node_names)

            # visualize.draw_net(config, genome2, True, '2', node_names=node_names)

            quit()



def run_neat(config):
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-57')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))


    winner = p.run(eval_genomes, 100)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)
    
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)

        

    node_names = {
                -7: 'energy',
                -6: 'pos x',
                -5: 'food rel x',
                -4: 'food y',
                -3: 'pos y',
                -2: 'food rel y',
                -1: 'food x',
                0: 'stop',
                1: 'up',
                2: 'down',
                3: 'left',
                4: 'right'
                }
    

    visualize.draw_net(config, winner, True, node_names=node_names)

    visualize.plot_stats(stats, ylog=False, view=True)

    visualize.plot_species(stats, view=True)
        
    
def test(config):
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    width, height = 1280, 720
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("The Game of Kinda-Life")
    gol = GoL(win, width, height)
    gol.test_ai(winner_net)



if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    # mp.set_start_method('spawn')
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)


    # spawn()
    run_neat(config)
    # test(config)