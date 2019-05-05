import char

# char_variable - объект класса char, определеленный в ветке char

# Карточка инициализации существующей переменной (a = 'L';)
class Init_card:
    def __init__(self, char_value):
        self.value = card_value

    def assign_value(self, char_variable):
        char_variable.set_value(self.value)
    
    self.value = None

# Карточка для объявления переменной (char a;)
class Declaration_card:
    def __init__(self, char_name):
        self.name = card_name

    def assign_name(self, char_variable):
        char_variable.set_name(self.value)

    self.name = None


# Карточка для совместного обьявления и инициализации(char a = 'L';)
class Init_declaration_card:
    def __init__(self, char_value, char_name):
        self.value = char_value
        self.name = char_name

    def assign_name(self, char_variable):
        char_variable.set_name(self.name)

    def assign_value(self, char_variable):
        char_variable.set_value(self.value)

    self.name = None
    self.value = None

# Карточка для присваивания переменных типа char(char a, char b: a = b)
class Value_to_value_card:
    # left_char, right char - объекты класа char
    def __init__(self, left_char, right_char):
        self.left = left_char
        self.right = right_char

    def assign():
        self.left.set_value(self.right.get_value())
    
    self.left = None
    self.right = None

# Карточка объявления указателя (char *a;)
class Init_pointer_card:
    def __init__(self, pointer_name):
        self.name = pointer_name
    
    def assign_name(self, pointer_variable):
        pointer_variable.set_name(self.name)

    self.name = None

# Карточка инициализации указателя (a = &b;)
#class Declaration_pointer_card:
 

# Карточка putchar(char a);
class Putchar_card:
    def __init__(self, char_variable):
        self.char_object = char_variable
    def output():
        # здесь идет связь с GUI(метод output возвратит вам значение переменной типа char) 
        return self.char_object.get_value()

    self.char_object = None

#class Putchar_pointer_card:
    
