char_case = []
pointer_char_case = []
output_string = ""

# Массивы, хранящие все созданные переменные(объекты классов Char и Pointer_char)
# Они используются только эмулятором и, если надо, рандомайзером

from char import Char
from pointer_char import Pointer_Char

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
                var.set_value(self.value)
                is_exist = True
                break
        if (not is_exist):
            raise RuntimeError("Ошибка: переменная " + self.name + " не была объявлена ранее")
    
    def view(self):
        return self.name + ' = \'' + str(self.value) + '\';'

    value = None
    name = None

# Карточка для совместного объявления и инициализации другой переменной(char a = b;)
class Init_card_another_var:
    global char_case
    def __init__(self, left_name, right_name):
        self.left_char = left_name
        self.right_char = right_name

    def assignment(self, value):
        if value == None:
            raise RuntimeError("Ошибка: переменная " + self.right_char + " не была инициализирована")
        new_char = Char()
        new_char.set_name(self.left_char)
        new_char.set_value(value)
        char_case.append(new_char)    

    def action(self):
        for var in char_case:
            if var.get_name() == self.left_char:
                raise RuntimeError("Ошибка: переменная " + self.left_char + " была объявлена ранее")
        existance = False     
        for var in char_case:
            if var.get_name() == self.right_char:
                existance = True
                self.assignment(var.get_value())
                break
        if (not existance):
            raise RuntimeError("Ошибка: переменная " + self.right_char + " не была объявлена ранее")

    def view(self):
        return 'char ' + str(self.left_char) + ' = ' + str(self.right_char) + ';'

    left_char = None
    right_char = None

# Карточка для объявления переменной (char a;)
class Declaration_card:
    def __init__(self, char_name):
        self.name = char_name

    def action(self):
        global char_case
        for var in char_case:
            if var.get_name() == self.name:
                raise RuntimeError("Ошибка: двойное объявление переменной " + self.name)   
        new_var = Char()
        new_var.set_name(self.name)
        char_case.append(new_var)

    def view(self):
        return 'char ' + str(self.name) + ';'
        
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
                raise RuntimeError("Ошибка: двойное объявление переменной " + self.name)    
        new_var = Char()
        new_var.set_name(self.name)
        new_var.set_value(self.value)
        char_case.append(new_var)

    def view(self):
        return 'char ' + str(self.name) + ' = \'' + str(self.value) + '\';'

    name = None
    value = None

# Карточка для объявления переменной через указатель(char a = *b;)
class Init_by_pointer:
    global char_case, pointer_char_case
    def __init__(self, char_name, pointer_name):
        self.c_name = char_name
        self.p_name = pointer_name

    def assign(self):
        if (self.pointer_obj.get_reference() == None):
            raise RuntimeError("Ошибка: указатель " + self.p_name + " ни на что не ссылается")
        else:
            ref = self.pointer_obj.get_reference()
            for var in char_case:
                if (var.get_name() == ref):
                    if var.get_value() == None:
                        raise RuntimeError("Ошибка: переменная, на которую ссылается указатель "
                                           + self.p_name + " не была инициализирована")
                    else:
                        char_obj = Char()
                        char_obj.set_value(var.get_value())
                        char_obj.set_name(self.c_name)
                        char_case.append(char_obj)
                    break
        
    def action(self):
        is_exist_c = False
        is_exist_p = False
        for var in char_case:
            if var.get_name() == self.c_name:
                is_exist_c = True
                break
        for var_p in pointer_char_case:
            if var_p.get_name() == self.p_name:
                is_exist_p = True
                self.pointer_obj = var_p
                break
        if (is_exist_c):
            raise RuntimeError("Ошибка: переменная " + self.c_name + " была объявлена ранее")
        elif (not is_exist_p):
            raise RuntimeError("Ошибка: указатель " + self.p_name + " не был объявлен ранее")
        else:
            self.assign()

    def view(self):
        return 'char ' + str(self.c_name) + ' = *' + str(self.p_name) + ';' 

    pointer_obj = None
    c_name = None
    p_name = None

# Карточка для присваивания переменных типа char(char a, char b: a = b;)
class Value_to_value_card:
    global char_case

    def __init__(self, left_name, right_name):
        self.left = left_name
        self.right = right_name

    def assign(self, right_var):
        for var in char_case:
            if var.get_name() == self.left:
                var.set_value(right_var.get_value())

    def action(self):
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

    def view(self):
        return str(self.left) + ' = ' + str(self.right) + ';'

    left = None
    right = None

