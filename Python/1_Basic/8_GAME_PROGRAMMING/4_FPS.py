import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Minew")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\MiNewMW\\Desktop\\Python_AE\\Game\\images\\background.png")

character = pygame.image.load("C:\\Users\\MiNewMW\\Desktop\\Python_AE\\Game\\images\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

character_to_x = 0
character_to_y = 0

character_speed = 0.6

enemy = pygame.image.load("C:\\Users\\MiNewMW\\Desktop\\Python_AE\\Game\\images\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height /2) - (enemy_height /2)

running = True
while running:
    frame = clock.tick(60)  #60~100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_UP:
                character_to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                character_to_y += character_speed

        if event.type == pygame.KEYUP:
            if    event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                character_to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                character_to_y = 0

    character_x_pos += character_to_x * frame
    character_y_pos += character_to_y * frame

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    

    screen.blit(background, (0, 0))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()