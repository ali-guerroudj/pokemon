import pygame
import sys
import json
import main

def load_pokemon_data():
    with open('pokemon.json', 'r') as file:
        data = json.load(file)
    return data

def run(screen):
    pygame.init()
    pygame.mixer.init()

    SCREEN_WIDTH = 1100
    SCREEN_HEIGHT = 720

    pokemon_data = load_pokemon_data()

    background_image = pygame.image.load('ressource_graphique/bg/pokedex_2d.png')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    logo_image = pygame.image.load('ressource_graphique/button/gauche.png')
    logo_image = pygame.transform.scale(logo_image, (20, 20))
    logo_position = [370, 590]

    second_image = pygame.image.load('ressource_graphique/button/droite.png')
    second_image = pygame.transform.scale(second_image, (20, 20))
    second_image_position = [455, 592]

    retour_button = pygame.image.load('ressource_graphique/button/retour.png')
    retour_button = pygame.transform.scale(retour_button, (60, 60))
    retour_button_position = [980, 528]

    retour_button_rect = retour_button.get_rect(topleft=retour_button_position)

    click_sound = pygame.mixer.Sound('musique/validation.mp3')
    exit_sound = pygame.mixer.Sound('musique/validation.mp3')
    arrow_click_sound = pygame.mixer.Sound('musique/bip.mp3')

    message_box = pygame.Surface((500, 300))
    message_box_position = [590, 200]
    message_box.fill((0, 0, 0))

    font = pygame.font.Font(None, 24)

    current_pokemon_index = 0

    num_rows = 3  # Nombre de rangées à afficher
    row_height = 50  # Hauteur de chaque rangée
    max_attributes_per_row = len(pokemon_data[0]) // num_rows
    horizontal_spacing = 10  # Espacement horizontal entre chaque attribut

    # Charger les images des Pokémon
    pokemon_images = []
    for pokemon in pokemon_data:
        image_path = f"ressource_graphique/pokemon/{pokemon['nom']}.png"
        pokemon_image = pygame.image.load(image_path)
        pokemon_image = pygame.transform.scale(pokemon_image, (100, 100))  # Ajuster la taille de l'image
        pokemon_images.append(pokemon_image)

    show_retour_button = True  # Variable pour contrôler l'affichage du bouton retour
    last_toggle_time = pygame.time.get_ticks()  # Temps du dernier changement d'affichage

    logo_visible = True  # Variable pour contrôler la visibilité de l'image gauche.png
    logo_last_toggle_time = pygame.time.get_ticks()  # Temps du dernier changement d'affichage de l'image gauche.png

    second_image_visible = True  # Variable pour contrôler la visibilité de l'image droite.png
    second_image_last_toggle_time = pygame.time.get_ticks()  # Temps du dernier changement d'affichage de l'image droite.png

    run = True
    while run:
        current_time = pygame.time.get_ticks()  # Temps actuel
        if current_time - last_toggle_time > 300:  # Si plus de 300 millisecondes se sont écoulées depuis le dernier changement
            show_retour_button = not show_retour_button  # Inverser l'état de l'affichage du bouton retour
            last_toggle_time = current_time  # Mettre à jour le temps du dernier changement

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_sound.play()
                pygame.time.wait(int(exit_sound.get_length() * 1000))
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if retour_button_rect.collidepoint(event.pos):
                    click_sound.play()
                    pygame.time.wait(int(click_sound.get_length() * 1000))
                    main.main()
                elif pygame.Rect(logo_position, logo_image.get_size()).collidepoint(event.pos):
                    arrow_click_sound.play()
                    current_pokemon_index = (current_pokemon_index - 1) % len(pokemon_data)
                    logo_visible = False  # Cacher l'image gauche.png après un clic
                    logo_last_toggle_time = current_time  # Mettre à jour le temps du dernier changement de visibilité de l'image gauche.png
                elif pygame.Rect(second_image_position, second_image.get_size()).collidepoint(event.pos):
                    arrow_click_sound.play()
                    current_pokemon_index = (current_pokemon_index + 1) % len(pokemon_data)
                    second_image_visible = False  # Cacher l'image droite.png après un clic
                    second_image_last_toggle_time = current_time  # Mettre à jour le temps du dernier changement de visibilité de l'image droite.png

        screen.blit(background_image, (0, 0))

        if logo_visible:
            screen.blit(logo_image, logo_position)
        if second_image_visible:
            screen.blit(second_image, second_image_position)

        screen.blit(message_box, message_box_position)

        pokemon = pokemon_data[current_pokemon_index]
        attribute_texts = [f"{key.capitalize()}: {value}" for key, value in pokemon.items()]
        
        # Affichage des attributs en rangées
        for i in range(num_rows):
            start_index = i * max_attributes_per_row
            end_index = min((i + 1) * max_attributes_per_row, len(attribute_texts))
            row_attributes = attribute_texts[start_index:end_index]
            row_y = message_box_position[1] + i * row_height

            for j, attribute_text in enumerate(row_attributes):
                text_surface = font.render(attribute_text, True, (255, 255, 255))
                text_x = message_box_position[0] + j * (500 // max_attributes_per_row + horizontal_spacing)
                screen.blit(text_surface, (text_x, row_y))

        # Affichage de l'image du Pokémon à gauche du Pokédex
        pokemon_image = pokemon_images[current_pokemon_index]
        pokemon_image_x = 210  # Ajustez cette valeur pour décaler l'image vers la droite
        pokemon_image_y = SCREEN_HEIGHT // 2 - pokemon_image.get_height() // 2
        screen.blit(pokemon_image, (pokemon_image_x, pokemon_image_y))

        # Vérifier si l'image gauche.png doit être affichée ou non
        if not logo_visible:
            current_time = pygame.time.get_ticks()
            if current_time - logo_last_toggle_time > 100:  # Si plus de 300 millisecondes se sont écoulées depuis le dernier changement de visibilité
                logo_visible = True  # Afficher à nouveau l'image gauche.png
                logo_last_toggle_time = current_time  # Mettre à jour le temps du dernier changement de visibilité de l'image gauche.png

        # Vérifier si l'image droite.png doit être affichée ou non
        if not second_image_visible:
            current_time = pygame.time.get_ticks()
            if current_time - second_image_last_toggle_time > 100:  # Si plus de 300 millisecondes se sont écoulées depuis le dernier changement de visibilité
                second_image_visible = True  # Afficher à nouveau l'image droite.png
                second_image_last_toggle_time = current_time  # Mettre à jour le temps du dernier changement de visibilité de l'image droite.png

        # Affichage du bouton retour
        if show_retour_button:
            screen.blit(retour_button, retour_button_position)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1100, 720))
    pygame.display.set_caption("Pokédex")
    run(screen)







































