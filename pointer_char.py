class Pointer_Char:
    def set_name(self, new_name):
        self.name = new_name

    def set_reference(self, char_variable):
        self.reference = char_variable

    # Тут возвращается объект класса char
    def get_reference(self):
        return self.reference 

    self.name = None
    self.reference = None
