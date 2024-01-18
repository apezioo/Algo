# for button, self.data in self.__etat_boutons.items():
#             if self.data[self.__dernier_bouton_clique2]['image'] == self.croix_rouge1 or self.data[self.__dernier_bouton_clique2]['image'] == self.croix_bleu1:
#                 row, col = Pion.get_button_rouge_position(button) if self.__joueur == 1 else Pion.get_button_bleu_position(button)

#                 horizontal = [self.__etat_boutons.get(self.get_button_by_position(row, col + i)) for i in range(align)]         # Vérifier l'alignement horizontal
#                 if all(self.__etat_boutons[self.__dernier_bouton_clique2]['image'] == self.croix_rouge1 in horizontal):
#                     self.end()
#                 elif all(self.__etat_boutons[self.__dernier_bouton_clique2]['image'] == self.croix_bleu1 in horizontal):
#                     self.end()

#                 vertical = [self.__etat_boutons.get(self.get_button_by_position(row + i, col)) for i in range(align)]           # Vérifier l'alignement vertical
#                 if all(self.__etat_boutons[self.__dernier_bouton_clique2]['image'] == self.croix_rouge1 in vertical):
#                     self.end()
#                 elif all(self.__etat_boutons[self.__dernier_bouton_clique2]['image'] == self.croix_bleu1 in vertical):
#                     self.end()

#                 diagonal_asc = [self.__etat_boutons.get(self.get_button_by_position(row - i, col + i)) for i in range(align)]   # Vérifier l'alignement diagonal (ascendante)
#                 if all(self.__etat_boutons[self.__dernier_bouton_clique2]['image'] == self.croix_rouge1 in diagonal_asc):
#                     self.end()
#                 elif all(self.__etat_boutons[self.__dernier_bouton_clique2]['image'] == self.croix_bleu1 in diagonal_asc):
#                     self.end()

#                 diagonal_des = [self.__etat_boutons.get(self.get_button_by_position(row + i, col + i)) for i in range(align)]   # Vérifier l'alignement diagonal (descendante)
#                 if all(self.__etat_boutons[self.__dernier_bouton_clique2]['image'] == self.croix_rouge1 in diagonal_des):
#                     self.end()
#                 elif all(self.__etat_boutons[self.__dernier_bouton_clique2]['image'] == self.croix_bleu1 in diagonal_des):
#                     self.end()

def check_top_left_to_bottom_right_diagonal(matrix, char, n):
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows - n + 1):
        for col in range(cols - n + 1):
            if all(matrix[row + i][col + i] == char for i in range(n)):
                return True
    return False

def check_other_diagonal(matrix, char, n):
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows - n + 1):
        for col in range(n - 1, cols):
            if all(matrix[row + i][col - i] == char for i in range(n)):
                return True
    return False

def detect_alignment(matrix, char, n):
    if check_top_left_to_bottom_right_diagonal(matrix, char, n):
        return f"Top-left to bottom-right diagonal alignment of '{char}' found."
    if check_top_right_to_bottom_left_diagonal(matrix, char, n):
        return f"Top-right to bottom-left diagonal alignment of '{char}' found."
    return f"No alignment of '{char}' found."

# Example usage:
matrix = [
    ['A', 'B', 'C', 'A', 'D'],
    ['E', 'A', 'F', 'D', 'G'],
    ['H', 'I', 'D', 'J', 'K'],
    ['L', 'M', 'N', 'A', 'O'],
    ['P', 'Q', 'R', 'S', 'A']
]

char_to_check = 'D'
alignment_length = 3

result = detect_alignment(matrix, char_to_check, alignment_length)
print(result)