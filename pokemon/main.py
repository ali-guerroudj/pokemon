import pygame
import sys
import subprocess
import pokedex

pygame.init()
pygame.mixer.init()

def main():
    SCREEN_WIDTH =   1100
    SCREEN_HEIGHT =   720

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pokémon")

    background_image = pygame.image.load('ressource_graphique/bg/bc.jpg')
    button_play = pygame.image.load('ressource_graphique/button/playbutton.png')
    button_quit = pygame.image.load('ressource_graphique/button/quit.png')
    button_pokedex = pygame.image.load('ressource_graphique/button/pokedex.png')

    new_size = (120,   120)
    button_pokedex_resized = pygame.transform.scale(button_pokedex, new_size)

    button_width = max(button_play.get_rect().width, button_quit.get_rect().width, button_pokedex_resized.get_rect().width)
    spacing =   40
    total_button_width = button_width *   3 + spacing *   2
    start_x = ((SCREEN_WIDTH - total_button_width) /   2) +   100

    rect_play = button_play.get_rect(topleft=(start_x, SCREEN_HEIGHT - button_play.get_rect().height -   40))
    rect_quit = button_quit.get_rect(topleft=(start_x + button_width + spacing, SCREEN_HEIGHT - button_quit.get_rect().height -   40))
    rect_pokedex = button_pokedex_resized.get_rect(topleft=(start_x + button_width *   2 + spacing *   2, SCREEN_HEIGHT - button_pokedex_resized.get_rect().height -   40))

    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.fill((0,   0,   0))
    overlay.set_alpha(0)

    last_clicked = None

    pygame.mixer.music.load('musique/music.mp3')
    pygame.mixer.music.play(-1)

    show_text = True
    text_blink_timer =   0
    BLINK_INTERVAL =   500

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect_play.collidepoint(event.pos):
                    last_clicked = 'play'
                    button_play = None
                    pygame.display.quit()
                    subprocess.run(["python", "test_comabt.py"])
                    run = False
                elif rect_quit.collidepoint(event.pos):
                    print("Quitter le jeu!")
                    last_clicked = 'quit'
                    button_quit = None
                    pygame.time.delay(0)
                    for i in range(255, -1, -5):
                        overlay.set_alpha(i)
                        screen.blit(overlay, (0,   0))
                        pygame.display.update()
                        pygame.time.delay(10)
                    run = False
                elif rect_pokedex.collidepoint(event.pos):
                    last_clicked = 'pokedex'
                    button_pokedex = None
                    pygame.mixer.music.stop()
                    pokedex.run(screen)

            elif event.type == pygame.MOUSEBUTTONUP:
                if last_clicked == 'play':
                    button_play = pygame.image.load('ressource_graphique/button/playbutton.png')
                elif last_clicked == 'quit':
                    button_quit = pygame.image.load('ressource_graphique/button/quit.png')
                elif last_clicked == 'pokedex':
                    button_pokedex = pygame.image.load('ressource_graphique/button/pokedex.png')

        screen.blit(background_image, (0,   0))
        if button_play is not None:
            screen.blit(button_play, rect_play)
        if button_quit is not None:
            screen.blit(button_quit, rect_quit)
        if button_pokedex is not None:
            screen.blit(button_pokedex_resized, rect_pokedex)

        font = pygame.font.Font(None,   36)
        current_time = pygame.time.get_ticks()
        if current_time - text_blink_timer >= BLINK_INTERVAL:
            show_text = not show_text
            text_blink_timer = current_time

        if show_text:
            text_surface = font.render("Press button", True, (0,   0,   0))
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH //   2 -   140, SCREEN_HEIGHT //   2 +   160))
            screen.blit(text_surface, text_rect)

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()










