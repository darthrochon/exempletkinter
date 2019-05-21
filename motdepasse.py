from tkinter import *
import string
from random import randint, choice

#---------------------------------------------------------------------
#fonction pour générer une chaine aléatoire
#https://pynative.com/python-generate-random-string/
def generer_mdp():
    mdp_min = 8
    mdp_max = 16
    caracteres_dispos = string.ascii_letters + string.digits
    lemdp = ""
    for x in range(randint(mdp_min,mdp_max)):
        lemdp += lemdp.join(choice(caracteres_dispos))
    mdp_saisi.delete(0,END)
    mdp_saisi.insert(0,lemdp)


# creation fenetre de base
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("800x400")
window.iconbitmap("icon.ico")
window.config(background="#939eaf")

#creation d'un frame
frame = Frame(window,bg="#939eaf")

#creatin d'un frame pour la droite
frame_droite = Frame(frame,bg="#939eaf")

#creation d'image
largeur = 300
hauteur = 300
mon_image = PhotoImage(file="lock.png")
canvas = Canvas(frame,width=largeur,height=hauteur, bg="#939eaf",bd=1,highlightthickness=0)
canvas.create_image(largeur/2,hauteur/2,image=mon_image)
canvas.grid(row=0,column=0,sticky=W)

#creation du titre
titre = Label(frame_droite,text="Mot de passe", font=("courrier",26),bg="#939eaf",fg="white")
titre.pack()


#input box
mdp_saisi = Entry(frame_droite,text="********",font=("courrier",14),bg="grey",fg="white")
mdp_saisi.pack()

#bouton
btn_mdp = Button(frame_droite,text="Générer",font=("courrier",14),bg="#939eaf",fg="white",command=generer_mdp)
btn_mdp.pack(pady=20,fill=X)
#placer la frame de droite
frame_droite.grid(row=0,column=1,sticky=W)

#afficher frame
frame.pack(expand=YES)


#------------------------------------
#barre de menu
barre_menu = Menu(window)
menu_fichier = Menu(barre_menu)
menu_fichier.add_command(label="Nouveau", command=generer_mdp)
menu_fichier.add_command(label="Quitter", command=window.quit)
barre_menu.add_cascade(label="Fichier", menu=menu_fichier)

#ajouter notre barre de menu à notre fenetre principale
window.config(menu=barre_menu)
window.mainloop()