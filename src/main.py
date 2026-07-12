import sys

import pygame

from game.board import Board
from game.food import Food
from game.snake import Snake


WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20


def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake(initial_position=(100, 100))
    food = Food(WIDTH, HEIGHT)
    board = Board(WIDTH, HEIGHT)
    score = 0
    game_over = False

    def reset_game():
        nonlocal score, game_over
        snake.reset(initial_position=(100, 100), direction=(20, 0))
        food.position = food.spawn_food(snake.body)
        score = 0
        game_over = False

    reset_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
                continue
            snake.handle_input(event)

        if not game_over:
            snake.move()
            if snake.check_collision(food.get_position()):
                snake.grow()
                score += 1
                food.position = food.spawn_food(snake.body)

            if snake.check_wall_collision(WIDTH, HEIGHT) or snake.check_self_collision():
                game_over = True

        board.draw_board(window, snake, food, score, game_over=game_over)
        pygame.display.flip()
        clock.tick(8)


if __name__ == "__main__":
    main()