import pygame
import sys

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                circle_color = COLOR_A
                print("Key 'A' pressed: Circle color is now BLUE")
            elif event.key == pygame.K_b:
                circle_color = COLOR_B
                print("Key 'B' pressed: Circle color is now GREEN")
            elif event.key == pygame.K_c:
                circle_color = COLOR_C
                print("Key 'C' pressed: Circle color is now ORANGE")
            
            elif event.key == pygame.K_r:
                circle_radius = 50
                circle_color = DEFAULT_COLOR
                circle_x = SCREEN_WIDTH // 2
                circle_y = SCREEN_HEIGHT // 2
                print("Key 'R' pressed: Resetting circle")

            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    circle_x += speed_x
    circle_y += speed_y

    if circle_x + circle_radius >= SCREEN_WIDTH or circle_x - circle_radius <= 0:
        speed_x *= -1  

    if circle_y + circle_radius >= SCREEN_HEIGHT or circle_y - circle_radius <= 0:
        speed_y *= -1  
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        circle_x -= player_speed
    if keys[pygame.K_RIGHT]:
        circle_x += player_speed
    if keys[pygame.K_UP]:
        circle_y -= player_speed
    if keys[pygame.K_DOWN]:
        circle_y += player_speed

    if keys[pygame.K_KP_PLUS] or keys[pygame.K_PLUS] or keys[pygame.K_EQUALS]:
        circle_radius += 2
    if keys[pygame.K_KP_MINUS] or keys[pygame.K_MINUS]:
        circle_radius -= 2

    if circle_radius < 5:
        circle_radius = 5
    if circle_radius > 150:
        circle_radius = 150

    screen.fill(WHITE)

    pygame.draw.circle(screen, circle_color, (int(circle_x), int(circle_y)), circle_radius)

    pygame.display.flip()
    clock.tick(FPS)
