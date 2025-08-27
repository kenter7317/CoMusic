import os

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
import clazz.PluginRepository
from clazz.ListController import ListController


class Backend(QObject):

    repository : clazz.PluginRepository
    controller : ListController

    def initPluginRepository(self):
        repository = clazz.PluginRepository.PluginRepository()
        pass


    def initListController(self):
        controller = clazz.ListController.ListController()
        pass

# Window Scheme




class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        backend = Backend()
        backend.initPluginRepository()
        backend.initListController()
        self.create_ui()
        # browser = QWebEngineView()
        # html_path = os.path.abspath("Embed.html") # TODO WEBCHANNEL
        # url = QUrl.fromLocalFile(html_path)
        #
        # menu_bar = self.menuBar()
        # menu_file = menu_bar.addMenu("파일")
        #
        # exit_action = QAction("종료", self)
        # exit_action.triggered.connect(self.close)
        # menu_file.addAction(exit_action)
        #
        # self.channel = QWebChannel(self)
        # self.backend = Backend()
        # self.channel.registerObject('backend', self.backend)
        # browser.page().setWebChannel(self.channel)
        #
        # list_dock = QDockWidget(self)
        # list_widget = QListView(self)
        # list_dock.setWidget(list_widget)
        # list_dock.setFloating(True)
        # list_dock.hide()
        # list_dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        # list_action = QAction("리스트", self)
        # list_action.triggered.connect(lambda: list_dock.show())
        #
        # menu_file.addAction(list_action)
        # browser.load(url)
        #
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setCentralWidget(browser)
        # self.resize(1024, 768)

    def create_ui(self):
        pass


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
