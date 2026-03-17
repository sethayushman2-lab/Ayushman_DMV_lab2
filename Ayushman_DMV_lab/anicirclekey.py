import pygame
import sys
import matplotlib.pyplot as plt

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
DEFAULT_COLOR = (255, 0, 0)
COLOR_A = (0, 0, 255)
COLOR_B = (0, 255, 0)
COLOR_C = (255, 165, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interactive Animated Circle - DMV Lab")

clock = pygame.time.Clock()

circle_x = SCREEN_WIDTH // 2
circle_y = SCREEN_HEIGHT // 2
circle_radius = 50
circle_color = DEFAULT_COLOR

speed_x = 5
speed_y = 5

player_speed = 7

# Store positions for graph
x_positions = []
y_positions = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                circle_color = COLOR_A
            elif event.key == pygame.K_b:
                circle_color = COLOR_B
            elif event.key == pygame.K_c:
                circle_color = COLOR_C

            elif event.key == pygame.K_r:
                circle_radius = 50
                circle_color = DEFAULT_COLOR
                circle_x = SCREEN_WIDTH // 2
                circle_y = SCREEN_HEIGHT // 2

            elif event.key == pygame.K_ESCAPE:
                running = False

    # Movement
    circle_x += speed_x
    circle_y += speed_y

    # Bounce logic
    if circle_x + circle_radius >= SCREEN_WIDTH or circle_x - circle_radius <= 0:
        speed_x *= -1

    if circle_y + circle_radius >= SCREEN_HEIGHT or circle_y - circle_radius <= 0:
        speed_y *= -1

    # Keyboard movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        circle_x -= player_speed
    if keys[pygame.K_RIGHT]:
        circle_x += player_speed
    if keys[pygame.K_UP]:
        circle_y -= player_speed
    if keys[pygame.K_DOWN]:
        circle_y += player_speed

    # Resize
    if keys[pygame.K_KP_PLUS] or keys[pygame.K_EQUALS]:
        circle_radius += 2
    if keys[pygame.K_KP_MINUS] or keys[pygame.K_MINUS]:
        circle_radius -= 2

    circle_radius = max(5, min(150, circle_radius))

    # Save positions for graph
    x_positions.append(circle_x)
    y_positions.append(circle_y)

    # Drawing
    screen.fill(WHITE)
    pygame.draw.circle(screen, circle_color, (int(circle_x), int(circle_y)), circle_radius)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# 📊 Plot graph after window closes
plt.figure(figsize=(6, 5))
plt.plot(x_positions, y_positions, color='blue')
plt.title("Circle Movement Trajectory")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.xlim(0, SCREEN_WIDTH)
plt.ylim(0, SCREEN_HEIGHT)
plt.gca().invert_yaxis()  # Match pygame coordinate system
plt.grid()
plt.show()