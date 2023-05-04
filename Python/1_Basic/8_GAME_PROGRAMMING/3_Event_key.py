import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Minew")

background = pygame.image.load("C:\\Users\\MiNewMW\\Desktop\\Python_AE\\Game\\images\\background.png")

character = pygame.image.load("C:\\Users\\MiNewMW\\Desktop\\Python_AE\\Game\\images\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

character_to_x = 0
character_to_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                character_to_x -= 5
            elif event.key == pygame.K_d:
                character_to_x += 5
            elif event.key == pygame.K_w:
                character_to_y -= 5
            elif event.key == pygame.K_s:
                character_to_y += 5

        if event.type == pygame.KEYUP:
            if    event.key == pygame.K_a or event.key == pygame.K_d :
                character_to_x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s :
                character_to_y = 0

        character_x_pos += character_to_x
        character_y_pos += character_to_y


    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()