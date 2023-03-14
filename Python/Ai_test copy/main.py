import neat
import pygame
import os
import random

# Initialize the NEAT algorithm
local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config.txt')
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
population = neat.Population(config)

def evaluate_genome(genome, config):
    net = neat.nn.FeedForwardNetwork.create(genome, config)

    # Initialize the game
    pygame.init()
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    # Initialize the game objects
    square_size = 20
    square1 = pygame.Rect(0, 0, square_size, square_size)
    square2 = pygame.Rect(screen_width - square_size, screen_height - square_size, square_size, square_size)
    dot_size = 10
    dot = pygame.Rect(0, 0, dot_size, dot_size)
    dot_color = (255, 0, 0)

    # Initialize the fitness score
    fitness = 0

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Move the squares based on the networks' outputs
        inputs = (square1.x, square1.y, square2.x, square2.y, dot.x, dot.y)
        outputs = net.activate(inputs)
        dx1, dy1, dx2, dy2 = outputs
        square1.move_ip(dx1, dy1)
        square2.move_ip(dx2, dy2)

        # Check if the squares hit the walls
        if square1.left < 0 or square1.right > screen_width or square1.top < 0 or square1.bottom > screen_height:
            fitness -= 1
            break
        if square2.left < 0 or square2.right > screen_width or square2.top < 0 or square2.bottom > screen_height:
            fitness -= 1
            break

        # Check if the squares collide
        if square1.colliderect(square2):
            fitness1 = fitness + 10
            fitness2 = fitness - 10
            break

        # Check if the squares find the dot
        if dot.colliderect(square1):
            fitness += 10
            dot.x = random.randint(0, screen_width - dot_size)
            dot.y = random.randint(0, screen_height - dot_size)
        if dot.colliderect(square2):
            fitness += 10
            dot.x = random.randint(0, screen_width - dot_size)
            dot.y = random.randint(0, screen_height - dot_size)

        # Draw the game objects
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), square1)
       
