import random

# Initialisation des variables
niveau_vie = 20
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0
numero_combat = 1

# Fonction pour afficher les règles du jeu
def afficher_regles():
    print("\nRÈGLES DU JEU :")
    print("Pour gagner un combat, le score du dé doit être supérieur à la force du monstre.")
    print("En cas de victoire, vous gagnez des points de vie égaux à la force du monstre.")
    print("En cas de défaite, vous perdez autant de points de vie que la force du monstre.")
    print("Contourner un monstre coûte 1 point de vie.")
    print("La partie se termine quand votre niveau de vie tombe à 0 ou moins.\n")

# Boucle principale du jeu
while niveau_vie > 0:
    # Détermination de la force de l'adversaire
    if nombre_victoires_consecutives >= 3:
        force_adversaire = random.randint(4, 6)  # Boss plus fort
        print("\nVous affrontez un BOSS !")
    else:
        force_adversaire = random.randint(1, 5)

    # Affichage des informations du combat
    print(f"\nAdversaire {numero_combat} - Force : {force_adversaire}")
    print(f"Niveau de vie : {niveau_vie}")
    print("Que voulez-vous faire ?")
    print("1 - Combattre cet adversaire")
    print("2 - Contourner cet adversaire")
    print("3 - Afficher les règles du jeu")
    print("4 - Quitter la partie")

    choix = input("Votre choix : ")

    if choix == "1":
        # Lancer du dé
        score_de = random.randint(1, 6)
        print(f"Lancer du dé : {score_de}")

        if score_de > force_adversaire:
            # Victoire
            niveau_vie += force_adversaire
            nombre_victoires += 1
            nombre_victoires_consecutives += 1
            print("Victoire !")
        else:
            # Défaite
            niveau_vie -= force_adversaire
            nombre_defaites += 1
            nombre_victoires_consecutives = 0
            print("Défaite...")

        # Mise à jour du statut
        print(f"Niveau de vie : {niveau_vie}")
        print(f"Victoires : {nombre_victoires} | Défaites : {nombre_defaites}")
        numero_combat += 1

    elif choix == "2":
        # Contournement
        niveau_vie -= 1
        nombre_victoires_consecutives = 0
        print("Vous avez contourné le monstre. -1 point de vie.")
        print(f"Niveau de vie : {niveau_vie}")

    elif choix == "3":
        # Affichage des règles
        afficher_regles()

    elif choix == "4":
        # Fin de partie
        print("Merci et au revoir...")
        break

    else:
        print("Choix invalide. Veuillez entrer 1, 2, 3 ou 4.")

# Fin de partie si niveau de vie épuisé
if niveau_vie <= 0:
    print(f"\nPartie terminée. Vous avez vaincu {nombre_victoires} monstre(s).")
