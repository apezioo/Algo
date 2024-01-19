 def circle_placement(self, event):
        button = event.widget

        if self.__etat_boutons.get(button) and self.__etat_boutons[button]['etat'] == 1:
            return                                                                                                                    # Sert à empecher le fait de pouvoir un pion sur un autre pion

        if self.__joueur == 1 and self.__dernier_bouton_clique is not None:
            last_row, last_col = Pion.get_button_rouge_position(self.__dernier_bouton_clique2)
            current_row, current_col = Pion.get_button_rouge_position(button)                                                         # Servent à récupérer la position du pion rouge en se servant de la fonction get_button_rouge_position de la class Pion

            valid_positions = [(last_row - 2, last_col - 1), (last_row - 2, last_col + 1),
                            (last_row - 1, last_col - 2), (last_row - 1, last_col + 2),
                            (last_row + 1, last_col - 2), (last_row + 1, last_col + 2),
                            (last_row + 2, last_col - 1), (last_row + 2, last_col + 1)]                                               # Sert à lister les positions valides

            if (current_row, current_col) not in valid_positions:               
                return                                                                                                               # Sert à faire rejouer le joueur si son déplacement n'est pas sur une case valide

        if self.__joueur == 2 and self.__dernier_bouton_clique2 is not None:
            last_row, last_col = Pion.get_button_bleu_position(self.__dernier_bouton_clique2)
            current_row, current_col = Pion.get_button_bleu_position(button)                                                          # Servent à récupérer la position du pion bleu en se servant de la fonction get_button_bleu_position de la class Pion

            valid_positions = [(last_row - 2, last_col - 1), (last_row - 2, last_col + 1),
                            (last_row - 1, last_col - 2), (last_row - 1, last_col + 2),
                            (last_row + 1, last_col - 2), (last_row + 1, last_col + 2),
                            (last_row + 2, last_col - 1), (last_row + 2, last_col + 1)]                                               # Sert à lister les positions valides

            if (current_row, current_col) not in valid_positions:                                                               
                return
            
        if self.__joueur == 1:
            pion_rouge = Image.open("img/cercle.png")
            pion_rouge1 = ImageTk.PhotoImage(pion_rouge)                                                                        # Servent à importer l'image du rond rouge 
            button.configure(image=pion_rouge1)
            button.image = pion_rouge1                                                                                          # Servent à appliquer l'image sur le bouton cliqué 

            if self.__turn >= 2:                                                                                                # Sert à détecter si il y a un pion rond rouge sur le plateau pour ensuite le transformer en croix rouge. De plus, la création des croix commencent à partir que "self.__turn==2" c'est a dire quand les deux joueurs ont posés leur premier pion
                if self.__dernier_bouton_clique2 is not None:
                    croix_rouge = Image.open("img/croix_rouge.png")
                    croix_rouge1 = ImageTk.PhotoImage(croix_rouge)                                                              # Servent à importer l'image de croix rouge 
                    self.__etat_boutons[self.__dernier_bouton_clique2]['image'] = croix_rouge1                                  # Sert à stocker le nouvel état de la case cliqué                
                    self.__dernier_bouton_clique2.configure(image=croix_rouge1)
                    self.__dernier_bouton_clique2.image = croix_rouge1                                                          # Servent à afficher l'image à l'endroit souhaité

            self.__dernier_bouton_clique2 = self.__dernier_bouton_clique                                                        
            self.__dernier_bouton_clique = button                                                                               # Servent à mettre a jour le rond rouge précedent en croix rouge

        elif self.__joueur == 2:
            pion_bleu = Image.open("img/sans_titre.png")
            pion_bleu1 = ImageTk.PhotoImage(pion_bleu)                                                                          # Servent à importer l'image du cercle Bleu
            button.configure(image=pion_bleu1)
            button.image = pion_bleu1                                                                                           # Servent à appliquer l'image sur le bouton cliqué

            if self.__turn >= 2:                                                                                                # Sert à détecter si il y a un pion rond bleu sur le plateau pour ensuite le transformer en croix bleu. De plus, la création des croix commencent à partir que "self.__turn==2" c'est a dire quand les deux joueurs ont posés leur premier pion
                if self.__dernier_bouton_clique2 is not None:
                    croix_bleu = Image.open("img/croix_bleu.png")
                    croix_bleu1 = ImageTk.PhotoImage(croix_bleu)                                                                # Servent à importer l'image de la croix bleu
                    self.__etat_boutons[self.__dernier_bouton_clique2]['image'] = croix_bleu1                                   # Sert à stocker le nouvel état de la case cliqué
                    self.__dernier_bouton_clique2.configure(image=croix_bleu1)
                    self.__dernier_bouton_clique2.image = croix_bleu1                                                           # Sert à afficher l'image à l'endroit souhaité

            self.__dernier_bouton_clique2 = self.__dernier_bouton_clique
            self.__dernier_bouton_clique = button                                                                               # Servent à mettre a jour le rond bleu précedent en croix bleu

        self.__etat_boutons[button]['etat'] = 1
        button.configure(state=DISABLED)                                                                                        # Servent à désactiver le bouton si il à déjà été cliqué
    
        self.__joueur = 3 - self.__joueur                                                                                       # Sert à effectuer le roulement des joueurs

        self.__turn += 1                                                                                                        # Sert à ajouter 1 à self.__turn à chaque pion posé pout gérer le placement des croix

        self.__text4.config(text=f"Joueur : {self.__joueur}")                                                                   # Sert à modifier l'affichage "Joueur : " en alternant 1 et 2
        self.__text5.config(text=f"Tour n° : {self.__turn+1}")                                                                  # Sert à ajouter 1 à chaque tour pour l'affichage du Tour)


    def check_end_game2(self):
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