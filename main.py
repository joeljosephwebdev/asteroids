import pygame
import time
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game_clock = pygame.time.Clock()
    dt = 0
    score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()



    # Define font and size
    title_font = pygame.font.Font(None, 74)  # None uses the default font, 74 is the font size
    subtitle_font = pygame.font.Font(None, 28)  # None uses the default font, 74 is the font size

    # Define text and color
    title_text = "Asteroids"
    subtitle_text = "Press enter to begin."
    text_color = (255, 255, 255)  # White color

    # Render the text
    title_text_surface = title_font.render(title_text, True, text_color)
    subtitle_text_surface = subtitle_font.render(subtitle_text, True, text_color)

    # Get the size of the text surface
    title_text_rect = title_text_surface.get_rect()
    subtitle_text_rect = subtitle_text_surface.get_rect()

    # Calculate the position to center the text
    title_text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100)
    subtitle_text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Set up the flashing effect
    last_flash_time = time.time()  # Track the last time the text was toggled
    text_visible = True  # Initially show the text

    #Title screen loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Break loop and start game if player pressed ENTER
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            time.sleep(0.5)
            break

        # Fill the screen with a color
        screen.fill((0, 0, 0))  # Black background

        # Blit the text surface onto the screen
        screen.blit(title_text_surface, title_text_rect)

        current_time = time.time()

        # Check if it's time to toggle the text visibility
        if current_time - last_flash_time > TEXT_FLASH_INTERVAL:
            text_visible = not text_visible  # Toggle visibility
            last_flash_time = current_time  # Update last flash time

        if text_visible:
            screen.blit(subtitle_text_surface, subtitle_text_rect) # Show flasing text

        # Update the display
        pygame.display.flip()

        # Frame rate control
        pygame.time.Clock().tick(60) / 1000

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.checkCollision(player) == True:
                print("Game Over \nScore:", score)
                return

        for asteroid in asteroids:
            for shot in shots:
                if shot.checkCollision(asteroid):
                    shot.kill()
                    score += asteroid.split()

        screen.fill("black")

        for item in drawable:
            item.wrapAround()
            item.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
