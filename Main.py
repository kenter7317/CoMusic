from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

app = QApplication(sys.argv)
window = QMainWindow()
browser = QWebEngineView()

browser.load("https://www.naver.com")
window.setCentralWidget(browser)
window.resize(1024, 768)
window.show()
sys.exit(app.exec_())
