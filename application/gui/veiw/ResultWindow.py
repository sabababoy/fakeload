from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from requests import request

class ResultWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()

        self.request = QComboBox()
        self.request.currentIndexChanged.connect(lambda: self.controller.result_window_controller.show_response(self))
        self.request.hide()
        self.response = QLabel()

        self.response_number = QLabel()
        self.response_number.hide()

        self.no_responses_label = QLabel('There are no responses')

        self.scroll_area = QScrollArea()
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.response)
        self.scroll_area.hide()

        self.main_layout.addWidget(self.no_responses_label)
        self.main_layout.addWidget(self.request)
        self.main_layout.addWidget(self.response_number)
        self.main_layout.addWidget(self.scroll_area)

        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        self.controller.result_window_controller.list_requests(self)