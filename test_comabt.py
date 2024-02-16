import pygame
import sys
import random
from PIL import Image
import testcombat
import main

# Initialisation de Pygame
pygame.init()

from pygame import mixer

# Définition des couleurs
BLANC = (255,   255,   255)
ROUGE = (255,   0,   0)

# Paramètres du jeu
largeur_fenetre =   800
hauteur_fenetre =   600
fps =   30

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Combat Tour par Tour")

# Chargement des images
# Chargement de l'image de fond
fond = pygame.image.load("ressource_graphique/bg/stade.jpg")

# Agrandissement de l'image de fond
largeur_fond =   800  # Largeur désirée pour l'image de fond
hauteur_fond =   500    # Hauteur désirée pour l'image de fond
fond = pygame.transform.scale(fond, (largeur_fond, hauteur_fond))

# Chargement des images des Pokémon
joueur_image = pygame.image.load("ressource_graphique/pokemon/carapuce1.png")
ennemi_image = pygame.image.load("ressource_graphique/pokemon/bulbizarre.png")

# Réduction de la taille des images des Pokémon
largeur_pokemon =   100  # Largeur désirée pour les images des Pokémon
hauteur_pokemon =   100  # Hauteur désirée pour les images des Pokémon
joueur_image = pygame.transform.scale(joueur_image, (largeur_pokemon, hauteur_pokemon))
ennemi_image = pygame.transform.scale(ennemi_image, (largeur_pokemon, hauteur_pokemon))

# Paramètres du joueur et de l'ennemi
vie_joueur =   60
exp_joueur =   0
degats_ennemi =   10
vie_ennemi =   40

# Position du joueur et de l'ennemi
pos_joueur = (200,   350)
pos_ennemi = (500,   120)

# Load the quit button image
quite_button_image = pygame.image.load("ressource_graphique/button/quite.png")

# Scale the quit button image to the desired dimensions
quite_button_width =   50  # Desired width
quite_button_height =   50  # Desired height
quite_button_image = pygame.transform.scale(quite_button_image, (quite_button_width, quite_button_height))

# Position of the quit button
quite_button_x =   700  # Desired x-coordinate
quite_button_y =   50  # Desired y-coordinate

# Define the quit button's rectangle for collision detection
quite_button_rect = quite_button_image.get_rect(topleft=(quite_button_x, quite_button_y))

# Fonction pour afficher le texte à l'écran
def afficher_texte(texte, x, y, taille=30):
    police = pygame.font.SysFont(None, taille)
    texte_affiche = police.render(texte, True, BLANC)
    fenetre.blit(texte_affiche, (x, y))

# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            # Check if the mouse click is within the quit button's rectangle
            if quite_button_rect.collidepoint(event.pos):
                # Handle the quit button click, e.g., return to the main page
                print("Quit button clicked. Returning to main page...")
                # Call the function that starts the main page
                main.main()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Attaque
                vie_ennemi -=   10
                print("bulbizzar attaque carapuce le mettre de hado...")
                if vie_ennemi <=   0:
                    exp_joueur +=   1
                    vie_ennemi =   40
            elif event.key == pygame.K_f:  # Fuite
                pygame.quit()
                sys.exit()

    # Affichage du fond
    fenetre.blit(fond, (0,   0))

    # Affichage du joueur et de l'ennemi
    fenetre.blit(joueur_image, pos_joueur)
    fenetre.blit(ennemi_image, pos_ennemi)

    # Affichage de la vie du joueur et de l'ennemi
    afficher_texte(f"Vie du joueur: {vie_joueur}",   10,   10)
    afficher_texte(f"Vie de l'ennemi: {vie_ennemi}",   10,   50)

    # Affichage de l'expérience du joueur
    afficher_texte(f"Expérience: {exp_joueur}",   600,   10)

    # Affichage du bouton de quitter
    fenetre.blit(quite_button_image, (quite_button_x, quite_button_y))

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Contrôle du taux de rafraîchissement
    pygame.time.Clock().tick(fps)

