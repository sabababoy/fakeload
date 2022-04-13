from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        
        self.controller = controller
        self.setFixedWidth(600)
        self.setMaximumHeight(500)

        self.app = QWidget()
        self.app_layout = QVBoxLayout()
        self.app.setLayout(self.app_layout)

        self.setCentralWidget(self.app)

        self.top_layout = QHBoxLayout()

        self.add_cookie_button = QPushButton('Set Cookies')
        self.add_cookie_button.clicked.connect(lambda: self.controller.main_window_controller.add_cookies(self))

        self.bottom_layout = QHBoxLayout()
        self.add_request_button = QPushButton('Add')
        self.add_request_button.clicked.connect(lambda: self.controller.add_request_window_controller.add_request(self))
        self.delete_request_button = QPushButton('Delete')
        self.delete_request_button.clicked.connect(lambda: self.controller.delete_request_window_controller.delete_request(self))
        self.start_button = QPushButton('Start')
        self.start_button.setFixedHeight(50)
        self.start_button.setStyleSheet("background-color: green")
        self.start_button.setEnabled(False)
        self.start_button.clicked.connect(lambda: self.controller.main_window_controller.start(self))

        self.req_lbl = QLabel('No requests')

        self.requests_list = []

        self.top_layout.addWidget(self.req_lbl)
        self.top_layout.addWidget(self.add_cookie_button)

        self.bottom_layout.addWidget(self.add_request_button)
        self.bottom_layout.addWidget(self.delete_request_button)

        self.requests_list_layout = QVBoxLayout()
        self.requests_list_widget = QWidget()
        self.requests_list_widget.setLayout(self.requests_list_layout)
        self.scroll_area = QScrollArea()
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.hide()
        self.scroll_area.setWidget(self.requests_list_widget)

        self.app_layout.addLayout(self.top_layout)
        self.app_layout.addWidget(self.scroll_area)
        self.app_layout.addLayout(self.bottom_layout)
        self.app_layout.addWidget(self.start_button)

        self.controller.main_window_controller.show_requests_list(self)
