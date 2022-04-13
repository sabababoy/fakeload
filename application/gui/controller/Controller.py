from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from http.cookiejar import Cookie

from requests import request
from ..veiw.MainWindow import MainWindow
from ..veiw.CookieWindow import *
from ..veiw.RequestWindow import *

class Controller():

    def __init__(self, user):
        self.user = user
        self.main_window_controller = MainWindowController(self)
        self.cookies_window_controller = CookiesWindowController(self)
        self.add_request_window_controller = AddRequestsWindowController(self)
        self.delete_request_window_controller = DeleteRequestWindowController(self)

        app = QApplication([])

        window = MainWindow(self)
        window.show()

        app.exec()


class MainWindowController():
    def __init__(self, mainController):
        self.mainController = mainController
        self.requests_list = []

    def add_cookies(self, window):
        dialog = CookieWindow(self.mainController)
        dialog.show()

    def add_request(self, window):
        window.dialog = AddRequestWindow(self.mainController,window)
        window.dialog.show()

    def show_requests_list(self, window):
        window.requests_list = []
        if len(self.mainController.user.requests):
            window.req_lbl.setText('Requests:')
        for i in self.mainController.user.requests:
            window.start_button.setEnabled(True)
            request_layout = QHBoxLayout()
            type_label = QLabel(i.type)
            url_label = QLabel(i.url)
            request_layout.addWidget(type_label)
            request_layout.addWidget(url_label)
            request_widget = QWidget()
            request_widget.setLayout(request_layout)
            window.requests_list.append(request_widget)
        for req in window.requests_list:
            window.requests_list_layout.addWidget(req)
        
        window.scroll_area.show()

    def send_requests(self, window):
        for request in window.requests_list:
            try:
                response = self.mainController.user.send(self.mainController.user.requests[window.requests_list.index(request)])
                if str(response) == "<Response [200]>":
                    request.children()[1].setStyleSheet("color:green")
                    request.children()[2].setStyleSheet("color:green")
                else:
                    request.children()[1].setStyleSheet("color:yellow")
                    request.children()[2].setStyleSheet("color:ywllow")
            except:
                request.children()[1].setStyleSheet("color:red")
                request.children()[2].setStyleSheet("color:red")

    def start(self, window):
        window.start_button.setEnabled(False)
        window.start_button.setStyleSheet("background-color:grey")
        
        self.send_requests(window)

        window.start_button.setEnabled(True)
        window.start_button.setStyleSheet("background-color:green")
        

class CookiesWindowController():
    def __init__(self, mainController):
        self.mainController = mainController

    def show_cookies(self, window):
        if len(self.mainController.user.cookies):
            window.cookie_label = QLabel('Cookies:')
            window.cookie_window_layout.addWidget(window.cookie_label)
            for cookie in self.mainController.user.cookies:
                window.cookie_window_layout.addWidget(QLabel(str(cookie)))

        else:
            window.cookie_label = QLabel('No cookies')
            window.cookie_window_layout.addWidget(window.cookie_label,  alignment=Qt.AlignmentFlag.AlignHCenter)

    def add_cookie(self, window):
        window.dialog = AddCookieWindow(self.mainController)
        window.dialog.show()
        window.close()
	
    def delete_cookie(self, window):
        window.dialog = DeleteCookieWindow(self.mainController)
        window.dialog.show()
        window.close()

    def ok(self, window):
        if (" " in window.domain.text() or " " in window.name.text() or " " in window.path.text()):
            window.warning_label.setText("Requierd arguments cannot contain spaces.")
            window.warning_label.setStyleSheet("color: red")
        elif (window.name.text() != '') and (window.value.text() != '') and (window.domain.text() != ''):
            window.controller.user.add_cookie(window.name.text(), window.value.text(), window.domain.text(), window.secure.isChecked(), port=window.port.text(), version=window.version.text(), path=window.path.text(), comment=window.comment.text())
            window.dialog = CookieWindow(self.mainController)
            window.dialog.show()
            window.close()
        elif window.warning_label.text() != "You must specify all of the required arguments.":
            window.warning_label.setText("You must specify all of the required arguments.")
            window.warning_label.setStyleSheet("color: red")

    def cancel(self, window):
        window.dialog = CookieWindow(self.mainController)
        window.dialog.show()
        window.close()

    def delete(self, window):
        if window.choice.currentIndex() >= 0:
            window.controller.user.cookies.pop(window.choice.currentIndex())
            window.dialog = CookieWindow(self.mainController)
            window.dialog.show()
            window.close()

class AddRequestsWindowController():
    def __init__(self, mainController):
        self.mainController = mainController

    def add_request(self, window):
        window.dialog = AddRequestWindow(self.mainController, window)
        window.dialog.show()

    def confirm(self, window, main_window):
        if window.url.text() != '' and ' ' not in window.url.text():
            window.controller.user.add_request(window.type_choice.currentText(), window.url.text(),  window.verify.isChecked())
            window.close()
            main_window.close()
            window.dialog = MainWindow(self.mainController)
            window.dialog.show()
        elif ' ' in window.url.text():
            window.warning_label.setText("Url cannot contain spaces")
            window.warning_label.setStyleSheet("color: red")
        else:
            window.warning_label.setText("You must specify url. Example: google.com")
            window.warning_label.setStyleSheet("color: red")

    def cancel(self, window):
        window.close()

class DeleteRequestWindowController():
    def __init__(self, mainController):
        self.mainController = mainController

    def delete_request(self, window):
        window.dialog = DeleteRequestWindow(self.mainController, window)
        window.dialog.show()

    def confirm(self, window, mainWindow):
        if window.choice.currentIndex() >= 0:
            window.controller.user.requests.pop(window.choice.currentIndex())
            mainWindow.close()
            window.dialog = MainWindow(self.mainController)
            window.dialog.show()
            window.close()
    
    def cancel(self, window):
        window.close()
