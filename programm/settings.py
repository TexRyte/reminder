import sys
import json
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *



class Settings_Window(QMainWindow):
    switch_to_main = Signal()  # Сигнал для возврата в главное окно
    settings_changed = Signal(dict)  # Сигнал для передачи темы

    def __init__(self):
        super().__init__()

        # Настройки
        with open ("settings.json") as f:
            self.settings = json.load(f)

        # Создание и настройка Settings_Window

        self.setWindowTitle("Настройки")


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

        
        if self.settings["height"] == "720":
            self.btn_resol_var_1.setChecked(True)

        elif self.settings["height"] == "1024":
            self.btn_resol_var_2.setChecked(True)

        elif self.settings["height"] == "1080":            
            self.btn_resol_var_3.setChecked(True) 

            # Режим окна 

        self.window_mode_layout = QGridLayout()

        self.btn_window_mode_fullscreen = QRadioButton("Полноэкранный")
        self.btn_window_mode_borderless = QRadioButton("Окно без рамки")
        self.btn_window_mode_windowed = QRadioButton("Оконный")

        self.btn_window_mode_fullscreen.clicked.connect(self.resol_disable)
        self.btn_window_mode_borderless.clicked.connect(self.resol_enable)
        self.btn_window_mode_windowed.clicked.connect(self.resol_disable)
        
        self.window_mode_buttons_group = QButtonGroup()
        self.window_mode_layout.addWidget(QLabel("Режим окна"), 0, 0, 3, 1, alignment=Qt.AlignCenter)

        list_of_buttons = [self.btn_window_mode_fullscreen, self.btn_window_mode_borderless, self.btn_window_mode_windowed]

        for i in range(3):
            self.window_mode_buttons_group.addButton(list_of_buttons[i])
            self.window_mode_layout.addWidget(list_of_buttons[i], i, 1, 1, 1, alignment=Qt.AlignCenter)

        if self.settings["window_mode"] == "windowed":
            self.btn_window_mode_windowed.setChecked(True)

        elif self.settings["window_mode"] == "fullscreen":
            self.btn_window_mode_fullscreen.setChecked(True)

        elif self.settings["window_mode"] == "borderless":            
            self.btn_window_mode_borderless.setChecked(True) 
            # Тема
        
        self.theme_layout = QGridLayout()
        self.btn_light_theme = QRadioButton("Светлая")
        self.btn_dark_theme = QRadioButton("Тёмная")

        self.theme_buttons_group = QButtonGroup()
        self.theme_layout.addWidget(QLabel("Тема"), 0, 0, 2, 1, alignment=Qt.AlignCenter)

        list_of_buttons = [self.btn_light_theme, self.btn_dark_theme]

        for i in range(2):
            self.theme_buttons_group.addButton(list_of_buttons[i])
            self.theme_layout.addWidget(list_of_buttons[i], i, 1, 1, 1, alignment=Qt.AlignCenter)

        del list_of_buttons

        if self.settings["current_theme"] == "light":
            self.btn_light_theme.setChecked(True)

        elif self.settings["current_theme"] == "dark":
            self.btn_dark_theme.setChecked(True)

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

        list_of_buttons = [self.btn_back, self.btn_default, self.btn_save]

        for i in list_of_buttons:
            i.setMinimumSize(QSize(230, 50))
            i.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        del list_of_buttons

        self.btn_back.clicked.connect(self.back)
        self.btn_default.clicked.connect(self.set_default)
        self.btn_save.clicked.connect(self.save_properties)

        # Добавляем кнопки в button_layout

        button_layout.addWidget(self.btn_back)
        button_layout.addWidget(self.btn_default)
        button_layout.addWidget(self.btn_save)

        self.set_properties()

    # Перетаскивание адаптивности шрифта кнопок в конец инициализации
    def resizeEvent(self, event):
        
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

    # Разрешение нужно только в случае, если окно borderless
    def resol_disable(self):
        for btn in self.resol_buttons_group.buttons():
            btn.setEnabled(False)
    
        self.settings_menu_Layout.itemAt(0).widget().setStyleSheet("""
            background-color: rgb(169, 169, 169);\n
            color: rgb(0, 0, 0);\n
            border-radius: 10px;\n""")
   
    def resol_enable(self):
        for btn in self.resol_buttons_group.buttons():
            btn.setEnabled(True)
        
        self.settings_menu_Layout.itemAt(0).widget().setStyleSheet(self.settings["widget_theme"])
        
    def set_default(self):
        self.btn_resol_var_1.setChecked(True)
        self.btn_light_theme.setChecked(True)
        self.btn_window_mode_windowed.setChecked(True)
        self.startup_checkbox.setChecked(False)
        self.save_properties()
    
    # Применение настроек
    def set_properties(self):
        self.setStyleSheet(self.settings["main_box_theme"])

        btns = [self.btn_save, self.btn_default, self.btn_back]
        for b in btns:
            b.setStyleSheet(self.settings["buttons_theme"])

        for w in range(self.settings_menu_Layout.count()):
            self.settings_menu_Layout.itemAt(w).widget().setStyleSheet(self.settings["widget_theme"]) 

        if not self.btn_resol_var_1.isEnabled():
            self.resol_disable()

        if not self.isHidden():
            self.hide()
            self.check_window_mode()
            self.show()
        else:
            self.hide()
            self.check_window_mode()

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

        # Нужно перенести смещение на последний момент, иначе координаты окна начинают своевольничать
        QTimer.singleShot(0, lambda: self.move(0, 0))

    def set_borderless_mode(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.resize(int(self.settings["width"]), int(self.settings["height"]))
        

    def check_window_mode(self):

        if self.settings["window_mode"] == "fullscreen":
            self.btn_window_mode_fullscreen.click() # Чтобы сработал .connect
            self.set_fullscreen_mode()

        elif self.settings["window_mode"] == "borderless":
            self.btn_window_mode_borderless.setChecked(True)
            self.set_borderless_mode()

        elif self.settings["window_mode"] == "windowed":   
            self.btn_window_mode_windowed.click() 
            self.set_windowed_mode()
        
    
    def save_properties(self):
        self.check_buttons()
        
        self.settings = {"main_box_theme" : self.main_box_theme,
                        "buttons_theme" : self.buttons_theme,
                        "widget_theme" : self.widget_theme,
                        "ScheduleTable_theme" : self.ScheduleTable_theme,
                        "current_theme" : self.btn_theme_checked,
                        "width" : self.resol_w,
                        "height" : self.resol_h,
                        "window_mode" : self.window_mode}
        
        with open ('settings.json', 'w') as f:
            json.dump(self.settings, f)
                
        self.set_properties()
        print(self.geometry())
        self.settings_changed.emit(self.settings)
            
    def check_buttons(self):
        
        if self.btn_resol_var_1.isEnabled():
            if self.btn_resol_var_1.isChecked():
                self.resol_w = "1280"
                self.resol_h = "720"
            elif self.btn_resol_var_2.isChecked():
                self.resol_w = "1280"
                self.resol_h = "1024"
            elif self.btn_resol_var_3.isChecked():
                self.resol_w = "1920"
                self.resol_h = "1080"
        else:
            self.resol_w = "1280"
            self.resol_h = "720"


        if self.btn_window_mode_fullscreen.isChecked():
            self.window_mode = "fullscreen"
        elif self.btn_window_mode_borderless.isChecked():
            self.window_mode = "borderless"
        elif self.btn_window_mode_windowed.isChecked():
            self.window_mode = "windowed"


        if self.btn_light_theme.isChecked():
            self.main_box_theme = "background-color: rgb(255, 255, 255);"
            self.buttons_theme = """
                border-radius: 10px;\n
                background-color: rgb(100, 149, 237);\n
                color: rgb(255, 255, 255);"""
            self.widget_theme = """
                background-color: rgb(100, 149, 237);\n
                color: rgb(255, 255, 255);\n
                border-radius: 10px;\n"""
            self.ScheduleTable_theme = """
            QTableWidget {
                border-style: solid;
                border-width: 1px;
                border-color: none grey none none;
            }
            QHeaderView::section {
                color: rgb(0, 0, 0);
                background-color: rgb(255, 255, 255);
                font-weight: bold;
            }
            """
            self.btn_theme_checked = "light"
            
        if self.btn_dark_theme.isChecked():
            self.main_box_theme = "background-color: rgb(31, 31, 31);"
            self.buttons_theme = """
                border-radius: 10px;\n
                background-color: rgb(184, 134, 11);\n
                color: rgb(0, 0, 0);"""
            self.widget_theme = """
                background-color: rgb(184, 134, 11);\n
                color: rgb(0, 0, 0);\n
                border-radius: 10px;\n"""
            self.ScheduleTable_theme = """
            QTableWidget {
                border-style: solid;
                border-width: 1px;
                border-color: none grey none none;
            }
            QHeaderView::section {
                color: rgb(0, 0, 0);
                background-color: rgb(218, 165, 32);
                font-weight: bold;
            }
            """
            self.btn_theme_checked = "dark"

        if self.startup_checkbox.isChecked():
            pass


