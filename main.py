from chained_list import *

my_list = List()

end_of_input = False

while not end_of_input:

    try:
        value = int(input("Quelle valeur souhaitez-vous ajouter! (un chiffre, 0 pour quitter)"))

        if value == 0:
            end_of_input = True
        else:
            my_list.add_element(value)

    except ValueError:
        print("Erreur: Valeur non valide")

print("--- Avant la suppression ---")
my_list.show_list_elements()
my_list.delete_selected_element(1)
print("--- Après la suppression ---")
my_list.show_list_elements()

new_sub_list = my_list.sub_list(2, 5)

print("--- Sous liste ---")
new_sub_list.show_list_elements()