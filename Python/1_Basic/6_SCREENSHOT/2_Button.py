from PIL import Image
import pyautogui as pag
import time
import pygame

pygame.init()                                   # Create Game Window
screen = pygame.display.set_mode((10,10))       # Window size
pygame.display.set_caption("Screenshot")        # Window name

filepath = '/Users/vision/academy/python/Python_HG/Screenshot/images'

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(f"{filepath}/image{curr_time}.png")

running = True                                  # Program running flag
while running:                                  # Loop in running is True

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL :
                screenshot()
            elif event.key == pygame.K_LSHIFT:
                running = False

pygame.quit()                                  # Quit game