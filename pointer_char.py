class Pointer_Char:
    def set_name(self, ref_name):
        self.name = ref_name

    def set_reference(self, char_name):
        self.reference = char_name

    def get_reference(self):
        return self.reference

    def get_name(self):
        return self.name

    name = None
    reference = None
