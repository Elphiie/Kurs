# https://neat-python.readthedocs.io/en/latest/xor_example.html
from gen import Game
import pygame
import neat
import os
import time
import pickle


class PongGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.food = self.game.food
        self.life = self.game.life


    def test_ai(self, net):
        """
        Test the AI against a human player by passing a NEAT neural network
        """
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            game_info = self.game.loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            output = net.activate((self.life.y, abs(
                self.life.x - self.food.x), self.food.y))
            decision = output.index(max(output))

            if decision == 1:  # AI moves up
                self.game.move_paddle(left=False, up=True)
            elif decision == 2:  # AI moves down
                self.game.move_paddle(left=False, up=False)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            elif keys[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)



    def train_ai(self, genome1, genome2, config, draw=True):
        """
        Train the AI by passing two NEAT neural networks and the NEAt config object.
        These AI's will play against eachother to determine their fitness.
        """
        run = True
        start_time = time.time()
        clock = pygame.time.Clock()

        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        self.genome1 = genome1

        max_hits = 50

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True

            game_info = self.game.loop()

            self.move_ai_paddles(net1)


            self.game.draw(True)
            pygame.display.update()

            duration = time.time() - start_time
            if game_info.score == 3 or duration >= 10:
                self.calculate_fitness(game_info, duration)
                break

        return False

    def move_ai_paddles(self, net1):
        """
        Determine where to move the left and the right paddle based on the two 
        neural networks that control them. 
        """
        players = [(self.genome1, net1, self.life, True)]
        for (genome, net, paddle, left) in players:
            output = net.activate(
                (paddle.y, abs(paddle.x - self.food.x), self.food.y))
            decision = output.index(max(output))

            valid = True
            if decision == 0:  # Don't move
                genome.fitness -= 0.1  # we want to discourage this
            elif decision == 1:  # Move up
                valid = self.game.move_paddle(left=left, up=True)
            
            elif decision == 2:  # Move down
                valid = self.game.move_paddle(left=left, up=False)
            
            elif decision == 3:
                valid = self.game.move_paddle(left=False, up=False)
            
            else:
                valid = self.game.move_paddle(left=True, up=False)

            if not valid:  # If the movement makes the paddle go off the screen punish the AI
                genome.fitness -= 1

    def calculate_fitness(self, game_info, duration):
        self.genome1.fitness += game_info.score + duration


def eval_genomes(genomes, config):
    """
    Run each genome against eachother one time to determine the fitness.
    """
    width, height = 700, 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")

    for i, (genome_id1, genome1) in enumerate(genomes):
        print(round(i/len(genomes) * 100), end=" ")
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[min(i+1, len(genomes) - 1):]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            pong = PongGame(win, width, height)

            force_quit = pong.train_ai(genome1, genome2, config, draw=True)
            if force_quit:
                quit()


def run_neat(config):
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-7')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


def test_best_network(config):
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    width, height = 700, 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")
    pong = PongGame(win, width, height)
    pong.test_ai(winner_net)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    run_neat(config)
    test_best_network(config)
