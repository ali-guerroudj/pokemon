import random

# Définition de la classe Pokemon
class Pokemon:
    def __init__(self, nom, points_de_vie, attaque):
        # Initialisation des attributs du Pokémon
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque

    def attaquer(self, adversaire):
        # Méthode pour attaquer un adversaire
        degats = random.randint(1, self.attaque)
        adversaire.subir_degats(degats)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts!")

    def subir_degats(self, degats):
        # Méthode pour subir des dégâts
        self.points_de_vie -= degats
        if self.points_de_vie < 0:
            self.points_de_vie = 0
        print(f"{self.nom} a maintenant {self.points_de_vie} points de vie.")

# Création de deux Pokémon
pikachu = Pokemon("Pikachu", 100, 20)
bulbizarre = Pokemon("Bulbizarre", 120, 15)

# Combat
tour = 1
while pikachu.points_de_vie > 0 and bulbizarre.points_de_vie > 0:
    print(f"\nTour {tour}")
    pikachu.attaquer(bulbizarre)
    if bulbizarre.points_de_vie <= 0:
        print(f"{bulbizarre.nom} a été vaincu!")
        break

    bulbizarre.attaquer(pikachu)
    if pikachu.points_de_vie <= 0:
        print(f"{pikachu.nom} a été vaincu!")
        break

    tour += 1
import random

# Définition de la classe Pokemon
class Pokemon:
    def __init__(self, nom, points_de_vie, attaque):
        # Initialisation des attributs du Pokémon
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque

    def attaquer(self, adversaire):
        # Méthode pour attaquer un adversaire
        degats = random.randint(1, self.attaque)
        adversaire.subir_degats(degats)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts!")

    def subir_degats(self, degats):
        # Méthode pour subir des dégâts
        self.points_de_vie -= degats
        if self.points_de_vie < 0:
            self.points_de_vie = 0
        print(f"{self.nom} a maintenant {self.points_de_vie} points de vie.")

# Création de deux Pokémon
pikachu = Pokemon("Pikachu", 100, 20)
bulbizarre = Pokemon("Bulbizarre", 120, 15)

# Combat
tour = 1
while pikachu.points_de_vie > 0 and bulbizarre.points_de_vie > 0:
    print(f"\nTour {tour}")
    pikachu.attaquer(bulbizarre)
    if bulbizarre.points_de_vie <= 0:
        print(f"{bulbizarre.nom} a été vaincu!")
        break

    bulbizarre.attaquer(pikachu)
    if pikachu.points_de_vie <= 0:
        print(f"{pikachu.nom} a été vaincu!")
        break

    tour += 1



