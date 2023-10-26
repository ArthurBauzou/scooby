import pygame
import random

# Initialisation
pygame.init()

# Taille de l'écran
largeur_ecran = 600
hauteur_ecran = 400

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)

# Dimention d'une cellule   ### AHAHAHA IL A FAIT UNE FAUTE GPT A FAIT UNE FAAAAAUTE LE NUUUUUUL
taille_cellule = 20

# Création de l'écran
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Définir la vitesse du jeu
vitesse = 10

font_style = pygame.font.SysFont(None, 30)

# Afficher le score
def afficher_score(score):
    score_surface = font_style.render("Score: " + str(score), True, noir)
    ecran.blit(score_surface, [0, 0])

# Afficher le serpent
def afficher_serpent(taille_serpent, liste_serpent):
    for i in liste_serpent:
        pygame.draw.rect(ecran, noir, [i[0], i[1], taille_cellule, taille_cellule])

# Fonction principale du jeu
def jeu_snake():
    game_over = False
    fin_jeu = False

    # Position initiale du serpent
    x_serpent = largeur_ecran / 2
    y_serpent = hauteur_ecran / 2

    # Vitesse initiale du serpent
    dx_serpent = 0
    dy_serpent = 0

    # Taille initiale du serpent
    taille_serpent = 1
    liste_serpent = []
    longueur_serpent = 1

    # Position initiale de la pomme
    x_pomme = round(random.randrange(0, largeur_ecran - taille_cellule) / 20.0) * 20
    y_pomme = round(random.randrange(0, hauteur_ecran - taille_cellule) / 20.0) * 20

    # Boucle principale du jeu
    while not game_over:

        while fin_jeu == True:
            ecran.fill(blanc)
            message = font_style.render("Appuyez sur Espace pour rejouer ou sur Echap pour quitter.", True, noir)
            ecran.blit(message, [largeur_ecran / 6, hauteur_ecran / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        fin_jeu = False
                    if event.key == pygame.K_SPACE:
                        jeu_snake()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx_serpent = -taille_cellule
                    dy_serpent = 0
                elif event.key == pygame.K_RIGHT:
                    dx_serpent = taille_cellule
                    dy_serpent = 0
                elif event.key == pygame.K_UP:
                    dy_serpent = -taille_cellule
                    dx_serpent = 0
                elif event.key == pygame.K_DOWN:
                    dy_serpent = taille_cellule
                    dx_serpent = 0

        if x_serpent >= largeur_ecran or x_serpent < 0 or y_serpent >= hauteur_ecran or y_serpent < 0:
            fin_jeu = True

        x_serpent += dx_serpent
        y_serpent += dy_serpent
        ecran.fill(blanc)
        pygame.draw.rect(ecran, rouge, [x_pomme, y_pomme, taille_cellule, taille_cellule])
        serpent_tete = []
        serpent_tete.append(x_serpent)
        serpent_tete.append(y_serpent)
        liste_serpent.append(serpent_tete)
        if len(liste_serpent) > longueur_serpent:
            del liste_serpent[0]

        for x in liste_serpent[:-1]:
            if x == serpent_tete:
                fin_jeu = True

        afficher_serpent(taille_serpent, liste_serpent)
        afficher_score(taille_serpent - 1)

        pygame.display.update()

        if x_serpent == x_pomme and y_serpent == y_pomme:
            x_pomme = round(random.randrange(0, largeur_ecran - taille_cellule) / 20.0) * 20
            y_pomme = round(random.randrange(0, hauteur_ecran - taille_cellule) / 20.0) * 20
            longueur_serpent += 1

        clock.tick(vitesse)

    pygame.quit()

jeu_snake()