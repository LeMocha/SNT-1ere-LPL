#Début du programme.
#Début de l'importation des dépendances
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import os
from os.path import basename
#Fin de l'importation des dépendances

root = tk.Tk()                                                  # Affichage de la fenêtre d'éxécution
root.withdraw()                                                 # Pour ne pas afficher la fenêtre nécéssaire au fonctionnement du programme.
print("Sélectionnez un fichier.")                               # Demande à l'utilisateur de sélectionner d'image
try:                                                            # Essayer de
    chemin = askopenfilename()                                  # Demander le chemin (avec la fenêtre Windows) du fichier et de le mettre dans une variable
except:                                                         # Si je n'y arrive pas (erreur) :
    print("Veillez sélectionner un fichier !")                  # Demander à l'utilisateur de choisir une image
    quit()                                                      # Stopper le programme

try:                                                            # Essayer d' :
    img = Image.open(chemin)                                    # Ouvrir de l'image choisie 
except:                                                         # Si je n'y arrive pas (erreur) :
    print("Vous devez choissir un fichier image compatible !")  # Demander à l'utilisateur de choisir une image correcte 
    quit()                                                      # Stopper le programme

basename(chemin)                                                # Donne à l'extension OS (qui gère les extensions de fichiers dans le cas présent) le chemin de notre image
fileName, fileExtension = os.path.splitext(chemin)              # Extrait le nom du fichier ainsi que son extension.
larg=img.width                                                  # Prend la largeur de l'image et la met dans une variable
haut=img.height                                                 # Prend la hauteur de l'image et la met dans une variable
print(larg)

print("Extention reconnue ! ", fileExtension)                   # Donne a l'utilisateur l'extension du fichier qui sera traité.
print("Chemin du fichier choisi : ", chemin)                    # Impression du chemin de l'image 
print("Taille de l'image", img.size)                            # Impression de la taille de l'image
print("Traitement en cours...")                                 # Dit à l'utilisateur que l'image est en cours de traitement.

for j in range (0,haut-1,1):                                    
    for k in range(10):
        img.putpixel((k,j),(0,255,0))
        img.putpixel((-k,-j),(0,255,0))

for j in range (0,larg-1,1):                                    
    for k in range(10):
        img.putpixel((-j,k),(0,255,0))
        img.putpixel((j,-k),(0,255,0))

nom = fileName+"-modifie"+fileExtension                         # Prépare le nom du fichier modifié pour sauvegarde
print("Terminé ! L'image a été enresitrée sous : ", nom)        # Dit à l'utilisateur que le traitement est terminé et son chemin d'enregistrement
img.save(nom)                                                   # Enregistre l'image avec le nom dans le chemin du fichier de base
img.show()                                                      # Affiche le résultat
#Fin du programme.