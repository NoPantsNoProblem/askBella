import pygame
import sys
import time
from pygame.locals import *

# Set up some constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SNAKE_SIZE = 20

# Define the colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Initialize the game
pygame.init()

# Set up the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

snake = [{'x': WINDOW_WIDTH / 2, 'y': WINDOW_HEIGHT / 2}]
direction = RIGHT
apple = {'x': SNAKE_SIZE * 3, 'y': SNAKE_SIZE * 3}

def draw_snake():
    for coord in snake:
        pygame.draw.rect(window, GREEN, pygame.Rect(coord['x'], coord['y'], SNAKE_SIZE, SNAKE_SIZE))

def draw_apple():
    pygame.draw.rect(window, RED, pygame.Rect(apple['x'], apple['y'], SNAKE_SIZE, SNAKE_SIZE))

def update_snake():
    global snake
    global apple
    global direction
    
    # Check for collision with apple
    if snake[0]['x'] == apple['x'] and snake[0]['y'] == apple['y']:
        apple['x'] = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple['y'] = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
    else:
        del snake[-1] # Remove the tail

    if direction == UP:
        new_head = {'x': snake[0]['x'], 'y': snake[0]['y'] - SNAKE_SIZE}
    elif direction == DOWN:
        new_head = {'x': snake[0]['x'], 'y': snake[0]['y'] + SNAKE_SIZE}
    elif direction == LEFT:
        new_head = {'x': snake[0]['x'] - SNAKE_SIZE, 'y': snake[0]['y']}
    elif direction == RIGHT:
        new_head = {'x': snake[0]['x'] + SNAKE_SIZE, 'y': snake[0]['y']}

    snake.insert(0, new_head) # Add new head

def run_game():
    global direction

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w and direction != DOWN:
                    direction = UP
                elif event.key == K_s and direction != UP:
                    direction = DOWN
                elif event.key == K_a and direction != RIGHT:
                    direction = LEFT
                elif event.key == K_d and direction != LEFT:
                    direction = RIGHT

        window.fill(WHITE)

        draw_snake()
        draw_apple()

        update_snake()

        pygame.display.update()
        time.sleep(0.2) # Delay to slow down the snake

run_game()
