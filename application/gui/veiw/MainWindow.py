from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        
        self.controller = controller

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

        self.req_lbl = QLabel('Requests:')

        self.top_layout.addWidget(self.req_lbl)
        self.top_layout.addWidget(self.add_cookie_button)

        self.bottom_layout.addWidget(self.add_request_button)
        self.bottom_layout.addWidget(self.delete_request_button)


        self.requests_list_layout = QVBoxLayout()

        self.app_layout.addLayout(self.top_layout)
        self.app_layout.addLayout(self.requests_list_layout)
        self.app_layout.addLayout(self.bottom_layout)

        self.controller.main_window_controller.show_requests_list(self)
