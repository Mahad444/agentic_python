# snake game 
import pygame 
import random
import sys
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake and food initialization
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 25)

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def move_snake(snake, direction):
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)
    return snake

def check_collision(snake):
    head = snake[0]
    # Wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    # Self collision
    if head in snake[1:]:
        return True
    return False

def smart_direction(snake, food, current_direction):
    head = snake[0]
    dx = food[0] - head[0]
    dy = food[1] - head[1]
    # Prefer horizontal movement if not blocked
    if dx != 0:
        new_dir = (CELL_SIZE if dx > 0 else -CELL_SIZE, 0)
        next_head = (head[0] + new_dir[0], head[1])
        if next_head not in snake:
            return new_dir
    if dy != 0:
        new_dir = (0, CELL_SIZE if dy > 0 else -CELL_SIZE)
        next_head = (head[0], head[1] + new_dir[1])
        if next_head not in snake:
            return new_dir
    return current_direction

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Smart movement towards food
    direction = smart_direction(snake, food, direction)
    snake = move_snake(snake, direction)

    # Check if snake eats food
    if snake[0] == food:
        score += 1
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        while food in snake:
            food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
    else:
        snake.pop()

    if check_collision(snake):
        break

    draw_snake(snake)
    draw_food(food)
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()