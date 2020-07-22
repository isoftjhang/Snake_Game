import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_board(self, window, snake, food, obstacles, score, high_score, level, difficulty, state):
        window.fill((10, 10, 20))

        for x in range(0, self.width, 20):
            pygame.draw.line(window, (40, 40, 60), (x, 0), (x, self.height))
        for y in range(0, self.height, 20):
            pygame.draw.line(window, (40, 40, 60), (0, y), (self.width, y))

        if state != "menu":
            for segment in snake.body:
                pygame.draw.rect(window, (0, 220, 90), (*segment, 20, 20))

            for obstacle in obstacles:
                pygame.draw.rect(window, (200, 200, 50), (*obstacle, 20, 20))

            pygame.draw.rect(window, (255, 80, 80), (*food.get_position(), 20, 20))

        font = pygame.font.SysFont("consolas", 24)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        level_text = font.render(f"Level: {level}", True, (255, 255, 255))
        high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        difficulty_text = font.render(f"Difficulty: {difficulty}", True, (255, 255, 255))
        window.blit(score_text, (10, 10))
        window.blit(level_text, (10, 40))
        window.blit(high_score_text, (10, 70))
        window.blit(difficulty_text, (10, 100))

        if state == "paused":
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            window.blit(overlay, (0, 0))
            pause_text = font.render("Paused", True, (255, 255, 255))
            resume_text = font.render("Press P to resume", True, (255, 255, 255))
            window.blit(pause_text, (self.width // 2 - 50, self.height // 2 - 20))
            window.blit(resume_text, (self.width // 2 - 110, self.height // 2 + 20))
        elif state == "game_over":
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            window.blit(overlay, (0, 0))
            game_over_text = font.render("Game Over", True, (255, 255, 255))
            restart_text = font.render("Press R to restart", True, (255, 255, 255))
            window.blit(game_over_text, (self.width // 2 - 80, self.height // 2 - 20))
            window.blit(restart_text, (self.width // 2 - 100, self.height // 2 + 20))
        elif state == "menu":
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 220))
            window.blit(overlay, (0, 0))
            title_text = font.render("Snake Game", True, (255, 255, 255))
            start_text = font.render("Press ENTER to start", True, (255, 255, 255))
            help_text = font.render("Use ARROW KEYS to move, P to pause", True, (255, 255, 255))
            difficulty_text = font.render("Select 1:Easy 2:Medium 3:Hard", True, (255, 255, 255))
            window.blit(title_text, (self.width // 2 - 70, self.height // 2 - 80))
            window.blit(start_text, (self.width // 2 - 120, self.height // 2 - 40))
            window.blit(help_text, (self.width // 2 - 190, self.height // 2))
            window.blit(difficulty_text, (self.width // 2 - 230, self.height // 2 + 40))