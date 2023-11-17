# Библиотека PyQt5 была установлена через команду 'pip install pyqt5' введённую в терминал.
# А вот PyQt5 работает благодаря фреймворку Qt.
# Здесь у нас импортируются отдельные модули.
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        # Здесь у нас создаётся окно, тексты, кнопки, листы и также указываются их размеры, картинки, цвета и т.д.
        # Каждая кнопка, текст, лист или другой виджет, названы в зависимости их задачи.
        # Во многом весь интерфейс был создан при помощи приложения Qt Designer.
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(960, 540)
        mainWindow.setMinimumSize(QtCore.QSize(960, 540))
        mainWindow.setMaximumSize(QtCore.QSize(960, 540))
        mainWindow.setStyleSheet("\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.phonkText = QtWidgets.QLabel(self.centralwidget)
        self.phonkText.setGeometry(QtCore.QRect(20, 5, 440, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.phonkText.setFont(font)
        self.phonkText.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.phonkText.setAlignment(QtCore.Qt.AlignCenter)
        self.phonkText.setObjectName("phonkText")
        self.hensonnButton = QtWidgets.QPushButton(self.centralwidget)
        self.hensonnButton.setGeometry(QtCore.QRect(36, 80, 180, 180))
        self.hensonnButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.hensonnButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/Hensonn.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hensonnButton.setIcon(icon)
        self.hensonnButton.setIconSize(QtCore.QSize(177, 177))
        self.hensonnButton.setObjectName("hensonnButton")
        self.imagineButton = QtWidgets.QPushButton(self.centralwidget)
        self.imagineButton.setGeometry(QtCore.QRect(264, 344, 180, 180))
        self.imagineButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.imagineButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/ImagineDragons.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imagineButton.setIcon(icon1)
        self.imagineButton.setIconSize(QtCore.QSize(177, 177))
        self.imagineButton.setObjectName("imagineButton")
        self.arturButton = QtWidgets.QPushButton(self.centralwidget)
        self.arturButton.setGeometry(QtCore.QRect(516, 344, 180, 180))
        self.arturButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.arturButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/АртурПирожков.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arturButton.setIcon(icon2)
        self.arturButton.setIconSize(QtCore.QSize(177, 177))
        self.arturButton.setObjectName("arturButton")
        self.valeraButton = QtWidgets.QPushButton(self.centralwidget)
        self.valeraButton.setGeometry(QtCore.QRect(744, 344, 180, 180))
        self.valeraButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.valeraButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/ВалерийМиладзе.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.valeraButton.setIcon(icon3)
        self.valeraButton.setIconSize(QtCore.QSize(177, 177))
        self.valeraButton.setObjectName("valeraButton")
        self.weekendButton = QtWidgets.QPushButton(self.centralwidget)
        self.weekendButton.setGeometry(QtCore.QRect(36, 344, 180, 180))
        self.weekendButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.weekendButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/TheWeekend.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weekendButton.setIcon(icon4)
        self.weekendButton.setIconSize(QtCore.QSize(177, 177))
        self.weekendButton.setObjectName("weekendButton")
        self.interworldButton = QtWidgets.QPushButton(self.centralwidget)
        self.interworldButton.setGeometry(QtCore.QRect(264, 80, 180, 180))
        self.interworldButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.interworldButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/InterWorld.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.interworldButton.setIcon(icon5)
        self.interworldButton.setIconSize(QtCore.QSize(177, 177))
        self.interworldButton.setObjectName("interworldButton")
        self.acrossButton = QtWidgets.QPushButton(self.centralwidget)
        self.acrossButton.setGeometry(QtCore.QRect(744, 80, 180, 180))
        self.acrossButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.acrossButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images/AcrossTheSpiderVerse.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acrossButton.setIcon(icon6)
        self.acrossButton.setIconSize(QtCore.QSize(177, 177))
        self.acrossButton.setObjectName("acrossButton")
        self.intoButton = QtWidgets.QPushButton(self.centralwidget)
        self.intoButton.setGeometry(QtCore.QRect(516, 80, 180, 180))
        self.intoButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.intoButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Images/IntoTheSpiderVerse.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.intoButton.setIcon(icon7)
        self.intoButton.setIconSize(QtCore.QSize(177, 177))
        self.intoButton.setObjectName("intoButton")
        self.phonkText_2 = QtWidgets.QLabel(self.centralwidget)
        self.phonkText_2.setGeometry(QtCore.QRect(10, 40, 440, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.phonkText_2.setFont(font)
        self.phonkText_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.phonkText_2.setAlignment(QtCore.Qt.AlignCenter)
        self.phonkText_2.setObjectName("phonkText_2")
        self.cartoonText = QtWidgets.QLabel(self.centralwidget)
        self.cartoonText.setGeometry(QtCore.QRect(500, 5, 440, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.cartoonText.setFont(font)
        self.cartoonText.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.cartoonText.setAlignment(QtCore.Qt.AlignCenter)
        self.cartoonText.setObjectName("cartoonText")
        self.cartoonText_2 = QtWidgets.QLabel(self.centralwidget)
        self.cartoonText_2.setGeometry(QtCore.QRect(500, 40, 440, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.cartoonText_2.setFont(font)
        self.cartoonText_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.cartoonText_2.setAlignment(QtCore.Qt.AlignCenter)
        self.cartoonText_2.setObjectName("cartoonText_2")
        self.engSingerText = QtWidgets.QLabel(self.centralwidget)
        self.engSingerText.setGeometry(QtCore.QRect(20, 264, 440, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.engSingerText.setFont(font)
        self.engSingerText.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.engSingerText.setAlignment(QtCore.Qt.AlignCenter)
        self.engSingerText.setObjectName("engSingerText")
        self.engSingerText_2 = QtWidgets.QLabel(self.centralwidget)
        self.engSingerText_2.setGeometry(QtCore.QRect(20, 300, 440, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.engSingerText_2.setFont(font)
        self.engSingerText_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.engSingerText_2.setAlignment(QtCore.Qt.AlignCenter)
        self.engSingerText_2.setObjectName("engSingerText_2")
        self.rusSingerText = QtWidgets.QLabel(self.centralwidget)
        self.rusSingerText.setGeometry(QtCore.QRect(500, 264, 440, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.rusSingerText.setFont(font)
        self.rusSingerText.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.rusSingerText.setAlignment(QtCore.Qt.AlignCenter)
        self.rusSingerText.setObjectName("rusSingerText")
        self.rusSingerText_2 = QtWidgets.QLabel(self.centralwidget)
        self.rusSingerText_2.setGeometry(QtCore.QRect(500, 300, 440, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.rusSingerText_2.setFont(font)
        self.rusSingerText_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.rusSingerText_2.setAlignment(QtCore.Qt.AlignCenter)
        self.rusSingerText_2.setObjectName("rusSingerText_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/stars.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.phonkText.raise_()
        self.hensonnButton.raise_()
        self.imagineButton.raise_()
        self.arturButton.raise_()
        self.valeraButton.raise_()
        self.weekendButton.raise_()
        self.interworldButton.raise_()
        self.acrossButton.raise_()
        self.intoButton.raise_()
        self.phonkText_2.raise_()
        self.cartoonText.raise_()
        self.cartoonText_2.raise_()
        self.engSingerText.raise_()
        self.engSingerText_2.raise_()
        self.rusSingerText.raise_()
        self.rusSingerText_2.raise_()

        # Здесь происходит соединение кнопок с функциями.
        self.hensonnButton.clicked.connect(self.run_hensonn)
        self.interworldButton.clicked.connect(self.run_interworld)
        self.intoButton.clicked.connect(self.run_into)
        self.acrossButton.clicked.connect(self.run_across)
        self.weekendButton.clicked.connect(self.run_weekend)
        self.imagineButton.clicked.connect(self.run_imagine)
        self.arturButton.clicked.connect(self.run_artur)
        self.valeraButton.clicked.connect(self.run_valera)
        # Устанавливаем иконку окна.
        icon_path = "Images/silvericon.png"
        app_icon = QtGui.QIcon()
        app_icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(app_icon)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        # Здесь задаются названия текстов.
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Music Player"))
        self.phonkText.setText(_translate("mainWindow", "The Most Popular"))
        self.phonkText_2.setText(_translate("mainWindow", "Phonk Artists"))
        self.cartoonText.setText(_translate("mainWindow", "The Most Popular"))
        self.cartoonText_2.setText(_translate("mainWindow", "Cartoon Albums"))
        self.engSingerText.setText(_translate("mainWindow", "The Most Popular"))
        self.engSingerText_2.setText(_translate("mainWindow", "English Singers"))
        self.rusSingerText.setText(_translate("mainWindow", "The Most Popular"))
        self.rusSingerText_2.setText(_translate("mainWindow", "Russian Singers"))
    # Функции для запуска файлов.
    def run_hensonn(self):
        hensonn_path = "HensonnWindow.py"
        subprocess.Popen(["python", hensonn_path], shell=True)
    def run_interworld(self):
        hensonn_path = "InterworldWindow.py"
        subprocess.Popen(["python", hensonn_path], shell=True)
    def run_into(self):
        hensonn_path = "IntoWindow.py"
        subprocess.Popen(["python", hensonn_path], shell=True)
    def run_across(self):
        hensonn_path = "AcrossWindow.py"
        subprocess.Popen(["python", hensonn_path], shell=True)
    def run_weekend(self):
        hensonn_path = "WeekendWindow.py"
        subprocess.Popen(["python", hensonn_path], shell=True)
    def run_imagine(self):
        hensonn_path = "ImagineWindow.py"
        subprocess.Popen(["python", hensonn_path], shell=True)
    def run_artur(self):
        hensonn_path = "ArturWindow.py"
        subprocess.Popen(["python", hensonn_path], shell=True)
    def run_valera(self):
        hensonn_path = "ValeraWindow.py"
        subprocess.Popen(["python", hensonn_path], shell=True)
# Запуск окна.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())