# Карточка объявления указателя (char *a;)
class Declaration_p_card:
    def __init__(self, pointer_name):
        self.name = pointer_name
    
    def action(self):
        global pointer_char_case
        is_exist = False
        for p_var in pointer_char_case:
            if (p_var.get_name() == self.name):
                is_exist = True
        if (is_exist):
            raise RuntimeError("Ошибка: указатель " + self.name + " был объявлен ранее")    
        else:
            new_p = Pointer_Char()
            new_p.set_name(self.name)
            pointer_char_case.append(new_p)

    def view(self):
        return 'char *' + str(self.name) + ';'

    name = None

# Карточка инициализации указателя (a = &b;)
class Init_p_card:
    global pointer_char_case, char_case

    def __init__(self, p_name, p_ref):
        self.name = p_name
        self.ref = p_ref

    def assign(self):
        for var_p in pointer_char_case:
            if var_p.get_name() == self.name:
                var_p.set_reference(self.ref)
                break
            
    def action(self):
        exist_p_char = False
        exist_char = False
        for var_p in pointer_char_case:
            if (var_p.get_name() == self.name):
                exist_p_char = True
                break
        for var in char_case:
            if (var.get_name() == self.ref):
                exist_char = True
                break
        if (not exist_p_char):
            raise RuntimeError("Ошибка: указатель " + self.name + " не был объявлен ранее")
        elif (not exist_char):    
            raise RuntimeError("Ошибка: переменная " + self.ref + " не была объявлена ранее")   
        else:
            self.assign()
            
    def view(self):
        return str(self.name) + ' = &' + str(self.ref) + ';'

    name = None
    ref = None

# Карточка putchar(char a);
class Putchar_card:
    global char_case, output_string

    def __init__(self, char_name):
        self.name = char_name
        
    def action(self): 
        is_exist = False
        for var in char_case:
            if var.get_name() == self.name:
                is_exist = True
                if var.get_value() != None:
                    output_string += var.get_value()
                else:
                    raise RuntimeError("Ошибка: " + self.name + " не была инициализирована ранее")
        if (not is_exist):
            raise RuntimeError("Ошибка: " + self.name + " не была объявлена ранее")

    def view(self):
        return 'putchar(' + str(self.name) + ');'

    name = None

# Карточка для вывода указателя (putchar(*a))
class Putchar_p_card:
    global pointer_char_case, char_case
    
    def __init__(self, pointer_name):
        self.name = pointer_name

    def not_none(self, pointer_object):
        if pointer_object.get_reference() == None:
            return 1
        for var in char_case:
            if (var.get_name() == pointer_object.get_reference() and
                var.get_value() == None):
                return 2
        return 3
        
    def output_value(self, pointer_object):
        for var in char_case:
            if var.get_name() == pointer_object.get_reference():
                return (var.get_value())

    def action(self):
        is_exist = False
        for p_var in pointer_char_case:
            if p_var.get_name() == self.name:
                is_exist = True
                p_object = p_var
                break
        if (not is_exist):
            raise RuntimeError("Ошибка: указатель " + self.name + " не был объявлен ранее")
        situation = self.not_none(p_object)
        if (situation == 1):
            raise RuntimeError("Ошибка: указатель " + self.name + " ни на что не ссылается")        
        elif (situation == 2):
            raise RuntimeError("Ошибка: переменная, на которую ссылается "
                               + self.name + " не была инициализирована")
        else:
            # Connect with GUI метод возвращает значение переменной на которую указывает name
            output_string += self.output_value(p_object)
    
    def view(self):
        return 'putchar(*' + str(self.name) + ');'

    name = None

