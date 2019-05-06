char_case = []
pointer_char_case = []
# Массивы, хранящие все созданные переменные(объекты классов Char и Pointer_char)
# Они используются только эмулятором

import char

# char_variable - объект класса char, определеленный в ветке char

# Карточка инициализации существующей переменной (a = 'L';)
class Init_card:
    def __init__(self, char_name, char_value):
        self.value = char_value
        self.name = char_name

    def action(self):
        global char_case
        is_exist = False
        for var in char_case:
            if var.get_name() == self.name:
                char_variable.set_value(self.value)
                is_exist = True
                break
        if (not is_exist):
            raise RuntimeError("Ошибка компиляции: " + self.name + " не была объявлена ранее")

    value = None
    name = None

# Карточка для объявления переменной (char a;)
class Declaration_card:
    def __init__(self, char_name):
        self.name = char_name

    def action(self):
        global char_case
        for var in char_case:
            if var.get_name() == self.name:
                raise RuntimeError("Ошибка компиляции: двойное объявление переменной " + self.name)   
        new_var = Char()
        new_var.set_name(self.name)
        char_case.append(new_var)
        
    name = None


# Карточка для совместного обьявления и инициализации(char a = 'L';)
class Init_declaration_card:
    def __init__(self, char_name, char_value):
        self.value = char_value
        self.name = char_name

    def action(self):
        global char_case
        for var in char_case:
            if var.get_name() == self.name:
                raise RuntimeError("Ошибка компиляции: двойное объявление переменной " + self.name)    
        new_var = Char()
        new_var.set_name(self.name)
        new_var.set_value(self.value)
        char_case.append(new_var)

    name = None
    value = None

# Карточка для присваивания переменных типа char(char a, char b: a = b)
class Value_to_value_card:
    def __init__(self, left_name, right_name):
        self.left = left_name
        self.right = right_name

    def assign(self, right_var):
        global char_case
        for var in char_case:
            if var.get_name() == self.left:
                var.set_value(right_var.get_value())

    def action(self):
        global char_case
        is_exist_left = False
        is_exist_right = False
        for var in char_case:
            if var.get_name() == self.left:
                is_exist_left = True
            elif var.get_name() == self.right:
                is_exist_right = True
                right_var = var
        if (is_exist_left and is_exist_right):
            if (right_var.get_value() != None):
                self.assign(right_var)
            else:
                raise RuntimeError("Ошибка: " + self.right + " не была инициализирована ранее")
        elif (not is_exist_left):
            raise RuntimeError("Ошибка: " + self.left + " не была объявлена ранее")
        else:
            raise RuntimeError("Ошибка: " + self.right + " не была объявлена ранее")
            
    left = None
    right = None

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
    def __init__(self, char_name):
        self.name = char_name
    def action(self): 
        global char_case
        is_exist = False
        for var in char_case:
            if var.get_name() == self.name:
                is_exist = True
                if var.get_value() != None:
                    # тут вывод в GUI вместо консоли
                    print(var.get_value())
                else:
                    raise RuntimeError("Ошибка: " + self.name + " не была инициализирована ранее")
        if (not is_exist):
            raise RuntimeError("Ошибка: " + self.name + " не была объявлена ранее")

    name = None

#class Putchar_pointer_card:
    
