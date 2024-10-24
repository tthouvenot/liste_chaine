# On crée la classe qui représente les éléments. Ils ont une valeur et un suivant qui par défaut est à None
class Element:

    def __init__(self, value):
        self.value = value
        self.next = None

# On crée la classe list qui sera la classe permettant de manipuler les éléments. ELle a une valeur premier élément et dernier élément tout deux par défaut à None
class List:

    def __init__(self):
        self.first_element = None
        self.last_element = None

    # Méthode ADD
    def add_element(self, element_value):

        new_element = Element(element_value)

        if self.first_element == None:
            self.first_element = new_element
        else:
            self.last_element.next = new_element

        self.last_element = new_element

    # Méthode Afficher tout
    def show_list_elements(self):

        printed_element = self.first_element

        while printed_element is not None:
            print(printed_element.value)
            printed_element = printed_element.next

    # Méthode supprimer dernier élément
    def delete_last_element(self):
        
        last_entry = self.first_element

        while last_entry.next.next != None:
            last_entry = last_entry.next

        last_entry.next = None
        self.last_element = last_entry

    # Méthode supprimer élément de l'index. Attention c'est bien l'index et non le nième élément qu'on souhaite supprimer
    def delete_selected_element(self, index):
        
        last_entry = self.first_element
        accu = 0

        if index == 0:
            self.first_element = last_entry.next
        elif index == 1:
            last_entry.next = last_entry.next.next
        else:
            while accu != index - 1:
                last_entry = last_entry.next
                accu += 1
            
            last_entry.next = last_entry.next.next
        
    # Méthode créer un sous tableau avec index début et index fin
    def sub_list(self, start_index, end_index):
        
        last_entry = self.first_element
        accu = 0
        sub_list = List()

        while last_entry.next.next != None:
            last_entry = last_entry.next

            if accu >= start_index-1 and accu <= end_index-1:
                sub_list.add_element(last_entry.value)

            accu += 1

        return sub_list
    
    # Appliquer un traitement sur chaque élément
    # On peut soit appeler un callback soit une lambda
    # Pour la callback: on fait une référence (my_list.list_map(le nom de la callback))
    # Pour la lambda: On fait directement la lambda dans l'appelle (my_list.list_map(lambda x: x*2))
    def list_map(self, callback):
        
        last_entry = self.first_element

        while last_entry is not None:
            last_entry.value = callback(last_entry.value)
            last_entry = last_entry.next

###############################
#                             #
#   Dernier TP liste chaîné   #
#                             #
###############################

    # Reversed list
    def reversed_data(self):

        current_entry = self.first_element
        previous_entry = current_entry
        self.first_element= None
        self.last_element = None

        while current_entry:
            next_entry = current_entry.next

            if self.last_element is None:
                self.last_element = current_entry
                current_entry.next= None
            elif self.first_element is None and current_entry.next is None:
                self.first_element = current_entry
                current_entry.next = previous_entry
            else:
                current_entry.next = previous_entry
            
            previous_entry = current_entry
            current_entry = next_entry

    # new reversed list
    def new_reversed_list(self):

        self.reversed_data()
        new_list = List()

        element = self.first_element

        while element is not None:
            new_list.add_element(element.value)
            element = element.next

        self.reversed_data()

        return new_list
    
    # Show reverse
    def show_reverse(self):
        self.reversed_data()
        self.show_list_elements()
        self.reversed_data()















# Permet d'être utiliser en callback
def add_value(add_value, start_value):
    
    return add_value + start_value