# Карточка для присваивания указателся указателю (a = b)
class Pointer_to_pointer:
    global pointer_char_case, char_case

    def __init__(self, p_1, p_2):
        self.name1 = p_1
        self.name2 = p_2

    def assign(self):
        if self.p_2.get_reference() == None:
            raise RuntimeError("Ошибка: указатель " + self.name2 + " не инициализирован")
        else:
            for p_var in pointer_char_case:
                if p_var.get_name() == self.name1:
                    p_var.set_reference(self.p_2.get_reference())
                    break
            
    def action(self):
        is_exist_1 = False
        is_exist_2 = False
        for p_var in pointer_char_case:
            if (p_var.get_name() == self.name1):
                is_exist_1 = True
            elif (p_var.get_name() == self.name2):
                is_exist_2 = True
                self.p_2 = p_var
        if (not is_exist_1):
            raise RuntimeError("Ошибка: уазатель " + self.name1 + " не был объявлен ранее")
        elif (not is_exist_2):
            raise RuntimeError("Ошибка: уазатель " + self.name2 + " не был объявлен ранее")
        else:
            self.assign()

    def view(self):
        return str(self.name1) + ' = ' + str(self.name2) + ';'

    p_2 = None 
    name1 = None
    name2 = None


# Карточка для присваивания значения указателя переменной (a = *b)
class Value_from_pointer:
    global pointer_char_case, char_case

    def __init__(self, char_name, pointer_name):
        self.name_c = char_name
        self.name_p = pointer_name

    def assign(self):
        for var in char_case:
            if var.get_name() == self.name_c:
                var.set_value(self.ref_pointer.get_value())
                break

    def checkout(self):
        if (self.pointer.get_reference() == None):
            raise RuntimeError("Ошибка: указатель " + self.name_p + " не был инициализирован")
        else:
            for var in char_case:
                if (var.get_name() == self.pointer.get_reference()):
                    self.ref_pointer = var
                    if self.ref_pointer.get_value() == None:
                        raise RuntimeError("Ошибка: переменная, на которую ссылается указатель "
                                           + self.name_p + " не был инициализирована")
                    else:
                        self.assign()

    def action(self):
        is_exist_c = False
        is_exist_p = False
        for var in char_case:
            if var.get_name() == self.name_c:
                is_exist_c = True
                break
        for p_var in pointer_char_case:
            if p_var.get_name() == self.name_p:
                self.pointer = p_var
                is_exist_p = True

        if (not is_exist_c):
            raise RuntimeError("Вы кретин: переменная " + self.name_c + " не была объявлена")
        elif (not is_exist_p):
            raise RuntimeError("Ошибка: указатель " + self.name_p + " не был объявлен")
        else:
            self.checkout()

    def view(self):
        return str(self.name_c) + ' = *' + str(self.name_p) + ';' 

    pointer = None
    ref_pointer = None
    name_c = None
    name_p = None

# Карточка для присваивания значения указателя указателю (*a = *b)
class Value_to_value_p:
    global char_case, pointer_char_case

    def __init__(self, p_1, p_2):
        self.name_left = p_1
        self.name_right = p_2

    def search(self):
        for var in char_case:
            if var.get_name() == self.object_right.get_reference():
                return var.get_value()

    def assign(self):
        if (self.object_right.get_reference() == None):
            raise RuntimeError("Ошибка: указатель " + self.name_right + " не был инициализирован")
        else:
            for var in char_case:
                if var.get_name() == self.object_right.get_reference():
                    if var.get_value() == None:
                        raise RuntimeError("Ошибка: переменная, на которую ссылается указатель "
                                           + self.name_right + " не была инициализирована")
                    else:
                        for char in char_case:
                            if (char.get_name() == self.object_left.get_reference()):
                                char.set_value(self.search())
                                break
                        break
            
    def action(self):
        is_exist_left = False
        is_exist_right = False
        for p_var in pointer_char_case:
            if p_var.get_name() == self.name_left:
                self.object_left = p_var
                is_exist_left = True
            elif p_var.get_name() == self.name_right:
                self.object_right = p_var
                is_exist_right = True
        if (not is_exist_left):
            raise RuntimeError("Ошибка: указатель " + self.name_left + " не был объявлен")
        elif (not is_exist_right):
            raise RuntimeError("Ошибка: указатель " + self.name_right + " не был объявлен")
        elif (self.object_left.get_reference() == None):
            raise RuntimeError("Ошибка: указатель " + self.name_left
                               + " не был инициализирован")
        else:
            self.assign()

    def view(self):
        return '*' + str(self.name_left) + ' = *' + str(self.name_right) + ';'

    object_right = None
    object_left = None
    name_left = None
    name_right = None
