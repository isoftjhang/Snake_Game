import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_board(self, window, snake, food, score, game_over=False):
        window.fill((10, 10, 20))

        for x in range(0, self.width, 20):
            pygame.draw.line(window, (40, 40, 60), (x, 0), (x, self.height))
        for y in range(0, self.height, 20):
            pygame.draw.line(window, (40, 40, 60), (0, y), (self.width, y))

        for segment in snake.body:
            pygame.draw.rect(window, (0, 220, 90), (*segment, 20, 20))

        pygame.draw.rect(window, (255, 80, 80), (*food.get_position(), 20, 20))

        font = pygame.font.SysFont("consolas", 24)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        window.blit(score_text, (10, 10))

        if game_over:
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            window.blit(overlay, (0, 0))
            game_over_text = font.render("Game Over", True, (255, 255, 255))
            restart_text = font.render("Press R to restart", True, (255, 255, 255))
            window.blit(game_over_text, (self.width // 2 - 80, self.height // 2 - 20))
            window.blit(restart_text, (self.width // 2 - 100, self.height // 2 + 20))