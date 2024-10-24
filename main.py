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

# print("--- Avant la suppression ---")
# my_list.show_list_elements()
# my_list.delete_selected_element(1)
# print("--- Après la suppression ---")
# my_list.show_list_elements()

# new_sub_list = my_list.sub_list(2, 5)

# print("--- Sous liste ---")
# new_sub_list.show_list_elements()

# print('--- Avant callback ---')
# my_list.show_list_elements()

# print("--- Callback ---")
# # my_list.list_map(add_value)

# print('--- Après callback ---')
# my_list.show_list_elements()

# print("--- Lambda ---")
# my_list.list_map(lambda x: x*2)
# my_list.show_list_elements()

# print("--- Sous liste ---")
# new_sub_list.show_list_elements()

# print('--- Avant callback ---')
# my_list.show_list_elements()

# print("--- Callback ---")
# # my_list.list_map(add_value)

# print('--- Après callback ---')
# my_list.show_list_elements()

# print("--- Lambda ---")
# my_list.list_map(lambda x: x*2)
# my_list.show_list_elements()

print("--- New Reversed List ---")
my_list.show_list_elements()
print()
new_reversed_list = my_list.new_reversed_list()
print()
new_reversed_list.show_list_elements()
print()
print("---------")

print("--- Show reverse ---")
my_list.show_list_elements()
print()
my_list.show_reverse()
print()
my_list.show_list_elements()
print()
print("---------")

print("--- Reversed data ---")
my_list.reversed_data()
print()
my_list.show_list_elements()
print()
print("---------")