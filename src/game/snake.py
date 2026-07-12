import pygame


class Snake:
    def __init__(self, initial_position):
        self.body = [initial_position]
        self.direction = (20, 0)
        self.grow_pending = False

    def reset(self, initial_position, direction=(20, 0)):
        self.body = [initial_position]
        self.direction = direction
        self.grow_pending = False

    def set_direction(self, direction):
        self.direction = direction

    def handle_input(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP and self.direction != (0, 20):
            self.direction = (0, -20)
        elif event.key == pygame.K_DOWN and self.direction != (0, -20):
            self.direction = (0, 20)
        elif event.key == pygame.K_LEFT and self.direction != (20, 0):
            self.direction = (-20, 0)
        elif event.key == pygame.K_RIGHT and self.direction != (-20, 0):
            self.direction = (20, 0)

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body = [new_head] + self.body
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False

    def grow(self):
        self.grow_pending = True

    def check_collision(self, position):
        return self.body[0] == position

    def check_wall_collision(self, width, height):
        x, y = self.body[0]
        return x < 0 or x >= width or y < 0 or y >= height

    def check_self_collision(self):
        return self.body[0] in self.body[1:]