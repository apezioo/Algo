from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer

class Pion:

    def __init__(self, joueur, etat):
        self.__joueur = joueur
        self.etat = etat

    def get_button_rouge_position(button):                     # Sert à récupérer les coordonnées du pion rouge
        row = int(button.place_info()['y']) // 70
        col = int(button.place_info()['x']) // 70              # place_info donne les coordonnées du poin supérieur gauche donc "//70" (car case de 70 pixels) pour obtenir le numero de la case
        return row, col
    
    def get_button_bleu_position(button2):                     # Sert à récupérer les coordonnées du pion bleu
        row2 = int(button2.place_info()['y']) // 70
        col2 = int(button2.place_info()['x']) // 70            # place_info donne les coordonnées du poin supérieur gauche donc "//70" (car case de 70 pixels) pour obtenir le numero de la case
        return row2, col2

class Acceuil:
    def __init__(self):
        self.__root1 = Tk()
        self.__root1.title("Acceuil")
        self.__root1.geometry("1000x1000")

        mixer.init()
        mixer.music.load("music/music1.mp3")
        mixer.music.set_volume(1)
        mixer.music.play(-1)

        self.__frame1 = Frame(self.__root1, bg="black")
        self.__frame1.pack(side=TOP, fill=BOTH, expand=True)

        self.__root1.grid_rowconfigure(0, weight=1)
        self.__root1.grid_columnconfigure(0, weight=1)

        style = ttk.Style()
        style.configure("TButton", foreground="black", background="black", font=("Helvetica", 12), padding=(40, 20))

        self.__frame2 = Frame(self.__frame1)
        self.__frame2.pack(side=TOP, pady=250, padx=10)  # Move the comboboxes to the top

        self.__text2 = Label(self.__frame2, text="Taille de la grille : ", font=("Helvetica", 12))
        self.__text2.grid(row=0, column=0, padx=5, pady=19)

        self.v = IntVar(value=10)

        size_values = [8, 9, 10, 11, 12]
        self.__size = ttk.Combobox(self.__frame2, textvariable=self.v, values=size_values, state="readonly")
        self.__size.grid(row=0, column=2, padx=5)

        self.__frame3 = Frame(self.__frame1)
        self.__frame3.pack(side=TOP)

        self.__text3 = Label(self.__frame3, text="Nombres de pions à aligner : ", foreground="black", font=("Helvetica", 12))
        self.__text3.grid(row=1, column=0, padx=5, pady=19)

        self.v2 = IntVar(value=5)

        align_values = [4, 5, 6]
        self.__align = ttk.Combobox(self.__frame3, textvariable=self.v2, values=align_values, state="readonly")
        self.__align.grid(row=1, column=2, padx=5)

        self.__frame4 = Frame(self.__frame1, bg="black")  # Set the background color to black
        self.__frame4.pack(side=BOTTOM, pady=50)  # Move the buttons to the bottom

        start_button = ttk.Button(self.__frame4, text="Commencer", command=self.start_game)
        start_button.pack(side=LEFT, padx=20)

        rules_button = ttk.Button(self.__frame4, text="Règles", command=self.show_rules)
        rules_button.pack(side=LEFT, padx=20)

        self.__root1.mainloop()



    def show_rules(self):
            rules_window = Toplevel(self.__root1)
            rules_window.title("Règles")
            rules_window.config(bg="black")

            rules_text = (
                "Règles du jeu :\n"
                "- Les deux joueurs vont jouer chacun leur tour.\n"
                "- Les joueurs peuvent déplacer leur pions qu'en L (comme le cavalier aux échecs).\n"
                "- La partie se fini si un des deux joueurs alignent le nombre de croix sélectionné ou si il ne peut plus se déplacer."
            )

            label = Label(rules_window, text=rules_text, padx=20, pady=20, bg="black", foreground="white")
            label.pack()

            close_button = Button(rules_window, text="Fermer", command=rules_window.destroy)
            close_button.pack(pady=10)

    def start_game(self):
            mixer.music.stop()
            self.__root1.destroy()
            Jeu(grid_size= self.v.get())
