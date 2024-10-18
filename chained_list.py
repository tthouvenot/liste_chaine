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

        while printed_element != None:
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
    

