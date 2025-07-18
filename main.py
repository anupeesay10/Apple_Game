import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((350, 600))
clock = pygame.time.Clock()

class Apple:

    def __init__(self, image, position, speed):
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.speed = speed

    def move(self):
        self.rect.y += self.speed


# variables
speed = 3
score = 0
timer = 60.0  # 60 seconds timer
game_over = False

# constants
TILESIZE = 32

# floor
floor_image = pygame.image.load("assets/floor.png").convert_alpha()
floor_image = pygame.transform.scale(floor_image,(TILESIZE*15,TILESIZE*5
                                                  ))
floor_rect = floor_image.get_rect(bottomleft = (0,screen.get_height())) #screen is in the fourth quadrant and y increases on the way down

#player
player_image = pygame.image.load("assets/player_static.png").convert_alpha()
player_image = pygame.transform.scale(player_image,(TILESIZE,TILESIZE*2))
player_rect = player_image.get_rect(center=(screen.get_width()/2, screen.get_height()-floor_image.get_height()-(player_image.get_height()/2)))

# apple
apple_image = pygame.image.load("assets/apple.png").convert_alpha()
apple_image = pygame.transform.scale(apple_image,(TILESIZE,TILESIZE))

apples = [
    Apple(apple_image, (100,0), 3),
    Apple(apple_image, (300,0), 3)
]

# fonts
font = pygame.font.Font('assets/PixeloidMono.ttf', TILESIZE//2)

# sound fx
pickup = pygame.mixer.Sound('assets/powerup.mp3')
pickup.set_volume(0.1)

running = True

def update():
    global speed
    global score
    global timer
    global game_over

    if not game_over:
        # Update timer
        timer -= 1/60  # Decrease by 1/60 second each frame (60 FPS)
        if timer <= 0:
            timer = 0
            game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= 8
        elif keys[pygame.K_RIGHT]:
            player_rect.x += 8

        # apple management
        for apple in apples:
            apple.move()

            if apple.rect.colliderect(floor_rect):
                apples.remove(apple)
                apples.append(Apple(apple_image, (random.randint(50,300), -50),speed))

            elif apple.rect.colliderect(player_rect):
                apples.remove(apple)
                apples.append(Apple(apple_image, (random.randint(50,300), -50),speed))
                speed += 0.1
                score += 1
                pickup.play()



def draw():
    screen.fill('lightblue')
    screen.blit(player_image, player_rect)
    screen.blit(floor_image, floor_rect)

    for apple in apples:
        screen.blit(apple.image, apple.rect)

    score_text = font.render(f"Score: {score}", True, 'white')
    screen.blit(score_text, (5, 5))
    
    # Display timer
    timer_text = font.render(f"Time: {int(timer)}", True, 'white')
    screen.blit(timer_text, (5, 35))
    
    # Display game over message
    if game_over:
        game_over_text = font.render("GAME OVER!", True, 'red')
        text_rect = game_over_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(game_over_text, text_rect)
        
        final_score_text = font.render(f"Final Score: {score}", True, 'red')
        score_rect = final_score_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 30))
        screen.blit(final_score_text, score_rect)

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update()
    draw()


    clock.tick(60)
    pygame.display.update()

