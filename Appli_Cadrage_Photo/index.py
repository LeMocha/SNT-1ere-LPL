#Début du programme.
#Début de l'importation des dépendances
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import colorchooser
from tkinter import messagebox
from PIL import Image
from PIL import ImageColor
import os
from os.path import basename
#Fin de l'importation des dépendances

root = tk.Tk()                                                                                              # Affichage de la fenêtre d'éxécution
root.title('Ajout de cadre automatique par Manoah SERVEAUX')                                                # Pour ne pas afficher la fenêtre nécéssaire au fonctionnement du programme.
root.geometry("600x200+10+20")

log1 = tk.Text(root, height=1, width=100)
log1.insert(tk.INSERT, "Sélectionnez un fichier")                                                           # Demande à l'utilisateur de sélectionner d'image
log1.pack()

try:                                                                                                        # Essayer de
    chemin = askopenfilename(title="Selection de l'image à encadrer")                                       # Demander le chemin (avec la fenêtre Windows) du fichier et de le mettre dans une variable
except:                                                                                                     # Si je n'y arrive pas (erreur) :
    quit()                                                                                                  # Stopper le programme

try:                                                                                                        # Essayer d' :
    img = Image.open(chemin)                                                                                # Ouvrir de l'image choisie 
except:                                                                                                     # Si je n'y arrive pas (erreur) :
    messagebox.showwarning(title="Erreur !", message="Vous devez choissir un fichier image compatible !")   # Demander à l'utilisateur de choisir une image correcte 
    quit()                                                                                                  # Stopper le programme

log1b = tk.Text(root, height=1, width=100)
log1b.insert(tk.INSERT, "Fait !")                                                                           # Demande à l'utilisateur de sélectionner d'image
log1b.pack()

basename(chemin)                                                                                            # Donne à l'extension OS (qui gère les extensions de fichiers dans le cas présent) le chemin de notre image
fileName, fileExtension = os.path.splitext(chemin)                                                          # Extrait le nom du fichier ainsi que son extension.
larg=img.width                                                                                              # Prend la largeur de l'image et la met dans une variable
haut=img.height                                                                                             # Prend la hauteur de l'image et la met dans une variable

log2 = tk.Text(root, height=1, width=100)
log2.insert(tk.INSERT, "Choississez la couleur du cadre.")                                                  # Demande à l'utilisateur de choisir une couleur pour son cadre  
log2.pack()

(rgb, hx) = colorchooser.askcolor(title="Couleur du cadre")                                                 # Fenêtre de sélection de cadre                            
try:
    couleur = ImageColor.getcolor(hx, "RGB")                                                                # Transforme la valeur hexadécimle en RGB (Tkinter propose le RGB mais pillow ne supporte
except:                                                                                                     # pas le format, alors il l'enregistre en hexadécimal et je le traduit via cette commande)
    messagebox.showwarning(title="Erreur !", message="Veuillez choisir une couleur !")
    quit()

log3 = tk.Text(root, height=1, width=100)
log3.insert(tk.INSERT, "Fait !")                                                                            ##
log3.pack()

lc=int(input("Tapez la taille du cadre que vous souhaitez : "))                                             # Demande a l'utilisateur quelle de cardre il souhaite régler 

log4 = tk.Text(root, height=1, width=100)
log4.insert(tk.INSERT, "Taille du cadre choisie : ", lc)                                                    ##
log4.pack()

log5 = tk.Text(root, height=1, width=100)
log5.insert(tk.INSERT, "Traitement en cours...")                                                            # Dit à l'utilisateur que l'image est en cours de traitement.
log5.pack()                                                                           

try:                                                                                                        # Essaie de lancer le traitement d'image
    for j in range (0,haut-1,1):                                    
        for k in range(lc):
            img.putpixel((k,j),couleur)
            img.putpixel((-k,-j),couleur)

    for j in range (0,larg-1,1):                                     
        for k in range(lc):
            img.putpixel((-j,k),couleur)
            img.putpixel((j,-k),couleur)
except:                                                                                                     # Si echec,
    messagebox.showwarning(title="Erreur !", message="Couleur ou taille de cadre invalide !")               # Demander à l'utilisateur de prendre une couleur
    quit()                                                                                                  # Stopper le programme    

nom = fileName+"-modifie"+fileExtension                                                                     # Prépare le nom du fichier modifié pour sauvegarde

meslog5 = 'Terminé ! L\'image a été enresitrée sous :\n'+nom+'\nOuverture du résultat...'

log5 = tk.Text(root, height=4, width=100)
log5.insert(tk.INSERT, meslog5)                                                                             # Dit à l'utilisateur que le traitement est terminé et son chemin d'enregistrement
log5.pack()   
    
img.save(nom)                                                                                               # Enregistre l'image avec le nom dans le chemin du fichier de base
img.show()                                                                                                  # Affiche le résultat
root.mainloop()
#Fin du programme.