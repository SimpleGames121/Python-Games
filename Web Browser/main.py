from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class Browser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Browser, self).__init__(*args,**kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("My Browser")
        self.window.setMinimumSize(1280,720)

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(50)

        self.go_btn = QPushButton("⌕")
        self.go_btn.setMinimumHeight(50)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(50)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(50)

        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))
        self.window.setLayout(self.layout)
        self.window.show()

        settings = QWebEngineSettings.globalSettings()
        settings.setAttribute(QWebEngineSettings.ErrorPageEnabled, True)

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)

        self.browser.setUrl(QUrl(url))


app = QApplication([])
window = Browser()
app.exec_()
