#importer la librairie tkinter
from tkinter import *

#importe webbrowser
import webbrowser

#fonction  pour ouvrir une page web
def ouvrirWeb():
    webbrowser.open_new("http://zombo.com")


#créer la fenêtre principale
fenetre = Tk()
fenetre.title("Mon application demo")
fenetre.geometry("720x480") #dimension de départ
fenetre.minsize(480,360) #dimension minimal
fenetre.iconbitmap("icon.ico") #icon de l'app
fenetre.config(background="#5b9960") #couleur de fond

#creer un boite, enfant de la fenetre principale
sous_fenetre = Frame(fenetre,bg="#5b9960")
sous_fenetre.pack(expand=YES)

#ces éléments d'interface sont des enfants de la sous-fenetre
#ajouter du texte, Titre, 
gros_titre = Label(sous_fenetre,text="Bienvenue dans python", font=("courrier",40),bg="#5b9960",fg="white")
gros_titre.pack()

#ajouter sous-titre
sous_titre = Label(sous_fenetre,text="python rulezzzzz", font=("courrier",25),bg="#5b9960",fg="white")
sous_titre.pack()

#bouton
mon_bouton = Button(sous_fenetre, text="Ouvrir zombo.com", font=("courrier",25),bg="white",fg="#5b9960", command=ouvrirWeb)
mon_bouton.pack(pady=25,fill=X)

#afficher
fenetre.mainloop()