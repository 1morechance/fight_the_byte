'''!@brief Файл с классом для создания переменной типа char


'''

class Char:
    '''!@brief Класс для создания переменной типа char
    @details Содержит имя переменной и её значение

    '''

    def set_name(self, new_name):
        self.name = new_name

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    name = None
    value = None
