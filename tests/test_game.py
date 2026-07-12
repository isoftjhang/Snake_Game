import unittest

from src.game.food import Food
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


if __name__ == "__main__":
    unittest.main()
