from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from http.cookiejar import Cookie
from ..model.Core import User
from ..veiw.CookieWindow import *
from ..veiw.RequestWindow import *

class Controller():

    def __init__(self):
        self.user = User()

    def show_requests_list(self, window):
        for i in self.user.requests:
            request_layout = QHBoxLayout()
            type_label = QLabel(i.type)
            url_label = QLabel(i.url)
            request_layout.addWidget(type_label)
            request_layout.addWidget(url_label)

            request_widget = QWidget()
            request_widget.setLayout(request_layout)
            window.requests_list_layout.addWidget(request_widget)

    def add_cookies(self, window):
        window.dialog = CookieWindow()
        window.dialog.show()

    def add_request(self, window):
        window.dialog = AddRequestWindow(window)
        window.dialog.show()

    def delete_request(self, window):
        window.dialog = DeleteRequestWindow(window)
        window.dialog.show()