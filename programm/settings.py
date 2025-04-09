import sys
import json
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *



class Settings_Window(QMainWindow):
    switch_to_main = Signal()  # Сигнал для возврата в главное окно
    theme_changed = Signal(dict)  # Сигнал для передачи темы

    def __init__(self):
        super().__init__()

        # Настройки
        self.set_theme()
    
        self.first_resize_done = False  # Нужен флаг, ибо при запуске окно меняет размер дважды
        

        # Создание и настройка Settings_Window

        self.setWindowTitle("Настройки")
        QTimer.singleShot(0, lambda: self.setGeometry(0, 31, 1280, 720))
        
        self.setStyleSheet(self.main_box_theme)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.main_box = QVBoxLayout(self.centralwidget) # Главный бокс настроек

        self.settingsWidget = QWidget()
        self.settings_layout = QHBoxLayout(self.settingsWidget) # Меню настроек
        
            # Разрешение

        self.resol_layout = QGridLayout()
        
        self.btn_resol_var_1 = QRadioButton("1280x720")
        self.btn_resol_var_2 = QRadioButton("1280x1024")
        self.btn_resol_var_3 = QRadioButton("1920x1080")
        
        self.resol_buttons_group = QButtonGroup()
        self.resol_layout.addWidget(QLabel("Разрешение"), 0, 0, 3, 1, alignment=Qt.AlignCenter)

        list_of_buttons = [self.btn_resol_var_1, self.btn_resol_var_2, self.btn_resol_var_3]

        for i in range(3):
            self.resol_buttons_group.addButton(list_of_buttons[i])
            self.resol_layout.addWidget(list_of_buttons[i], i, 1, 1, 1, alignment=Qt.AlignCenter)

            # Режим окна 

        self.window_mode_layout = QGridLayout()

        self.btn_window_mode_var_1 = QRadioButton("Полноэкранный")
        self.btn_window_mode_var_2 = QRadioButton("Окно без рамки")
        self.btn_window_mode_var_3 = QRadioButton("Оконный")
        
        self.window_mode_buttons_group = QButtonGroup()
        self.window_mode_layout.addWidget(QLabel("Режим окна"), 0, 0, 3, 1, alignment=Qt.AlignCenter)

        list_of_buttons = [self.btn_window_mode_var_1, self.btn_window_mode_var_2, self.btn_window_mode_var_3]

        for i in range(3):
            self.window_mode_buttons_group.addButton(list_of_buttons[i])
            self.window_mode_layout.addWidget(list_of_buttons[i], i, 1, 1, 1, alignment=Qt.AlignCenter)

            # Тема
        
        self.theme_layout = QGridLayout()
        self.btn_theme_var_1 = QRadioButton("Светлая")
        self.btn_theme_var_2 = QRadioButton("Тёмная")

        self.theme_buttons_group = QButtonGroup()
        self.theme_layout.addWidget(QLabel("Тема"), 0, 0, 2, 1, alignment=Qt.AlignCenter)

        list_of_buttons = [self.btn_theme_var_1, self.btn_theme_var_2]

        for i in range(2):
            self.theme_buttons_group.addButton(list_of_buttons[i])
            self.theme_layout.addWidget(list_of_buttons[i], i, 1, 1, 1, alignment=Qt.AlignCenter)

        del list_of_buttons

            # Автозагрузка 
        
        self.startup_layout = QHBoxLayout()
        self.startup_layout.addWidget(QLabel("Автозагрузка"), alignment=Qt.AlignCenter)

        self.startup_checkbox = QCheckBox()
        self.startup_layout.addWidget(self.startup_checkbox, alignment=Qt.AlignCenter)

            # Настраиваем вид settings_menu_Layout

        self.settings_menu_Widget = QWidget() # Для центрирования
        self.settings_menu_Widget.setMinimumWidth(500)

        self.settings_menu_Layout = QVBoxLayout(self.settings_menu_Widget) 
        self.settings_layout.addStretch()
        self.settings_layout.addWidget(self.settings_menu_Widget)
        self.settings_layout.addStretch()
        
        list_of_layouts = [self.resol_layout, self.window_mode_layout, self.theme_layout, self.startup_layout]

        for i in list_of_layouts:
            temp_widget = QWidget()
            temp_widget.setStyleSheet(self.widget_theme)

            temp_widget.setLayout(i)
            temp_widget.setMinimumSize(320, 200)
            self.settings_menu_Layout.addWidget(temp_widget)

        self.settings_menu_Layout.setSpacing(10)

        

        # Создаем ScrollArea

        self.scrollArea = QScrollArea() # Для прокрутки, если понадобится
        self.scrollArea.setMinimumHeight(620)
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setWidgetResizable(True)

        self.scrollArea.setWidget(self.settingsWidget)


        # Создание разделительной линия

        self.Hline = QFrame()
        self.Hline.setFrameShape(QFrame.HLine)  
        self.Hline.setFrameShadow(QFrame.Sunken)
        self.Hline.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.Hline.setFixedHeight(3) 
        self.Hline.setStyleSheet("border: 1px dashed gray;")

        # Создание поля для кнопок quit, default, save

        button_layout = QHBoxLayout()  # Горизонтальный макет для кнопок
        button_layout.setSpacing(10)  # Отступы между кнопками
        button_layout.setContentsMargins(10, 10, 10, 10)  # Внутренние отступы
        
        # Настройка главного бокса

        self.main_box.setSpacing(0)
        self.main_box.setContentsMargins(0, 0, 0, 0)

        self.main_box.addWidget(self.scrollArea)
        self.main_box.addWidget(self.Hline)
        self.main_box.addLayout(button_layout)

        self.main_box.setStretch(0, 10)
        self.main_box.setStretch(2, 1)

        # Создание кнопок

        self.btn_back = QPushButton("Вернуться")
        self.btn_default = QPushButton("По умолчанию")
        self.btn_save = QPushButton("Сохранить")

        btn_style = self.buttons_theme
        list_of_buttons = [self.btn_back, self.btn_default, self.btn_save]

        for i in list_of_buttons:
            i.setMinimumSize(QSize(230, 50))
            i.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            i.setStyleSheet(btn_style)

        del list_of_buttons

        self.btn_back.clicked.connect(self.back)
        self.btn_default.clicked.connect(self.set_default)
        self.btn_save.clicked.connect(self.save_properties)

        # Добавляем кнопки в button_layout

        button_layout.addWidget(self.btn_back)
        button_layout.addWidget(self.btn_default)
        button_layout.addWidget(self.btn_save)

    # Перетаскивание адаптивности шрифта кнопок в конец инициализации
    def resizeEvent(self, event):
        # Проверка не даёт второй раз изменить размер окна, если то только что запустилось
        if not self.first_resize_done:
            self.first_resize_done = True
            QTimer.singleShot(0, self.update_button_font)
            QTimer.singleShot(0, self.update_menu_font)

            return 
        
        QTimer.singleShot(0, self.update_button_font)
        QTimer.singleShot(0, self.update_menu_font)

    # Создание адаптивности шрифта кнопок нижней панели
    def update_button_font(self):
        # Кнопки одинаковые, поэтому нету разницы, какую взять
        new_size = max(10, self.btn_back.height() // 10) # Число 10 не имеет какой-либо логики и взято эмпирически


        self.btn_font = QFont("Arial", new_size, QFont.Bold)

        self.btn_default.setFont(self.btn_font)
        self.btn_back.setFont(self.btn_font)
        self.btn_save.setFont(self.btn_font)

    # Создание адаптивности шрифта кнопок настроек
    def update_menu_font(self):
        new_size = max(10, self.settings_menu_Widget.width() // 30) # 30 взято импирически

        font = QFont("Arial", new_size, QFont.Bold)

        for widget in self.settings_menu_Widget.findChildren(QWidget):
            widget.setFont(font)

    
    # Возврат к главному окну
    def back(self):
        self.close()  
        self.switch_to_main.emit()  # Отправляем сигнал в MainWindow

    def set_default(self):
        self.main_box_theme = "background-color: rgb(255, 255, 255);"
        self.buttons_theme = """
            border-radius: 10px;\n
            background-color: rgb(100, 149, 237);\n
            color: rgb(255, 255, 255);"""
        self.widget_theme = """
            background-color: rgb(100, 149, 237);\n
            color: rgb(255, 255, 255);\n
            border-radius: 10px;\n"""
        
    def save_properties(self):
        self.check_buttons()

        with open ('settings.json', 'w') as f:
            temp_dict = {"main_box_theme" : self.main_box_theme,
                         "buttons_theme" : self.buttons_theme,
                          "widget_theme" : self.widget_theme}
            json.dump(temp_dict, f)
            del temp_dict
        
    
    def set_theme(self):
        with open ("settings.json") as f:
            temp_dict = json.load(f)
            self.main_box_theme = temp_dict["main_box_theme"]
            self.buttons_theme = temp_dict["buttons_theme"]
            self.widget_theme = temp_dict["widget_theme"]

        
        self.theme_changed.emit(temp_dict) # Отправляем новые стили

        del temp_dict

    def check_buttons(self):
        if self.btn_resol_var_1.isChecked():
            pass
        if self.btn_resol_var_2.isChecked():
            pass
        if self.btn_resol_var_3.isChecked():
            pass

        if self.btn_window_mode_var_1.isChecked():
            pass
        if self.btn_window_mode_var_2.isChecked():
            pass
        if self.btn_window_mode_var_3.isChecked():
            pass

        if self.btn_theme_var_1.isChecked():
            self.main_box_theme = "background-color: rgb(255, 255, 255);"
            self.buttons_theme = """
                border-radius: 10px;\n
                background-color: rgb(100, 149, 237);\n
                color: rgb(255, 255, 255);"""
            self.widget_theme = """
                background-color: rgb(100, 149, 237);\n
                color: rgb(255, 255, 255);\n
                border-radius: 10px;\n"""
            
        if self.btn_theme_var_2.isChecked():
            self.main_box_theme = "background-color: rgb(31, 31, 31);"
            self.buttons_theme = """
                border-radius: 10px;\n
                background-color: rgb(184, 134, 11);\n
                color: rgb(0, 0, 0);"""
            self.widget_theme = """
                background-color: rgb(184, 134, 11);\n
                color: rgb(0, 0, 0);\n
                border-radius: 10px;\n"""
           

        if self.startup_checkbox.isChecked():
            pass


