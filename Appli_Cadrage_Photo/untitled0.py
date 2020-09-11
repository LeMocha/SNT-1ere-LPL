#d Importation des Dépences
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
#f

root = tk.Tk()                               # Dossier de sélection pour la fenêtre de base
root.withdraw()                              # Pour ne pas afficher la fenêtre Tkinter
print("Sélectionnez un fichier.")
chemin = askopenfilename()                   # Lance la fenêtre de sélection d'image
img = Image.open(chemin)                     # Ouverture de l'image choisie 
print("Chemin du fichier choisi : ", chemin) # Impression du chemin de l'image 
print("Taille de l'image", img.size)         # Impression de la taille de l'image

print("Traitement en cours...")              # Dit à l'utilisateur que l'image est en train d'être traitée