import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import main_menu

class Main_Window(QtWidgets.QMainWindow, main_menu.Startup):
    '''!@brief Класс описания параметров и функций кнопок главного меню
    '''
    def __init__(self, parent=None):
        super().__init__()
        self.setup_main(self)
        self.setup_actions_main()       

def main():
    '''!@brief основная функция работы файла
    '''
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_Window()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
