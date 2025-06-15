from PyQt5.QtCore import QUrlQuery, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

app = QApplication(sys.argv)
window = QMainWindow()
browser = QWebEngineView()
url = QUrl('http://google.com') # will change YouTube Embed

browser.load(url)
window.setCentralWidget(browser)
window.resize(1024, 768)
window.show()
sys.exit(app.exec_())