class Jeu:
    
    def __init__(self, grid_size):
        self.__grid_size = grid_size
        self.__joueur = 1
        self.__turn = 0

        mixer.init()
        mixer.music.load("music/music2.mp3")
        mixer.music.set_volume(1)
        mixer.music.play(-1)

        self.__croix_positions_joueur1 = []
        self.__croix_positions_joueur2 = []

        self.__etat_boutons = {}                                # création d'un dictionnaire pour gérer l'état des cases

        self.__dernier_bouton_clique = None                     # création d'une variable initialisé sur None pour détecter le dernier bouton cliqué et ainsi le transformer en croix

        self.__root = Tk()
        self.__root.title("Projet")

        self.__frame1 = Frame(self.__root, bg="black")
        self.__frame1.grid(row=0, column=0, columnspan=2)

        self.__canvas = Canvas(self.__frame1)
        self.__canvas.pack()

        self.create_grid()

        self.__frame2 = Frame(self.__root)
        self.__frame2.grid(row=1, column=0)

        
        # Boutons de la sélection de la taille de la grille
        
        self.__frame3 = Frame(self.__root)
        self.__frame3.grid(row=1, column=1)                                                                            # Création du Frame pour placer les boutons

        self.__text2 = Label(self.__frame3, text="Nombres de cases : ")                 
        self.__text2.grid(row=0, column=0, columnspan=5)                                                               # Création et placement du texte au dessus des boutons

        self.v = IntVar(value=grid_size)
        self.__case1 = ttk.Radiobutton(self.__frame3, variable=self.v, value=8, text="8", command=self.update_grid)
        self.__case2 = ttk.Radiobutton(self.__frame3, variable=self.v, value=9, text="9", command=self.update_grid)
        self.__case3 = ttk.Radiobutton(self.__frame3, variable=self.v, value=10, text="10", command=self.update_grid)      # Création des boutons, utilisation des Boutons Radios
        self.__case4 = ttk.Radiobutton(self.__frame3, variable=self.v, value=11, text="11", command=self.update_grid)        
        self.__case5 = ttk.Radiobutton(self.__frame3, variable=self.v, value=12, text="12", command=self.update_grid)

        self.__case1.grid(row=1, column=0)
        self.__case2.grid(row=1, column=1)
        self.__case3.grid(row=1, column=2)                                                                             # Placement des boutons dans le frame
        self.__case4.grid(row=1, column=3)
        self.__case5.grid(row=1, column=4)


       
        # Boutons de la sélection du nombre de pion à aligner
        
        self.__frame4 = Frame(self.__root)
        self.__frame4.grid(row=1, column=0, sticky=W, padx=10)                                                         # Création du Frame pour placer les boutons ("sticky=w" sert à placer le frame collé à gauche et "padx=10" à le décaller un peu du bord)
                                                                                                                                                                    
        self.__text3 = Label(self.__frame4, text="Nombres de pions à aligner : ")
        self.__text3.grid(row=0, column=0, columnspan=3)                                                               # Création et placement du texte au dessus des boutons

        self.v2 = IntVar(value=5)
        self.__case11 = ttk.Radiobutton(self.__frame4, variable=self.v2, value=4, text="4")
        self.__case12 = ttk.Radiobutton(self.__frame4, variable=self.v2, value=5, text="5")                                # Création des boutons, utilisation des Boutons Radios
        self.__case13 = ttk.Radiobutton(self.__frame4, variable=self.v2, value=6, text="6")

        self.__case11.grid(row=1, column=0)
        self.__case12.grid(row=1, column=1)                                                                            # Placement des boutons dans le frame
        self.__case13.grid(row=1, column=2)

        self.__text4 = Label(self.__frame4, text=f"Joueur : {self.__joueur}")
        self.__text4.grid(row=0, column=3, padx=200)                                                                    # Servent à afficher le joueur qui joue

        self.__text5 = Label(self.__frame4, text=f"Tour n° : {self.__turn+1}")
        self.__text5.grid(row=1, column=3, padx=200)                                                                    # Servent à afficher le numéro du Tour




        self.__root.mainloop()

    
    
    def create_grid(self):
        self.__w = self.__grid_size * 70                                                                               # Sert à définir la taille de la grille. Le " * 50" sert à définir le nombre de pixel des cases, ici 50 pixels
        self.__h = self.__grid_size * 70
        self.__canvas.config(width=self.__w, height=self.__h, highlightthickness=0, bd=0, bg="black")

        square_size = int(min(self.__w, self.__h) / self.__grid_size)                                                  # Sert à définir la taille de chaque case. "min(self.__w, self.__h)" sert à définir le plus petit des deux et donc assurer une case carrée. On divise ensuite par le nombre de cases voulu défini par "self.__grid_size"
        for i in range(0, self.__w, square_size):
            for j in range(0, self.__h, square_size):

                button = Button(self.__canvas, bd=2, bg="black")                
                button.place(x=i, y=j, width=square_size, height=square_size)                                          # Sert à que la grille soit constitué de boutons cliquables
                button.bind("<Button-1>", self.circle_placement)                                                       # Sert à activer la fonction "circle_placement" au moment du clique
                self.__etat_boutons[button] = {'etat': 0, 'image': None}                                               # Sert à mettre l'etat des boutons à 0
                

    def update_grid(self):                                                                                                      # Sert à modifier la grille en fonction de la taille choisie
        if messagebox.askquestion('Avertissement','Cette action va redémarrer la partie.\nConfirmer',icon ='warning')=='yes':   # Affiche une fênetre pour confirmer le changement
            self.__root.destroy()                                                                                               # Sert à supprimer le programme en cas de redémarrage
            Jeu(self.v.get())

    def valid_move(self, last_position, current_position):
        last_row, last_col = last_position
        current_row, current_col = current_position

        valid_positions = [
            (last_row - 2, last_col - 1), (last_row - 2, last_col + 1),
            (last_row - 1, last_col - 2), (last_row - 1, last_col + 2),
            (last_row + 1, last_col - 2), (last_row + 1, last_col + 2),
            (last_row + 2, last_col - 1), (last_row + 2, last_col + 1)
        ]

        return (current_row, current_col) in valid_positions

    def check_end_game(self):
        if self.__turn >= 2:
            player_positions = (
                Pion.get_button_rouge_position if self.__joueur == 1 else Pion.get_button_bleu_position
            )
            current_position = player_positions(self.__dernier_bouton_clique)

            for button, info in self.__etat_boutons.items():
                i, j = int(button.place_info()['y']) // 70, int(button.place_info()['x']) // 70
                if info['etat'] == 0 and self.valid_move(current_position, (i, j)):
                    return False
        self.end()


    def circle_placement(self, event):
        button = event.widget

        if self.__etat_boutons.get(button) and self.__etat_boutons[button]['etat'] == 1:
            return

        if self.__joueur == 1 and self.__dernier_bouton_clique is not None:
            last_position = Pion.get_button_rouge_position(self.__avantdernier_bouton_clique)
            current_position = Pion.get_button_rouge_position(button)
            if not self.valid_move(last_position, current_position):
                return

        if self.__joueur == 2 and self.__avantdernier_bouton_clique is not None:
            last_position = Pion.get_button_bleu_position(self.__avantdernier_bouton_clique)
            current_position = Pion.get_button_bleu_position(button)
            if not self.valid_move(last_position, current_position):
                return

        if self.__joueur == 1:
            pion_rouge = Image.open("img/cercle.png")
            pion_rouge1 = ImageTk.PhotoImage(pion_rouge)                                                                        # Servent à importer l'image du rond rouge 
            button.configure(image=pion_rouge1)
            button.image = pion_rouge1                                                                                          # Servent à appliquer l'image sur le bouton cliqué 

            if self.__turn >= 2:                                                                                                # Sert à détecter si il y a un pion rond rouge sur le plateau pour ensuite le transformer en croix rouge. De plus, la création des croix commencent à partir que "self.__turn==2" c'est a dire quand les deux joueurs ont posés leur premier pion
                if self.__avantdernier_bouton_clique is not None:
                    croix_rouge = Image.open("img/croix_rouge.png")
                    croix_rouge1 = ImageTk.PhotoImage(croix_rouge)                                                              # Servent à importer l'image de croix rouge 
                    self.__etat_boutons[self.__avantdernier_bouton_clique]['image'] = croix_rouge1                                  # Sert à stocker le nouvel état de la case cliqué                
                    self.__avantdernier_bouton_clique.configure(image=croix_rouge1)
                    self.__avantdernier_bouton_clique.image = croix_rouge1                                                          # Servent à afficher l'image à l'endroit souhaité

            self.__avantdernier_bouton_clique = self.__dernier_bouton_clique                                                        
            self.__dernier_bouton_clique = button                                                                               # Servent à mettre a jour le rond rouge précedent en croix rouge

        elif self.__joueur == 2:
            pion_bleu = Image.open("img/sans_titre.png")
            pion_bleu1 = ImageTk.PhotoImage(pion_bleu)                                                                          # Servent à importer l'image du cercle Bleu
            button.configure(image=pion_bleu1)
            button.image = pion_bleu1                                                                                           # Servent à appliquer l'image sur le bouton cliqué

            if self.__turn >= 2:                                                                                                # Sert à détecter si il y a un pion rond bleu sur le plateau pour ensuite le transformer en croix bleu. De plus, la création des croix commencent à partir que "self.__turn==2" c'est a dire quand les deux joueurs ont posés leur premier pion
                if self.__avantdernier_bouton_clique is not None:
                    croix_bleu = Image.open("img/croix_bleu.png")
                    croix_bleu1 = ImageTk.PhotoImage(croix_bleu)                                                                # Servent à importer l'image de la croix bleu
                    self.__etat_boutons[self.__avantdernier_bouton_clique]['image'] = croix_bleu1                                   # Sert à stocker le nouvel état de la case cliqué
                    self.__avantdernier_bouton_clique.configure(image=croix_bleu1)
                    self.__avantdernier_bouton_clique.image = croix_bleu1                                                           # Sert à afficher l'image à l'endroit souhaité

            self.__avantdernier_bouton_clique = self.__dernier_bouton_clique
            self.__dernier_bouton_clique = button                                                                               # Servent à mettre a jour le rond bleu précedent en croix bleu

        self.__etat_boutons[button]['etat'] = 1
        button.configure(state=DISABLED)                                                                                        # Servent à désactiver le bouton si il à déjà été cliqué
    
        self.__joueur = 3 - self.__joueur                                                                                       # Sert à effectuer le roulement des joueurs

        self.__turn += 1                                                                                                        # Sert à ajouter 1 à self.__turn à chaque pion posé pout gérer le placement des croix

        self.__text4.config(text=f"Joueur : {self.__joueur}")                                                                   # Sert à modifier l'affichage "Joueur : " en alternant 1 et 2
        self.__text5.config(text=f"Tour n° : {self.__turn+1}")                                                                  # Sert à ajouter 1 à chaque tour pour l'affichage du Tour)

        if self.__turn >= 2:
            self.check_end_game()

    def end(self):
        if messagebox.askquestion('Fin de la partie',f'Partie terminée : Victoire du joueur {self.__joueur}\n\nVoulez vouz rejouer ?',icon ='question')=='yes':
            self.__root.destroy()                                                                                                                                           # Sert à supprimer le programme en cas de redémarrage
            Jeu(self.v.get())                                                                                                                                               # Sert à remettre le Tour à 1 en cas de redémarrage de la partie
        else :
            self.__root.destroy()                                                                                                                                           # Sert à fermer le programme en cas de réponse négative                                                                       


    def start_game():
        Acceuil.__root1.destroy()
        Jeu()

acceuil = Acceuil()      