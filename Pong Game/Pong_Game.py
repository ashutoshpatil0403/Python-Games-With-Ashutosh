import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong Game')

# Clock
clock = pygame.time.Clock()

# Paddle class
class Paddle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 10

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

# Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-4, 4])

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)

def main():
    run = True
    paddle1 = Paddle(10)
    paddle2 = Paddle(WIDTH - 20)
    ball = Ball()
    score1, score2 = 0, 0
    font = pygame.font.SysFont(None, 35)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1.rect.top > 0:
            paddle1.move(up=True)
        if keys[pygame.K_s] and paddle1.rect.bottom < HEIGHT:
            paddle1.move(up=False)
        if keys[pygame.K_UP] and paddle2.rect.top > 0:
            paddle2.move(up=True)
        if keys[pygame.K_DOWN] and paddle2.rect.bottom < HEIGHT:
            paddle2.move(up=False)

        ball.move()
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.dx *= -1

        if ball.rect.left <= 0:
            score2 += 1
            ball = Ball()
        if ball.rect.right >= WIDTH:
            score1 += 1
            ball = Ball()

        screen.fill(BLACK)
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)
        score_text = font.render(f"{score1} - {score2}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
