import sys
from enum import Enum
from pathlib import Path

import pygame

from game.board import Board
from game.food import Food
from game.obstacle import ObstacleManager
from game.snake import Snake


WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
HIGH_SCORE_FILE = Path("highscore.txt")
DIFFICULTIES = {
    "Easy": {"speed": 6, "obstacles": 1},
    "Medium": {"speed": 8, "obstacles": 2},
    "Hard": {"speed": 10, "obstacles": 3},
}


class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"


def load_high_score():
    if not HIGH_SCORE_FILE.exists():
        HIGH_SCORE_FILE.write_text("0", encoding="utf-8")
        return 0

    try:
        return int(HIGH_SCORE_FILE.read_text(encoding="utf-8").strip())
    except ValueError:
        return 0


def save_high_score(new_score, current_high):
    if new_score <= current_high:
        return current_high

    HIGH_SCORE_FILE.write_text(str(new_score), encoding="utf-8")
    return new_score


def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake(initial_position=(100, 100))
    food = Food(WIDTH, HEIGHT)
    board = Board(WIDTH, HEIGHT)
    obstacle_manager = ObstacleManager(WIDTH, HEIGHT)
    score = 0
    level = 1
    difficulty = "Medium"
    speed = DIFFICULTIES[difficulty]["speed"]
    obstacles = []
    high_score = load_high_score()
    state = GameState.MENU

    def get_obstacle_count():
        return DIFFICULTIES[difficulty]["obstacles"] + max(0, level - 1)

    def reset_game():
        nonlocal score, state, level, speed, obstacles
        snake.reset(initial_position=(100, 100), direction=(20, 0))
        score = 0
        level = 1
        speed = DIFFICULTIES[difficulty]["speed"]
        food.position = food.spawn_food(snake.body, [])
        obstacles = obstacle_manager.spawn_obstacles(snake.body, food.position, get_obstacle_count())
        state = GameState.PLAYING

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if state == GameState.MENU:
                    if event.key == pygame.K_RETURN:
                        reset_game()
                    elif event.key == pygame.K_1:
                        difficulty = "Easy"
                        speed = DIFFICULTIES[difficulty]["speed"]
                    elif event.key == pygame.K_2:
                        difficulty = "Medium"
                        speed = DIFFICULTIES[difficulty]["speed"]
                    elif event.key == pygame.K_3:
                        difficulty = "Hard"
                        speed = DIFFICULTIES[difficulty]["speed"]
                elif state in (GameState.GAME_OVER, GameState.PLAYING) and event.key == pygame.K_r:
                    reset_game()
                elif state in (GameState.GAME_OVER, GameState.PAUSED, GameState.PLAYING) and event.key == pygame.K_ESCAPE:
                    state = GameState.MENU
                elif state == GameState.PLAYING and event.key == pygame.K_p:
                    state = GameState.PAUSED
                elif state == GameState.PAUSED and event.key == pygame.K_p:
                    state = GameState.PLAYING
                elif state == GameState.PLAYING:
                    snake.handle_input(event)

        if state == GameState.PLAYING:
            snake.move()
            if snake.check_collision(food.get_position()):
                snake.grow()
                score += 1
                level = 1 + score // 5
                speed = DIFFICULTIES[difficulty]["speed"] + (level - 1)
                food.position = food.spawn_food(snake.body, obstacles)
                obstacles = obstacle_manager.spawn_obstacles(snake.body, food.position, get_obstacle_count())

            if (
                snake.check_wall_collision(WIDTH, HEIGHT)
                or snake.check_self_collision()
                or snake.body[0] in obstacles
            ):
                state = GameState.GAME_OVER
                high_score = save_high_score(score, high_score)

        board.draw_board(window, snake, food, obstacles, score, high_score, level, difficulty, state.value)
        pygame.display.flip()
        if state == GameState.PLAYING:
            clock.tick(speed)
        else:
            clock.tick(10)


if __name__ == "__main__":
    main()