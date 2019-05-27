
    
'''!@brief Классы карточек для интепретатора.
    @details Данные классы позволяют интерпертировать выбранные игроками карточки в код ЯП Си.
    @author Данный ряд классов был создан Владиславом Кривозубовым студентом ИУ7-22Б
    @param[in] char_case - массив сгенерированных простых карточек
    @param[in] pointer_char_case - массив сгенерированных карточек указателей
    @param[out] output_string - Выходная строка
    
'''

char_case = []
pointer_char_case = []
output_string = ""

def clean():
    global char_case, pointer_char_case
    char_case = []
    pointer_char_case = []

# Массивы, хранящие все созданные переменные(объекты классов Char и Pointer_char)
# Они используются только эмулятором и, если надо, рандомайзером

from char import Char
from pointer_char import Pointer_Char

# Карточка инициализации существующей переменной (a = 'L';)
class Init_card:
    '''!@brief Класс инициализации существующей переменной
        @param[out] value, name - значение и имя перемнной соответственно
    '''

    def __init__(self, char_name, char_value):
        self.value = char_value
        self.name = char_name

    def action(self):
        '''!@brief Функция выполнения инструкции карточки  
            @details Проверяет были ли объявленная переменная ранне, если да, то присваивает
            ей какое - то значение
            @param[in] is_exist - boolean переменная, которая возрващает True, если заданная переменная существует
        '''

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
        '''!@brief Возвращает имя карточки  
        '''

        return self.name + ' = \'' + str(self.value) + '\';'

    value = None
    name = None

# Карточка для совместного объявления и инициализации другой переменной(char a = b;)
class Init_card_another_var:
    '''!@brief Класс для совместного объявления и инициализации другой переменной
        @param[in] left_char, right_char - задают поля классов
    '''

    global char_case
    def __init__(self, left_name, right_name):
        self.left_char = left_name
        self.right_char = right_name

    def assignment(self, value):
        '''!@brief Функция присваивания значения переменной 
            @param[in] new_char - переменная для новой переменной игры
        '''

        if value == None:
            raise RuntimeError("Ошибка: переменная " + self.right_char + " не была инициализирована")
        new_char = Char()
        new_char.set_name(self.left_char)
        new_char.set_value(value)
        char_case.append(new_char)    

    def action(self):
        '''!@brief Функция выполнения инструкции карточки  
            @details Проверяет задавалась ли указанная переменная в стаке карт, если нет,
            то добавляет её в стак и присваивает ей значение другой переменной
            @param[in] existance - boolean переменная, которая возвращает True, если
            переменная сущетсвует
        '''

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
        '''!@brief Возвращает имя карточки  
        '''

        return 'char ' + str(self.left_char) + ' = ' + str(self.right_char) + ';'

    left_char = None
    right_char = None

# Карточка для объявления переменной (char a;)
class Declaration_card:
    '''!@brief Класс для объявления переменной
        @param[out] name - возвращает имя переменной
    '''

    def __init__(self, char_name):
        self.name = char_name

    def action(self):
        '''!@brief Функция выполнения инструкции карточки  
            @details Проверяет задавалась ли указанная переменная в стаке карт, если нет,
            то добавляет её в стак
            @param[in] new_var - переменная для новой переменной игры
        '''

        global char_case
        for var in char_case:
            if var.get_name() == self.name:
                raise RuntimeError("Ошибка: двойное объявление переменной " + self.name)   
        new_var = Char()
        new_var.set_name(self.name)
        char_case.append(new_var)

    def view(self):
        '''!@brief Возвращает имя карточки  
        '''

        return 'char ' + str(self.name) + ';'
        
    name = None


# Карточка для совместного обьявления и инициализации(char a = 'L';)
class Init_declaration_card:
    '''!@brief Класс для совместного обьявления и инициализации
        @param[out] value, name - значение и имя перемнной соответственно
    '''

    def __init__(self, char_name, char_value):
        self.value = char_value
        self.name = char_name

    def action(self):
        '''!@brief Функция выполнения инструкции карточки  
            @details Проверяет задавалась ли указанная переменная в стаке карт, если нет,
            то добавляет её в стак и присваивает ей какое-то значение
            @param[in] new_var - переменная для новой переменной игры
        '''

        global char_case
        for var in char_case:
            if var.get_name() == self.name:
                raise RuntimeError("Ошибка: двойное объявление переменной " + self.name)    
        new_var = Char()
        new_var.set_name(self.name)
        new_var.set_value(self.value)
        char_case.append(new_var)

    def view(self):
        '''!@brief Возвращает имя карточки  
        '''

        return 'char ' + str(self.name) + ' = \'' + str(self.value) + '\';'

    name = None
    value = None

