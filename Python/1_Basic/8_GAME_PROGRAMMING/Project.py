import os
import random
import pygame

###################################################################################
# Initialize game
pygame.init()

# Set screen
screen_width = 1024
screen_height = 320
screen = pygame.display.set_mode((screen_width, screen_height))

# Set game title
pygame.display.set_caption("Minew")

# FPS (Frame per Second)
clock = pygame.time.Clock()
###################################################################################

# User game initialize
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "P_background.png"))

# Character
character = pygame.image.load(os.path.join(image_path, "P_character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 8) - (character_width / 2)
character_y_pos = screen_height - character_height

character_to_y = 0

character_speed = 0.6

# Bullet
bullet = pygame.image.load(os.path.join(image_path, "P_bullet.png"))
bullet_size = bullet.get_rect().size
bullet_width = bullet_size[0]
# bullet_height = bullet_size[1]

bullets = []

bullet_speed = 10

# Enemy
enemy = pygame.image.load(os.path.join(image_path, "P_enemy.png"))
enemy_size = enemy.get_rect().size

enemy_images = [
    pygame.image.load(os.path.join(image_path, "P_enemy.png")),
    pygame.image.load(os.path.join(image_path, "P_enemy_2.png")),
    pygame.image.load(os.path.join(image_path, "P_enemy_3.png"))
]

enemy_speed_x = 3

enemies = []

enemies.append({
    "pos_x" : (screen_width) - enemy_size[0],
    "pos_y" : random.randint(0, screen_height - enemy_size[1]),
    "img_idx" : 0,
    "to_x" : enemy_speed_x,
    "to_y" : 0
})
enemies.append({
    "pos_x" : (screen_width) - enemy_size[0],
    "pos_y" : random.randint(0, screen_height - enemy_size[1]),
    "img_idx" : 0,
    "to_x" : enemy_speed_x,
    "to_y" : 0
})
enemies.append({
    "pos_x" : (screen_width) - enemy_size[0],
    "pos_y" : random.randint(0, screen_height - enemy_size[1]),
    "img_idx" : 0,
    "to_x" : enemy_speed_x,
    "to_y" : 0
})
enemies.append({
    "pos_x" : (screen_width) - enemy_size[0],
    "pos_y" : random.randint(0, screen_height - enemy_size[1]),
    "img_idx" : 0,
    "to_x" : enemy_speed_x,
    "to_y" : 0
})

# Remove bullets
bullet_to_remove = -1
enemy_to_remove = -1

# Config
game_font = pygame.font.Font(None, 40)

total_time = 100

start_ticks = pygame.time.get_ticks()

running = True
while running:
    frame = clock.tick(60)  #60~100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                character_to_y -= character_speed
            elif event.key == pygame.K_SPACE:
                bullet_x_pos = character_x_pos + (character_width)
                bullet_y_pos = character_y_pos - (character_height / 2)
                bullets.append([bullet_x_pos, bullet_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                character_to_y = 0

    # Character position
    character_to_y += 0.01
    character_y_pos += character_to_y * frame

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # Bullets position
    bullets = [[b[0] + bullet_speed, b[1]] for b in bullets]
    bullets = [[b[0], b[1]] for b in bullets if b[0] < 1024]

    # Enemies position
    for enemy_idx, enemy_val in enumerate(enemies) :
        enemy_x_pos = enemy_val["pos_x"]
        enemy_y_pos = enemy_val["pos_y"]
        enemy_img_idx = enemy_val["img_idx"]

        enemy_size = enemy_images[enemy_img_idx].get_rect().size
        enemy_width = enemy_size[0]
        enemy_height = enemy_size[1]

        if enemy_x_pos < 0:
            enemy_val["pos_x"] = screen_width
        
        enemy_val["pos_x"] -= enemy_val["to_x"]

    # Collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for enemy_idx, enemy_val in enumerate(enemies):
        enemy_x_pos = enemy_val["pos_x"]
        enemy_y_pos = enemy_val["pos_y"]
        enemy_img_idx = enemy_val["img_idx"]

        enemy_rect = enemy_images[enemy_img_idx].get_rect()
        enemy_rect.left = enemy_x_pos
        enemy_rect.top = enemy_y_pos

        # enemy vs character
        if character_rect.colliderect(enemy_rect):
            running = False
            game_result = "Game Over"
            break

        # enemy vs bullets
        for bullet_idx, bullet_val in enumerate(bullets):
            bullet_x_pos = bullet_val[0]
            bullet_y_pos = bullet_val[1]

            #bullet's rect(virture box) update
            bullet_rect = bullet.get_rect()
            bullet_rect.left = bullet_x_pos
            bullet_rect.top = bullet_y_pos

            # Check Collision with enemy
            if bullet_rect.colliderect(enemy_rect):
                bullet_to_remove = bullet_idx
                enemy_to_remove = enemy_idx

                # Change enemy status
                if enemy_img_idx < 2 :
                    enemy_width = enemy_rect.size[0]
                    enemy_height = enemy_rect.size[1]

                    next_enemy_rect = enemy_images[enemy_img_idx+1].get_rect()
                    next_enemy_width = next_enemy_rect.size[0]
                    next_enemy_height = next_enemy_rect.size[1]

                    # Enemy Change
                    enemies.append({
                        "pos_x" : enemy_x_pos,
                        "pos_y" : enemy_y_pos,
                        "img_idx" : enemy_img_idx + 1,
                        "to_x" : enemy_speed_x * 1.5,
                        "to_y" : 0
                    })

                break
        else:
            continue
        break

    # Remove collided bullets ans enemies
    if enemy_to_remove > -1 :
        del enemies[enemy_to_remove]
        enemy_to_remove = -1
    
    if bullet_to_remove > -1:
        del bullets[bullet_to_remove]
        bullet_to_remove = -1

    # Print sprites to game window
    screen.blit(background, (0, 0))

    for bullet_x_pos, bullet_y_pos in bullets :
        screen.blit(bullet, (bullet_x_pos, bullet_y_pos))

    for idx, val in enumerate(enemies):
        enemy_x_pos = val["pos_x"]
        enemy_y_pos = val["pos_y"]
        enemy_img_idx = val["img_idx"]
        screen.blit(enemy_images[enemy_img_idx], (enemy_x_pos, enemy_y_pos))

    screen.blit(character, (character_x_pos, character_y_pos))

    # Set timer
    past_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(round((total_time-past_time),2)), True, (255, 255, 255))
    screen.blit(timer, (10,10))

    # Surviving during time end
    if total_time - past_time <= 0 :
        game_result = "Mission Complete ! "
        running = False

    pygame.display.update()

# Win / Lose message
msg = game_font.render(game_result, True, (255, 255, 0))  # 255, 255, 0 => Yellow
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# Quit Game
pygame.time.delay(2000)
pygame.quit()