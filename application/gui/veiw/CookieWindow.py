from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *


class CookieWindow(QMainWindow):
	def __init__(self, controller):
		
		super().__init__()
		self.controller = controller
		self.setMinimumWidth(500)

		self.add_cookie_button = QPushButton('Add')
		self.delete_cookie_button = QPushButton('Delete')
		self.clear_all_cookies_button = QPushButton('Clear all')

		self.cookie_window_layout = QVBoxLayout()
		self.cookie_window = QWidget()
		self.cookie_window.setLayout(self.cookie_window_layout)

		self.setCentralWidget(self.cookie_window)

		self.menu_layout = QHBoxLayout()

		self.menu_layout.addWidget(self.add_cookie_button)
		self.menu_layout.addWidget(self.delete_cookie_button)
		self.menu_layout.addWidget(self.clear_all_cookies_button)

		self.cookie_window_layout.addLayout(self.menu_layout)

		self.controller.cookies_window_controller.show_cookies(self)

		self.add_cookie_button.clicked.connect(lambda: self.controller.cookies_window_controller.add_cookie(self))
		self.delete_cookie_button.clicked.connect(lambda: self.controller.cookies_window_controller.delete_cookie(self))
		self.clear_all_cookies_button.clicked.connect(lambda: self.controller.cookies_window_controller.clear_all(self))

class AddCookieWindow(QMainWindow):
	def __init__(self, controller):
		super().__init__()
		self.controller = controller

		self.setFixedWidth(305)
		
		self.addCookieForm = QWidget()
		self.mainLayout = QVBoxLayout()

		self.form = QFormLayout()
		self.form.addRow(QLabel("Required arguments:"))

		self.name = QLineEdit()
		self.value = QLineEdit()
		self.domain = QLineEdit()
		self.version = QLineEdit()
		self.port = QLineEdit()
		self.path = QLineEdit()
		self.comment = QLineEdit()
		self.secure = QCheckBox()

		self.form.addRow("Name:", self.name)
		self.form.addRow("Value:", self.value)
		self.form.addRow("Secure:", self.secure)
		self.form.addRow("Domain:", self.domain)
		self.form.addRow(QLabel("Optoinal arguments:"))
		self.form.addRow("Version", self.version)
		self.form.addRow("Port:", self.port)
		self.form.addRow("Path:", self.path)
		self.form.addRow("Comment:", self.comment)

		self.buttons = QHBoxLayout()
		self.ok_button = QPushButton("Ok")
		self.ok_button.clicked.connect(lambda: self.controller.cookies_window_controller.ok(self))
		self.cancel_button = QPushButton("Cancel")
		self.cancel_button.clicked.connect(lambda: self.controller.cookies_window_controller.cancel(self))
		self.buttons.addWidget(self.ok_button)
		self.buttons.addWidget(self.cancel_button)

		self.warning_label = QLabel()

		self.mainLayout.addLayout(self.form)
		self.mainLayout.addLayout(self.buttons)
		self.mainLayout.addWidget(self.warning_label)

		self.addCookieForm.setLayout(self.mainLayout)
		
		self.setCentralWidget(self.addCookieForm)
	

class DeleteCookieWindow(QMainWindow):
	def __init__(self, controller):
		super().__init__()

		self.controller = controller

		self.mainWidget = QWidget()
		self.choice = QComboBox()
		self.deleteButton = QPushButton("Delete")
		self.cancelButton = QPushButton("Cancel")
		self.deleteButton.clicked.connect(lambda: self.controller.cookies_window_controller.delete(self))
		self.cancelButton.clicked.connect(lambda: self.controller.cookies_window_controller.cancel(self))

		self.windowLayout = QVBoxLayout()
		self.choiceLayout = QHBoxLayout()
		self.buttonsLayout = QHBoxLayout()
		
		self.windowLayout.addLayout(self.choiceLayout)
		self.windowLayout.addLayout(self.buttonsLayout)
		self.mainWidget.setLayout(self.windowLayout)
		
		
		for cookie in self.controller.user.session.cookies:
			self.choice.addItem(cookie.name)
		
		self.choiceLayout.addWidget(self.choice)
		self.buttonsLayout.addWidget(self.deleteButton)
		self.buttonsLayout.addWidget(self.cancelButton)

		self.setCentralWidget(self.mainWidget)