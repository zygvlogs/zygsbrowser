import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

DOMAIN_MAP = {
    'home.zyg': 'zygvlogs.site/homedex',
    'zyg.zyg': 'zygvlogs.site',
    'wikipedia.babrai': 'wikipedia.org',
    'millieb.millie': 'zygvlogs.site/millieb',
    'rickroll.zyg': 'icegif.com/wp-content/uploads/2023/01/icegif-162.gif',
    'pinguins.babrai': 'i.pinimg.com/originals/0f/31/53/0f3153d46f659b681ac9b28b8d9872bb.gif',
    'grass.zyg': 'i.kym-cdn.com/editorials/icons/mobile/000/004/533/tgcover.jpg',
    }

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

         # Load home page
        self.load_home_page()

    def load_home_page(self):
        self.url_entry.setText("http://home.zyg")
        self.fetch_content()

    def fetch_content(self):
        url = self.url_entry.text().strip()
        parsed_url = QUrl(url)
        full_domain = parsed_url.host()

        if full_domain not in DOMAIN_MAP:
            QMessageBox.critical(self, "Error", "Nothing was found or use http://")
            return

       
        real_domain = DOMAIN_MAP[full_domain]
        real_url = parsed_url.toString().replace(full_domain, real_domain)

        self.browser.setUrl(QUrl(real_url))

app = QApplication(sys.argv)
window = SimpleBrowser()
window.show()
sys.exit(app.exec_())
