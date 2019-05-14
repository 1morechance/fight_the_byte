import sys
from PyQt5 import QtWidgets
import main_menu
import game_process_menu
import settings
import rules_menu

# В этом классе мы описываем параметры и функции кнопок главного меню
class Main_Window(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        
        # Описываем функции каждой кнопки, используя ее objectName(Play_button, etc.)
        self.Play_button.clicked.connect(self.Game)
        self.Settings_button.clicked.connect(self.Settings)
        self.Rules_button.clicked.connect(self.Rules)
        self.dialog_game_process = Play_Window(self)
        self.dialog_settings = Settings_Window(self)
        self.dialog_rules = Rules_Window(self)

    #Функции, вызова новых окон в соответствии с каждой кнопкой
    # В функции Game, НЕОБХОДИМО ДЕВЕЛОПЕРАМ написать начало игры
    def Game(self):
        self.dialog_game_process.show()

    def Settings(self):
        self.dialog_settings.show()

    def Rules(self):
        self.dialog_rules.show()
        
# Описаниее окна игрового процесса,здесь есть кнопка Next_turn_button, ну собственно здесь начинается работа девелоперов
class Play_Window(QtWidgets.QMainWindow, game_process_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        
# Описание окна настроек, которое ни на что не влияет потому что никто не удосужился заняться звуком)
class Settings_Window(QtWidgets.QMainWindow, settings.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.Back_to_main_menu_button.clicked.connect(self.comeback)

    def comeback(self):
        self.hide()
        
# Окно правил        
class Rules_Window(QtWidgets.QMainWindow, rules_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.Back_to_main_menu_button.clicked.connect(self.comeback)

    def comeback(self):
        self.hide()

# main function    
def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_Window()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
