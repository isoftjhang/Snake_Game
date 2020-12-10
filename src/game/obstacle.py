import random


class ObstacleManager:
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        self.obstacles = []

    def spawn_obstacles(self, snake_body, food_position, count):
        self.obstacles = []
        attempts = 0
        # Prevent infinite loops when the board becomes crowded.
        while len(self.obstacles) < count and attempts < 1000:
            x = random.randrange(0, self.board_width, 20)
            y = random.randrange(0, self.board_height, 20)
            position = (x, y)
            if position in snake_body or position == food_position or position in self.obstacles:
                attempts += 1
                continue
            self.obstacles.append(position)
        return self.obstacles

    def get_positions(self):
        return self.obstacles
