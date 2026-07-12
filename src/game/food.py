import random


class Food:
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        self.position = self.spawn_food([])

    def spawn_food(self, snake_body):
        while True:
            x = random.randrange(0, self.board_width, 20)
            y = random.randrange(0, self.board_height, 20)
            if (x, y) not in snake_body:
                self.position = (x, y)
                return self.position

    def get_position(self):
        return self.position