# Карточка для объявления переменной через указатель(char a = *b;)
class Init_by_pointer:
    '''!@brief Класс для объявления переменной через указатель
        @param[in] pointer_obj - переменная для объекта класса
        @param[out] c_name, p_name - переменные для имен указателя и переменной

    '''

    global char_case, pointer_char_case
    def __init__(self, char_name, pointer_name):
        self.c_name = char_name
        self.p_name = pointer_name

    def assign(self):
        '''!@brief Фукнция присваивания указателя переменной  
        '''

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
        '''!@brief Функция выполнения инструкции карточки  
            @details Проверяет задавалась ссылается ли заданный указатель на что либо, если да, то
            создает новую переменную, проверяет задавалась ли она раньше, если нет, то
            присваивает ей этот указатель
        '''

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
        '''!@brief Возвращает имя карточки  
        '''

        return 'char ' + str(self.c_name) + ' = *' + str(self.p_name) + ';' 

    pointer_obj = None
    c_name = None
    p_name = None

# Карточка для присваивания переменных типа char(char a, char b: a = b;)
class Value_to_value_card:
    '''!@brief Класс для присваивания переменных типа char 

    '''

    global char_case

    def __init__(self, left_name, right_name):
        self.left = left_name
        self.right = right_name

    def assign(self, right_var):
        '''!@brief Фукнция присвоения значения одной переменной другой  
        '''

        for var in char_case:
            if var.get_name() == self.left:
                var.set_value(right_var.get_value())

    def action(self):
        '''!@brief Функция выполнения инструкции карточки  
            @details Проверяет были ли заданны и имеют ли значение две указанные переменные, если
            да, то присваивает значение первой переменной второй
        '''

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
    '''!@brief Класс объявления указателя 
        @param[in] name - имя переменной игры
    '''

    def __init__(self, pointer_name):
        self.name = pointer_name
    
    def action(self):
        '''!@brief Функция выполнения инструкции карточки  
            @details Проверяет был ли задан указатель ранее, если нет, то создает его
        '''

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
        '''!@brief Возвращает имя карточки  
        '''

        return 'char *' + str(self.name) + ';'

    name = None

# Карточка инициализации указателя (a = &b;)
class Init_p_card:
    '''!@brief Класс инициализации указателя 

    '''

    global pointer_char_case, char_case

    def __init__(self, p_name, p_ref):
        self.name = p_name
        self.ref = p_ref

    def assign(self):
        '''!@brief Фукнция присвоения адреса указателя новой переменной  
        '''

        for var_p in pointer_char_case:
            if var_p.get_name() == self.name:
                var_p.set_reference(self.ref)
                break
            
    def action(self):
        '''!@brief Функция выполнения инструкции карточки  
            @details Проверяет были ли заданы указатели ранее, если да, то присваивает адрес
            одного другому
        '''

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
        '''!@brief Возвращает имя карточки  
        '''

        return str(self.name) + ' = &' + str(self.ref) + ';'

    name = None
    ref = None

# Карточка putchar(char a);
class Putchar_card:
    '''!@brief Класс вывода значения переменной
        @param[in] name - имя переменной игры

    '''

    global char_case, output_string

    def __init__(self, char_name):
        self.name = char_name
        
    def action(self):
        '''!@brief Функция выполнения инструкции карточки  
            @details Проверяет была ли задана переменная, если да, то выводит ее значение 
        '''

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
        '''!@brief Возвращает имя карточки  
        '''

        return 'putchar(' + str(self.name) + ');'

    name = None

