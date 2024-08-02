import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

DOMAIN_MAP = {
    'zyg.zyg': 'zygvlogs.site',
    #'babrai.babrai': 'babrai.com',
    'millieb.millie': 'zygvlogs.site/millieb',}

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ZygBrowser")
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.url_entry = QLineEdit()
        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.fetch_content)

        layout = QVBoxLayout()
        layout.addWidget(self.url_entry)
        layout.addWidget(self.go_button)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def fetch_content(self):
        url = self.url_entry.text().strip()
        parsed_url = QUrl(url)
        full_domain = parsed_url.host()

        if full_domain not in DOMAIN_MAP:
            QMessageBox.critical(self, "Error", "No simulated redirect for this domain")
            return

       
        real_domain = DOMAIN_MAP[full_domain]
        real_url = parsed_url.toString().replace(full_domain, real_domain)

        self.browser.setUrl(QUrl(real_url))

app = QApplication(sys.argv)
window = SimpleBrowser()
window.show()
sys.exit(app.exec_())
