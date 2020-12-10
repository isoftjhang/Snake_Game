import unittest

from src.game.food import Food
from src.game.obstacle import ObstacleManager
from src.game.snake import Snake


class SnakeGameTests(unittest.TestCase):
    def test_reset_restores_snake_to_initial_state(self):
        snake = Snake(initial_position=(100, 100))
        snake.grow()
        snake.move()
        snake.set_direction((-20, 0))

        snake.reset(initial_position=(40, 40), direction=(20, 0))

        self.assertEqual(snake.body, [(40, 40)])
        self.assertEqual(snake.direction, (20, 0))
        self.assertFalse(snake.grow_pending)

    def test_move_grows_when_growth_is_pending(self):
        snake = Snake(initial_position=(100, 100))
        snake.grow()

        snake.move()

        self.assertEqual(snake.body[0], (120, 100))
        self.assertEqual(len(snake.body), 2)

    def test_food_spawn_avoids_snake_body(self):
        food = Food(board_width=200, board_height=200)
        snake_body = [(0, 0), (20, 0), (40, 0)]

        position = food.spawn_food(snake_body)

        self.assertNotIn(position, snake_body)
        self.assertEqual(position[0] % 20, 0)
        self.assertEqual(position[1] % 20, 0)

    def test_food_spawn_avoids_obstacles(self):
        food = Food(board_width=200, board_height=200)
        snake_body = [(0, 0), (20, 0), (40, 0)]
        obstacles = [(60, 0), (80, 0)]

        position = food.spawn_food(snake_body, obstacles)

        self.assertNotIn(position, snake_body)
        self.assertNotIn(position, obstacles)
        self.assertEqual(position[0] % 20, 0)
        self.assertEqual(position[1] % 20, 0)

    def test_obstacle_spawn_avoids_snake_and_food(self):
        obstacle_manager = ObstacleManager(board_width=200, board_height=200)
        snake_body = [(0, 0), (20, 0), (40, 0)]
        food_position = (60, 0)

        obstacles = obstacle_manager.spawn_obstacles(snake_body, food_position, count=3)

        self.assertEqual(len(obstacles), 3)
        for obstacle in obstacles:
            self.assertNotIn(obstacle, snake_body)
            self.assertNotEqual(obstacle, food_position)
            self.assertEqual(obstacle[0] % 20, 0)
            self.assertEqual(obstacle[1] % 20, 0)

    def test_obstacle_spawns_are_unique(self):
        obstacle_manager = ObstacleManager(board_width=200, board_height=200)
        snake_body = [(0, 0), (20, 0)]
        food_position = (40, 0)

        obstacles = obstacle_manager.spawn_obstacles(snake_body, food_position, count=4)

        self.assertEqual(len(obstacles), len(set(obstacles)))


if __name__ == "__main__":
    unittest.main()
