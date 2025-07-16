import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from settings import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.settings_window = Settings_Window()  # Ссылка на окно настроек
        self.settings_window.switch_to_main.connect(self.show_main_window)  # Связываем сигнал

        self.settings_window.settings_changed.connect(self.update_settings) # обновление настроек главного экрана
        
        # Сохранённые настройкиs
        with open("settings.json") as f:
            settings = json.load(f)

        # Создание и найстройка MainWindow

        self.setWindowTitle("Напоминалка")
        
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.main_layout = QHBoxLayout(self.centralwidget) # Главный бокс главного экрана
        

        # Настройка рассписания

        self.ScheduleTable = QTableWidget()  
        self.ScheduleTable.setColumnCount(8)
        self.ScheduleTable.setHorizontalHeaderLabels(["Дата/Время","Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"])
        self.ScheduleTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScheduleTable.setMinimumSize(QSize(1000, 720))
        self.ScheduleTable.horizontalHeader().setDefaultSectionSize(125)
        self.ScheduleTable.horizontalHeader().setFont(QFont("Arial", 12))

        # Создание InteractionBox

        self.InteractionBox = QVBoxLayout() # Тут будет инфа о напоминании и блок с кнопками
        self.InteractionBox.setSpacing(0)  

        # Настройка main_layout

        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0) # Поставил, чтобы не было фантомных чисел в разрешении

        self.main_layout.addWidget(self.ScheduleTable)
        self.main_layout.addLayout(self.InteractionBox)

        self.main_layout.setStretch(0, 3) 
        self.main_layout.setStretch(1, 1) 

        # Создаю содержание InteractionBox
    
        self.scrollArea = QScrollArea() # Тут будет подробная инфа о напоминаниях
        self.scrollArea.setMinimumSize(QSize(280, 620))
        self.scrollArea.setStyleSheet("border: none;")

        self.Hline = QFrame() # Нужна для разделения кнопок и информации выше
        self.Hline.setFrameShape(QFrame.HLine)
        self.Hline.setFrameShadow(QFrame.Sunken)

        self.button_layout = QVBoxLayout() # В нём будут кнопки
        self.button_layout.setSpacing(10)  
        self.button_layout.setContentsMargins(10, 10, 10, 10) 

        # Настройка кнопок

        self.btn_add = QPushButton("Добавить")
        self.btn_settings = QPushButton("Настройки")
        self.btn_quit = QPushButton("Выйти")

        self.btn_quit.clicked.connect(self.close)
        self.btn_settings.clicked.connect(self.go_settings)

        list_of_buttons = [self.btn_add, self.btn_settings, self.btn_quit]

        for i in list_of_buttons:
            i.setMinimumSize(QSize(230, 30))
            i.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        del list_of_buttons # Он больше не нужен

        # Добавляем кнопки в их layout

        self.button_layout.addWidget(self.btn_add)
        self.button_layout.addWidget(self.btn_settings)
        self.button_layout.addWidget(self.btn_quit)

        # Теперь добавим элементы в InteractionBox
        
        self.InteractionBox.addWidget(self.scrollArea)
        self.InteractionBox.addWidget(self.Hline)
        self.InteractionBox.addLayout(self.button_layout)

        self.InteractionBox.setStretch(0, 5)
        self.InteractionBox.setStretch(2, 1)

        self.update_settings(settings)

    # Нужно перетащить адаптивность шрифта кнопок в конец инициализации, иначе размер и шрифты начинают глючить
    def resizeEvent(self, event):
        QTimer.singleShot(0, self.update_button_font)

    # Создание адаптивности шрифта кнопок
    def update_button_font(self):
        # Кнопки одинаковые, поэтому нету разницы, какую взять
        new_size = max(10, self.btn_add.height() // 10) # Число 10 не имеет какой-либо логики и взято эмпирически
        self.btn_font = QFont("Arial", new_size, QFont.Bold)
        
        self.btn_settings.setFont(self.btn_font)
        self.btn_add.setFont(self.btn_font)
        self.btn_quit.setFont(self.btn_font)

    def update_settings(self, settings):
        # Применение нового стиля:
        self.setStyleSheet(settings["main_box_theme"])

        # Обновление стиля кнопок
        btns = [self.btn_add, self.btn_settings, self.btn_quit]
        for b in btns:
            b.setStyleSheet(settings["buttons_theme"])
        
        self.ScheduleTable.setStyleSheet(settings["ScheduleTable_theme"])

        if self.settings_window.isHidden():
            self.hide()
            self.check_window_mode(settings)
            self.show()
        else:
            self.check_window_mode(settings)


    def set_fullscreen_mode(self):
        screen = QApplication.primaryScreen().geometry()
        self.resize(screen.width(), screen.height())
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  
        self.setWindowState(Qt.WindowState.WindowFullScreen)  
        
    def set_windowed_mode(self):
        self.setWindowFlags(Qt.WindowType.Window)  
        self.setWindowState(Qt.WindowState.WindowNoState)
        screen = QApplication.primaryScreen().availableGeometry()
        self.resize(screen.width(), screen.height())

    def set_borderless_mode(self, settings):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.resize(int(settings["width"]), int(settings["height"]))


    def check_window_mode(self, settings):
        if settings["window_mode"] == "fullscreen":
            self.set_fullscreen_mode()

        elif settings["window_mode"] == "borderless":
            self.set_borderless_mode(settings)

        elif settings["window_mode"] == "windowed":            
            self.set_windowed_mode()
        
        self.move(0, 0)

    def show_main_window(self):
        self.show() 


    def go_settings(self):
        self.hide()
        try:
            if self.settings_window is None:  
                self.settings_window = Settings_Window()
                
                
            self.settings_window.show()
            self.settings_window.raise_()

        except Exception as e:
            print(e)         
            sys.exit()
    

    def add_reminder(self):
        pass


        


def start():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


start()
