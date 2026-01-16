from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import os
import json

from settings import *



class New_Remind_Window(QMainWindow):

    def __init__(self, input_settings):
        super().__init__()
        self.settings_path = self.user_settings_path()
        self.settings = input_settings

        self.settings.settings_changed.connect(self.update_theme)

        if not os.path.exists(self.settings_path):
            # копируем шаблон из ресурсов
            with open(self.resource_path("settings.json"), "r") as src:
                with open(self.settings_path, "w") as dst:
                    dst.write(src.read())

        with open(self.settings_path) as f:
            settings = json.load(f)

        self.setWindowTitle("Добавить новое напоминание")
        self.setWindowFlags(
            Qt.WindowType.Window |
            Qt.WindowType.WindowTitleHint |
            Qt.WindowType.WindowSystemMenuHint |
            Qt.WindowType.WindowMinimizeButtonHint |
            Qt.WindowType.WindowCloseButtonHint
        )
        w_size = QGuiApplication.primaryScreen().size().width() // 3 # Взято имперически
        h_size = QGuiApplication.primaryScreen().size().height() // 4 # Взято имперически
        self.setFixedSize(w_size, h_size)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.main_box = QVBoxLayout(self.centralwidget)



        self.new_remind_box = QGridLayout()
        self.buttons_box = QHBoxLayout()

        self.Hline = QFrame()
        self.Hline.setFrameShape(QFrame.HLine)  
        self.Hline.setFrameShadow(QFrame.Sunken)
        self.Hline.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.Hline.setFixedHeight(3) 
        self.Hline.setStyleSheet("border: 1px dashed gray;")

        for i in [self.new_remind_box, self.Hline, self.buttons_box]:
            if not isinstance(i, QWidget):
                temp = QWidget()
                temp.setLayout(i)
                self.main_box.addWidget(temp)
            else:
                self.main_box.addWidget(i)

        self.main_box.setStretch(0, 10)
        self.main_box.setStretch(2, 1)

        self.main_box.setSpacing(2) 
        self.main_box.setContentsMargins(2, 2, 2, 2) 

        # new_remind_box

        self.name_LEdit = QLineEdit()
        self.name_LEdit.setPlaceholderText("Введите название")

        self.desc_TEdit = QTextEdit()
        self.desc_TEdit.setPlaceholderText("Введите описание (опционально)")

        self.date = QDateEdit()
        self.date.setCalendarPopup(True)  
        self.date.setDate(QDate.currentDate()) 

        self.time = QTimeEdit()
        self.time.setDisplayFormat("HH:mm")

        self.priority = QComboBox()
        self.priority.addItem("Выберите приоритет")
        self.priority.addItems(str(i) for i in range(1, 11))
        
        self.repeatability = QComboBox()
        self.repeatability.addItems([
            "Повторяемость (опционально)",
            "Каждый день",
            "Каждую неделю",
            "Каждый месяц",
            "Каждый год",
            "Каждые N минут",
            "Каждые N часов",
            "Каждые N дней",
            "Каждые N неделей",
            "Каждые N месяцев",
            "Каждые N лет"
        ])

        self.user_repeatability = QSpinBox()
        self.user_repeatability.setValue(1)
        self.user_repeatability.setEnabled(False)

        

        self.new_remind_box.addWidget(self.name_LEdit, 0, 0, 1, 2)
        self.new_remind_box.addWidget(self.desc_TEdit, 1, 0, 4, 2)
        self.new_remind_box.addWidget(self.date, 0, 2)
        self.new_remind_box.addWidget(self.time, 1, 2)
        self.new_remind_box.addWidget(self.priority, 2, 2)
        self.new_remind_box.addWidget(self.repeatability, 3, 2)
        self.new_remind_box.addWidget(self.user_repeatability, 4, 2)

        for i in range(self.new_remind_box.count()):
            self.new_remind_box.itemAt(i).widget().setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
         

        # button_box

        self.btn_back = QPushButton("Вернуться")
        self.btn_save = QPushButton("Сохранить")

        self.btn_back.clicked.connect(self.back)
        self.btn_save.clicked.connect(self.save)

        self.buttons_box.addWidget(self.btn_back)
        self.buttons_box.addWidget(self.btn_save)

        for i in range(self.buttons_box.count()):
            self.buttons_box.itemAt(i).widget().setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.update_theme(settings)

    def resource_path(self, filename):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, filename)
            return os.path.join(os.path.abspath("."), filename)
            
    def user_settings_path(self):
        return os.path.join(os.path.dirname(sys.executable if hasattr(sys, 'frozen') else __file__), "settings.json")            

    def update_theme(self, settings):
        self.setStyleSheet(settings["main_box_theme"])

        l = [self.name_LEdit, self.desc_TEdit, self.time, self.priority, self.repeatability, self.user_repeatability]
        for _ in l:
            _.setStyleSheet(settings["remind_widget_theme"])
        
        self.date.setStyleSheet(settings["QDate_edit"])
        
        self.btn_back.setStyleSheet(settings["buttons_theme"])
        self.btn_save.setStyleSheet(settings["buttons_theme"])

    def back(self):
        self.close()
    
    def save(self):
        pass