# Карточка для вывода указателя (putchar(*a))
class Putchar_p_card:
    '''!@brief Класс для вывода указателя

    '''

    global pointer_char_case, char_case
    
    def __init__(self, pointer_name):
        self.name = pointer_name

    def not_none(self, pointer_object):
        '''!@brief Фукнция для выявления ошибочных ситуаций
            @details возвращает 1, если указатель ни на что не ссылаетя
            2, если переменная, на которую ссылается указатель не была инициализирована

        '''

        if pointer_object.get_reference() == None:
            return 1
        for var in char_case:
            if (var.get_name() == pointer_object.get_reference() and
                var.get_value() == None):
                return 2
        return 3
        
    def output_value(self, pointer_object):
        '''!@brief функция вывода символа
        '''

        for var in char_case:
            if var.get_name() == pointer_object.get_reference():
                return (var.get_value())

    def action(self):
        '''!@brief Функция выполнения инструкции карточки  
            @details Прогоняет функцию not_none, если всё в порядке, то выводит значение
            указателя
        '''

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
        '''!@brief Возвращает имя карточки  
        '''

        return 'putchar(*' + str(self.name) + ');'

    name = None

# Карточка для присваивания указателся указателю (a = b)
class Pointer_to_pointer:
    '''!@brief Класс для присваивания указателся указателю 

    '''

    global pointer_char_case, char_case

    def __init__(self, p_1, p_2):
        self.name1 = p_1
        self.name2 = p_2

    def assign(self):
        '''!@brief Функция проверки инициализации указателя
        '''

        if self.p_2.get_reference() == None:
            raise RuntimeError("Ошибка: указатель " + self.name2 + " не инициализирован")
        else:
            for p_var in pointer_char_case:
                if p_var.get_name() == self.name1:
                    p_var.set_reference(self.p_2.get_reference())
                    break
            
    def action(self):
        '''!@brief Функция выполнения инструкции карточки  
            @details Проверяет были ли объявлены указатели, если да, то присваивает значение одного
            второму
        '''

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
        '''!@brief Возвращает имя карточки  
        '''

        return str(self.name1) + ' = ' + str(self.name2) + ';'

    p_2 = None 
    name1 = None
    name2 = None


# Карточка для присваивания значения указателя переменной (a = *b)
class Value_from_pointer:
    '''!@brief Класс для присваивания значения указателя переменной
        @param[in] pointer - указатель
        @param[in] ref_pointer - переменный указатель
        @param[out] name_c, name_p - имя переменной и указателя

    '''

    global pointer_char_case, char_case

    def __init__(self, char_name, pointer_name):
        self.name_c = char_name
        self.name_p = pointer_name

    def assign(self):
        '''!@brief Функция присваивание значения указателя переменной
        '''

        for var in char_case:
            if var.get_name() == self.name_c:
                var.set_value(self.ref_pointer.get_value())
                break

    def checkout(self):
        '''!@brief Функция проверки инициализации указателя и переменной
        '''

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
        '''!@brief Функция выполнения инструкции карточки  
            @details Совершает проверку кретин ли вы, если нет то присваивает  значение указателя
            переменной
            @param[in] is_exist_c, is_exist_p - boolean переменные, которые возвращают True, если
            переменная или уазатель существуют
        '''

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
        '''!@brief Возвращает имя карточки  
        '''

        return str(self.name_c) + ' = *' + str(self.name_p) + ';' 

    pointer = None
    ref_pointer = None
    name_c = None
    name_p = None

# Карточка для присваивания значения указателя указателю (*a = *b)
class Value_to_value_p:
    '''!@brief Класс для присваивания значения указателя указателю 

    '''

    global char_case, pointer_char_case

    def __init__(self, p_1, p_2):
        self.name_left = p_1
        self.name_right = p_2

    def search(self):
        '''!@brief Производит проверку инициализации указателя
        '''

        for var in char_case:
            if var.get_name() == self.object_right.get_reference():
                return var.get_value()

    def assign(self):
        '''!@brief Функция присвоения значения указателя указателю  
        '''

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
        '''!@brief Функция выполнения инструкции карточки  
            @details Проверяет были ли задан указатели ранее, если да, то
            присваивает значениe указателя указателю
        '''

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
        '''!@brief Возвращает имя карточки  
        '''

        return '*' + str(self.name_left) + ' = *' + str(self.name_right) + ';'

    object_right = None
    object_left = None
    name_left = None
    name_right = None
