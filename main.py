import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Размер ракеток и мяча
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пин-понг на Algo VSCode")

# Создаем шрифт
font = pygame.font.SysFont(None, 36)

# Начальные позиции ракеток
p1_y = p2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Позиции мяча
ball_x, ball_y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
ball_dx, ball_dy = 5, 5

clock = pygame.time.Clock()

# Основной цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка клавиш
    keys = pygame.key.get_pressed()
    # Для Игрока 1 (левый) W/S
    if keys[pygame.K_w] and p1_y > 0:
        p1_y -= 5
    if keys[pygame.K_s] and p1_y < HEIGHT - PADDLE_HEIGHT:
        p1_y += 5
    # Для Игрока 2 (правый) UP/DOWN
    if keys[pygame.K_UP] and p2_y > 0:
        p2_y -= 5
    if keys[pygame.K_DOWN] and p2_y < HEIGHT - PADDLE_HEIGHT:
        p2_y += 5

    # Обновление позиции мяча
    ball_x += ball_dx
    ball_y += ball_dy

    # Отскок от верхней и нижней границы
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_dy *= -1

    # Отскок от ракеток
    # Левая ракетка
    if (ball_x <= PADDLE_WIDTH and p1_y < ball_y < p1_y + PADDLE_HEIGHT):
        ball_dx *= -1
    # Правая ракетка
    if (ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and p2_y < ball_y < p2_y + PADDLE_HEIGHT):
        ball_dx *= -1

    # Проверка выхода мяча за границы
    if ball_x < 0 or ball_x > WIDTH:
        # сброс мяча в центр
        ball_x, ball_y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_dx *= -1

    # Рисуем
    screen.fill(BLACK)
    # Ракетки
    pygame.draw.rect(screen, WHITE, (0, p1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, p2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    # Мяч
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    # Очки (можно добавить и усложнить)
    # Отобразить счет (по желанию)
    
    pygame.display.flip()
    clock.tick(60)
