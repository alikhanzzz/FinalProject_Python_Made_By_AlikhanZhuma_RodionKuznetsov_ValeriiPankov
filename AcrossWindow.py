# Библиотека PyQt5 была установлена через команду 'pip install pyqt5' введённую в терминал.
# А вот PyQt5 работает благодаря фреймворку Qt.
# Здесь у нас импортируются отдельные модули.
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pygame
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon
class Ui_acrossWindow(object):
    def setupUi(self, acrossWindow):
        # Здесь у нас создаётся окно, тексты, кнопки, листы и также указываются их размеры, картинки, цвета и т.д.
        # Каждая кнопка, текст, лист или другой виджет, названы в зависимости их задачи.
        # Во многом весь интерфейс был создан при помощи приложения Qt Designer.
        acrossWindow.setObjectName("acrossWindow")
        acrossWindow.resize(960, 540)
        acrossWindow.setMinimumSize(QtCore.QSize(960, 540))
        acrossWindow.setMaximumSize(QtCore.QSize(960, 540))
        acrossWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0.125 rgba(0, 0, 0, 255), stop:1 rgba(240, 0, 15, 255));")
        self.centralwidget = QtWidgets.QWidget(acrossWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frameRight = QtWidgets.QFrame(self.centralwidget)
        self.frameRight.setGeometry(QtCore.QRect(353, 0, 607, 540))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frameRight.setFont(font)
        self.frameRight.setStyleSheet("border: 7px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-radius: 1em;")
        self.frameRight.setFrameShape(QtWidgets.QFrame.VLine)
        self.frameRight.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameRight.setObjectName("frameRight")
        self.frameLeft = QtWidgets.QFrame(self.centralwidget)
        self.frameLeft.setGeometry(QtCore.QRect(0, 0, 360, 540))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frameLeft.setFont(font)
        self.frameLeft.setStyleSheet("border: 7px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-radius: 1em;")
        self.frameLeft.setFrameShape(QtWidgets.QFrame.VLine)
        self.frameLeft.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameLeft.setObjectName("frameLeft")
        self.acrossLogo = QtWidgets.QLabel(self.centralwidget)
        self.acrossLogo.setGeometry(QtCore.QRect(30, 30, 300, 300))
        self.acrossLogo.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"")
        self.acrossLogo.setText("")
        self.acrossLogo.setPixmap(QtGui.QPixmap("Images/AcrossTheSpiderVerse.jpg"))
        self.acrossLogo.setScaledContents(True)
        self.acrossLogo.setObjectName("acrossLogo")
        self.acrossText = QtWidgets.QLabel(self.centralwidget)
        self.acrossText.setGeometry(QtCore.QRect(0, 335, 360, 45))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.acrossText.setFont(font)
        self.acrossText.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.acrossText.setAlignment(QtCore.Qt.AlignCenter)
        self.acrossText.setWordWrap(False)
        self.acrossText.setIndent(-1)
        self.acrossText.setObjectName("acrossText")
        self.frameLeftBack = QtWidgets.QFrame(self.centralwidget)
        self.frameLeftBack.setGeometry(QtCore.QRect(0, 0, 360, 540))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frameLeftBack.setFont(font)
        self.frameLeftBack.setStyleSheet("border: 7px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.frameLeftBack.setFrameShape(QtWidgets.QFrame.VLine)
        self.frameLeftBack.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameLeftBack.setObjectName("frameLeftBack")
        self.frameRightBack = QtWidgets.QFrame(self.centralwidget)
        self.frameRightBack.setGeometry(QtCore.QRect(360, 0, 600, 540))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frameRightBack.setFont(font)
        self.frameRightBack.setStyleSheet("border-right: 7px solid;\n"
"border-top: 7px solid;\n"
"border-bottom: 7px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.frameRightBack.setFrameShape(QtWidgets.QFrame.VLine)
        self.frameRightBack.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameRightBack.setObjectName("frameRightBack")
        self.listOfMusic = QtWidgets.QListWidget(self.centralwidget)
        self.listOfMusic.setGeometry(QtCore.QRect(380, 30, 550, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.listOfMusic.setFont(font)
        self.listOfMusic.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: 0px;\n"
"color: rgb(255, 255, 255);")
        self.listOfMusic.setObjectName("listOfMusic")
        self.nowPlayingText = QtWidgets.QLabel(self.centralwidget)
        self.nowPlayingText.setGeometry(QtCore.QRect(380, 345, 550, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.nowPlayingText.setFont(font)
        self.nowPlayingText.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.nowPlayingText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nowPlayingText.setObjectName("nowPlayingText")
        self.musicSlider = QtWidgets.QSlider(self.centralwidget)
        self.musicSlider.setGeometry(QtCore.QRect(380, 450, 550, 30))
        self.musicSlider.setStyleSheet("QSlider {\n"
"    background: transparent;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 2px;\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #000000;\n"
"    border: 3px solid #000000;\n"
"    width: 2px;\n"
"    margin: -12px 0; \n"
"}\n"
"")
        self.musicSlider.setOrientation(QtCore.Qt.Horizontal)
        self.musicSlider.setObjectName("musicSlider")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(100, 420, 75, 75))
        self.playButton.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.playButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/playbutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setIconSize(QtCore.QSize(75, 75))
        self.playButton.setObjectName("playButton")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(185, 420, 75, 75))
        self.pauseButton.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pauseButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/pausebutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon1)
        self.pauseButton.setIconSize(QtCore.QSize(75, 75))
        self.pauseButton.setObjectName("pauseButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(265, 420, 80, 80))
        self.nextButton.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.nextButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/nextbutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon2)
        self.nextButton.setIconSize(QtCore.QSize(80, 80))
        self.nextButton.setObjectName("nextButton")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(15, 420, 80, 80))
        self.prevButton.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.prevButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/prevbutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevButton.setIcon(icon3)
        self.prevButton.setIconSize(QtCore.QSize(80, 80))
        self.prevButton.setObjectName("prevButton")
        self.statusOfMusicText = QtWidgets.QLabel(self.centralwidget)
        self.statusOfMusicText.setGeometry(QtCore.QRect(380, 390, 550, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.statusOfMusicText.setFont(font)
        self.statusOfMusicText.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.statusOfMusicText.setText("##########")
        self.statusOfMusicText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statusOfMusicText.setObjectName("statusOfMusicText")
        self.spiderText = QtWidgets.QLabel(self.centralwidget)
        self.spiderText.setGeometry(QtCore.QRect(0, 375, 360, 45))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.spiderText.setFont(font)
        self.spiderText.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.spiderText.setAlignment(QtCore.Qt.AlignCenter)
        self.spiderText.setObjectName("spiderText")
        self.frameLeftBack.raise_()
        self.frameRight.raise_()
        self.frameLeft.raise_()
        self.acrossLogo.raise_()
        self.acrossText.raise_()
        self.frameRightBack.raise_()
        self.listOfMusic.raise_()
        self.nowPlayingText.raise_()
        self.musicSlider.raise_()
        self.playButton.raise_()
        self.pauseButton.raise_()
        self.nextButton.raise_()
        self.prevButton.raise_()
        self.statusOfMusicText.raise_()
        self.spiderText.raise_()

        self.timeOfMusicText = QtWidgets.QLabel(self.centralwidget)
        self.timeOfMusicText.setGeometry(QtCore.QRect(380, 465, 550, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.timeOfMusicText.setFont(font)
        self.timeOfMusicText.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                           "color: rgb(255, 255, 255);")
        self.timeOfMusicText.setText("00:00")
        self.timeOfMusicText.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.timeOfMusicText.setObjectName("timeOfMusicText")

        self.lenghtOfMusicText = QtWidgets.QLabel(self.centralwidget)
        self.lenghtOfMusicText.setGeometry(QtCore.QRect(855, 465, 550, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lenghtOfMusicText.setFont(font)
        self.lenghtOfMusicText.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                             "color: rgb(255, 255, 255);")
        self.lenghtOfMusicText.setText("00:00")
        self.lenghtOfMusicText.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lenghtOfMusicText.setObjectName("lenghtOfMusicText")

        acrossWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(acrossWindow)
        QtCore.QMetaObject.connectSlotsByName(acrossWindow)
        # Здесь происходит соединение кнопок с функциями.
        self.playButton.clicked.connect(self.play_music)
        self.pauseButton.clicked.connect(self.pause_music)
        self.nextButton.clicked.connect(self.play_next)
        self.prevButton.clicked.connect(self.play_previous)

        pygame.init()
        pygame.mixer.init()
        # Здесь указывается путь, название и общая длительность всей музыки.
        self.music_files = [
                ("AcrossTheSpiderVerse Music/Metro Boomin, Swae Lee, Lil Wayne & Offset - Annihilate.mp3", "Annihilate (Metro Boomin, Swae Lee, etc)", 231),
                ("AcrossTheSpiderVerse Music/Don Toliver, 21 Savage & 2 Chainz - Givin' Up (Not The One).mp3", "Givin' Up (Don Toliver, 21 Savage & 2 Chainz)", 234),
                ("AcrossTheSpiderVerse Music/Metro Boomin, A$AP Rocky & Roisee - Am I Dreaming.mp3", "Am I Dreaming (Metro Boomin, etc)", 256),
                ("AcrossTheSpiderVerse Music/Metro Boomin, Swae Lee, NAV & A Boogie Wit Da Hoodie - Calling.mp3", "Calling (Metro Boomin, Swae Lee, etc)", 219),
                ("AcrossTheSpiderVerse Music/Metro Boomin, Don Toliver & Lil Uzi Vert - Home.mp3", "Home (Metro Boomin, Don Toliver, etc)", 195),
                ("AcrossTheSpiderVerse Music/Metro Boomin & Coi Leray - Self Love.mp3", "Self Love (Metro Boomin & Coi Leray)", 189),
                ("AcrossTheSpiderVerse Music/EI8HT & Offset - Silk & Cologne (Spider-Verse Remix).mp3", "Silk & Cologne (EI8HT & Offset)", 162),
                ("AcrossTheSpiderVerse Music/Metro Boomin & James Blake - Hummingbird.mp3", "Hummingbird (Metro Boomin & James Blake)", 319),
                ("AcrossTheSpiderVerse Music/Metro Boomin, Don Toliver, Wizkid, BEAM & Toian - Link Up.mp3", "Link Up (Metro Boomin, Don Toliver, etc)", 195),
        ]
        self.current_index = 0
        for file_path, display_name, music_len in self.music_files:
                self.add_music_to_list(file_path, display_name)
        # Здесь происходит соединение кнопок с функциями.
        self.nextButton.clicked.connect(self.play_next_with_animation)
        self.prevButton.clicked.connect(self.play_prev_with_animation)

        self.animationNextButton_timer = QTimer(self.centralwidget)
        self.animationNextButton_timer.timeout.connect(self.resetNextButton_button_icon)

        self.animationPrevButton_timer = QTimer(self.centralwidget)
        self.animationPrevButton_timer.timeout.connect(self.resetPrevButton_button_icon)

        self.play_button_state = "normal"
        self.pause_button_state = "normal"

        self.playButton.clicked.connect(self.playButton_clicked)
        self.pauseButton.clicked.connect(self.pauseButton_clicked)

        self.slider_update_timer = QTimer(self.centralwidget)
        self.slider_update_timer.timeout.connect(self.update_slider_position)
        self.slider_update_timer.start(100)

        self.current_position = 0

        self.time_update_timer = QTimer(self.centralwidget)
        self.time_update_timer.timeout.connect(self.update_time_text)
        self.time_update_timer.start(100)

        self.musicSlider.sliderMoved.connect(self.set_music_position)

        self.musicSlider.sliderReleased.connect(self.set_music_position)

        self.musicSlider.sliderMoved.connect(self.slider_moved)
        self.musicSlider.sliderReleased.connect(self.slider_released)
        # Устанавливаем иконку окна.
        icon_path = "Images/silvericon.png"
        app_icon = QtGui.QIcon()
        app_icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(app_icon)
    def retranslateUi(self, acrossWindow):
        # Здесь задаются названия текстов.
        _translate = QtCore.QCoreApplication.translate
        acrossWindow.setWindowTitle(_translate("acrossWindow", "Spider-Man: Across The Spider-Verse (Album)"))
        self.acrossText.setText(_translate("acrossWindow", "Across The"))
        self.nowPlayingText.setText(_translate("acrossWindow", "Now Playing:"))
        self.spiderText.setText(_translate("acrossWindow", "Spider-Verse"))
    def play_music(self):
        # Функция запуска музыки.
        file_path, display_name, music_length = self.music_files[self.current_index]
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        self.statusOfMusicText.setText(f"{display_name}")

        music_length = pygame.mixer.Sound(file_path).get_length()
        self.musicSlider.setMaximum(int(music_length * 1000))

        music_length_text = "{:02}:{:02}".format(int(music_length) // 60, int(music_length) % 60)
        self.lenghtOfMusicText.setText(music_length_text)

        self.current_position = 0
        self.musicSlider.setValue(0)
        self.update_position()

        self.slider_update_timer.start(100)
        self.time_update_timer.start(100)
    def pause_music(self):
        # Функция паузы музыки.
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    def play_next(self):
        # Функция включения следующей музыки.
        self.current_index = (self.current_index + 1) % len(self.music_files)
        self.play_music()
    def play_previous(self):
        # Функция включения предыдущей музыки.
        self.current_index = (self.current_index - 1) % len(self.music_files)
        self.play_music()
    def add_music_to_list(self, file_path, display_name):
        # Функция добавления музыки в listOfMusic.
        item = QtWidgets.QListWidgetItem(display_name)
        self.listOfMusic.addItem(item)
    def play_next_with_animation(self):
        # Функция включения кнопки nextButton при нажатии.
        icon_path = "Images/nextbuttonInverse.png"
        self.nextButton.setIcon(QIcon(icon_path))
        self.animationNextButton_timer.start(100)
        if self.pause_button_state == "inverse":
            inverse_icon_path_play = "Images/playbuttonInverse.png"
            original_icon_path_pause = "Images/pausebutton.png"
            self.playButton.setIcon(QIcon(inverse_icon_path_play))
            self.play_button_state = "inverse"
            self.pauseButton.setIcon(QIcon(original_icon_path_pause))
            self.pause_button_state = "normal"
            QtWidgets.QApplication.processEvents()
        if self.play_button_state == "normal":
            inverse_icon_path_play = "Images/playbuttonInverse.png"
            original_icon_path_pause = "Images/pausebutton.png"
            self.playButton.setIcon(QIcon(inverse_icon_path_play))
            self.play_button_state = "inverse"
            self.pauseButton.setIcon(QIcon(original_icon_path_pause))
            self.pause_button_state = "normal"
            QtWidgets.QApplication.processEvents()
    def play_prev_with_animation(self):
        # Функция включения кнопки prevButton при нажатии.
        icon_path = "Images/prevbuttonInverse.png"
        self.prevButton.setIcon(QIcon(icon_path))
        self.animationPrevButton_timer.start(100)
        if self.pause_button_state == "inverse":
            inverse_icon_path_play = "Images/playbuttonInverse.png"
            original_icon_path_pause = "Images/pausebutton.png"
            self.playButton.setIcon(QIcon(inverse_icon_path_play))
            self.play_button_state = "inverse"
            self.pauseButton.setIcon(QIcon(original_icon_path_pause))
            self.pause_button_state = "normal"
            QtWidgets.QApplication.processEvents()
        if self.play_button_state == "normal":
            inverse_icon_path_play = "Images/playbuttonInverse.png"
            original_icon_path_pause = "Images/pausebutton.png"
            self.playButton.setIcon(QIcon(inverse_icon_path_play))
            self.play_button_state = "inverse"
            self.pauseButton.setIcon(QIcon(original_icon_path_pause))
            self.pause_button_state = "normal"
            QtWidgets.QApplication.processEvents()
    def resetNextButton_button_icon(self):
        # Функция выключения кнопки nextButton.
        original_icon_path = "Images/nextbutton.png"
        self.nextButton.setIcon(QIcon(original_icon_path))
        self.animationNextButton_timer.stop()
    def resetPrevButton_button_icon(self):
        # Функция выключения кнопки prevButton.
        original_icon_path = "Images/prevbutton.png"
        self.prevButton.setIcon(QIcon(original_icon_path))
        self.animationPrevButton_timer.stop()
    def playButton_clicked(self):
        # Функция интерактивности кнопки playButton при нажатии.
        icon_path_play = "Images/playbuttonInverse.png"
        self.playButton.setIcon(QIcon(icon_path_play))
        self.play_button_state = "inverse"
        QtWidgets.QApplication.processEvents()
        if self.pause_button_state == "inverse":
            original_icon_path_pause = "Images/pausebutton.png"
            self.pauseButton.setIcon(QIcon(original_icon_path_pause))
            self.pause_button_state = "normal"
            QtWidgets.QApplication.processEvents()
    def pauseButton_clicked(self):
        # Функция интерактивности кнопки pauseButton при нажатии.
        if self.pause_button_state == "normal":
            original_icon_path_play = "Images/playbutton.png"
            inverse_icon_path_pause = "Images/pausebuttonInverse.png"
            self.playButton.setIcon(QIcon(original_icon_path_play))
            self.play_button_state = "normal"
            self.pauseButton.setIcon(QIcon(inverse_icon_path_pause))
            self.pause_button_state = "inverse"
            QtWidgets.QApplication.processEvents()
        elif self.pause_button_state == "inverse":
            inverse_icon_path_play = "Images/playbuttonInverse.png"
            original_icon_path_pause = "Images/pausebutton.png"
            self.playButton.setIcon(QIcon(inverse_icon_path_play))
            self.play_button_state = "inverse"
            self.pauseButton.setIcon(QIcon(original_icon_path_pause))
            self.pause_button_state = "normal"
            QtWidgets.QApplication.processEvents()
    def update_slider_position(self):
        # Функция обновления позиции musicSlider.
        if pygame.mixer.music.get_busy() and not self.musicSlider.isSliderDown():
            current_position = pygame.mixer.music.get_pos()
            self.current_position = current_position
            self.musicSlider.setValue(current_position)
            elapsed_time = QTime(0, 0).addMSecs(self.current_position)
            self.timeOfMusicText.setText(elapsed_time.toString("mm:ss"))
    def update_time_text(self):
        # Функция обновления времени в timeOfMusicText.
        if pygame.mixer.music.get_busy() and not self.musicSlider.isSliderDown():
            self.current_position = pygame.mixer.music.get_pos()
            elapsed_time = QTime(0, 0).addMSecs(self.current_position)
            self.timeOfMusicText.setText(elapsed_time.toString("mm:ss"))
    def set_music_position(self):
        # Функция перемотки позиции musicSlider.
        if pygame.mixer.music.get_busy():
            position = self.musicSlider.value()
            pygame.mixer.music.set_pos(position / 1000.0)
            self.current_position = position
            elapsed_time = QTime(0, 0).addMSecs(self.current_position)
            self.timeOfMusicText.setText(elapsed_time.toString("mm:ss"))
    def update_position(self):
        # Функция обновления позиции после перемотки musicSlider.
        if pygame.mixer.music.get_busy():
            current_position = pygame.mixer.music.get_pos()
            self.current_position = current_position
            self.musicSlider.setValue(current_position)
            elapsed_time = QTime(0, 0).addMSecs(self.current_position)
            self.timeOfMusicText.setText(elapsed_time.toString("mm:ss"))
        else:
            self.slider_update_timer.stop()
            self.time_update_timer.stop()
    def slider_moved(self):
        # Функция связанная с позицией musicSlider.
        if pygame.mixer.music.get_busy():
            self.slider_update_timer.stop()
            position = self.musicSlider.value()
            elapsed_time = QTime(0, 0).addMSecs(position)
            self.timeOfMusicText.setText(elapsed_time.toString("mm:ss"))
    def slider_released(self):
        # Функция связанная с позицией musicSlider.
        if pygame.mixer.music.get_busy():
            position = self.musicSlider.value()
            self.temporary_position = position
            pygame.mixer.music.stop()
            pygame.mixer.music.play(start=self.temporary_position / 1000.0)
            elapsed_time = QTime(0, 0).addMSecs(self.temporary_position)
            self.timeOfMusicText.setText(elapsed_time.toString("mm:ss"))
            self.slider_update_timer.stop()
            self.time_update_timer.stop()
# Запуск окна.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_acrossWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())