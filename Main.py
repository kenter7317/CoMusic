import os

from PyQt5.QtCore import QUrlQuery, QUrl, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QListWidget, QListView, QDockWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
import VideoList

# Window Scheme
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        browser = QWebEngineView()
        html_path = os.path.abspath("Embed.html") # TODO WEBCHANNEL
        url = QUrl.fromLocalFile(html_path)

        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu("파일")

        exit_action = QAction("종료", self)
        exit_action.triggered.connect(self.close)
        menu_file.addAction(exit_action)

        list_dock = QDockWidget(self)
        list_widget = QListView(self)
        list_dock.setWidget(list_widget)
        list_dock.setFloating(True)
        list_dock.hide()
        list_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        list_action = QAction("리스트", self)
        list_action.triggered.connect(lambda: list_dock.show())

        menu_file.addAction(list_action)
        browser.load(url)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setCentralWidget(browser)
        self.resize(1024, 768)

class DiscordBot():
    def __init__(self): # TODO
        pass
    pass

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
