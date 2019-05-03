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

    def assign_value():
        char_variable.set_value(self.value)

    self.name = None
    self.value = None
