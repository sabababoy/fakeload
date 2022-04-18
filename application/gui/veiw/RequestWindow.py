from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class AddRequestWindow(QMainWindow):
	def __init__(self, controller, main_window):
		super().__init__()
		self.main_window = main_window
		self.controller = controller
		self.setMinimumWidth(500)

		self.mainLayout = QVBoxLayout()
		self.mainWidget = QWidget()

		self.warning_label = QLabel('')
		self.type_choice = QComboBox()
		self.http_type = QComboBox()
		self.url = QLineEdit()
		self.verify = QCheckBox()
		self.confirm = QPushButton("Confirm")
		self.confirm.clicked.connect(lambda: self.controller.add_request_window_controller.confirm(self, self.main_window))
		self.cancel_button = QPushButton("Cancel")
		self.cancel_button.clicked.connect(lambda: self.controller.add_request_window_controller.cancel(self))
		self.requestLayout = QHBoxLayout()
		self.requestLayout.addWidget(self.type_choice)
		self.requestLayout.addWidget(self.http_type)
		self.requestLayout.addWidget(self.url)
		self.requestLayout.addWidget(self.verify)

		self.buttonsLayout = QHBoxLayout()
		self.buttonsLayout.addWidget(self.confirm)
		self.buttonsLayout.addWidget(self.cancel_button)

		self.http_type.addItem("https://")
		self.http_type.addItem("http://")

		self.type_choice.addItem("GET")
		self.type_choice.addItem("POST")
		self.type_choice.addItem("DELETE")


		self.mainLayout.addLayout(self.requestLayout)
		self.mainLayout.addWidget(self.warning_label)
		self.mainLayout.addLayout(self.buttonsLayout)
		self.mainWidget.setLayout(self.mainLayout)

		self.setCentralWidget(self.mainWidget)

class DeleteRequestWindow(QMainWindow):
	def __init__(self, controller, mainWindow):
		super().__init__()
		self.controller = controller
		self.mainWindow = mainWindow

		self.mainWidget = QWidget()
		self.choice = QComboBox()
		self.deleteButton = QPushButton("Confirm")
		self.cancelButton = QPushButton("Cancel")
		self.deleteButton.clicked.connect(lambda: self.controller.delete_request_window_controller.confirm(self, self.mainWindow))
		self.cancelButton.clicked.connect(lambda: self.controller.delete_request_window_controller.cancel(self))

		self.windowLayout = QVBoxLayout()
		self.choiceLayout = QHBoxLayout()
		self.buttonsLayout = QHBoxLayout()
		
		self.windowLayout.addLayout(self.choiceLayout)
		self.windowLayout.addLayout(self.buttonsLayout)
		self.mainWidget.setLayout(self.windowLayout)
		
		for request in self.controller.user.requests:
			self.choice.addItem(request.url)
		
		self.choiceLayout.addWidget(self.choice)
		self.buttonsLayout.addWidget(self.deleteButton)
		self.buttonsLayout.addWidget(self.cancelButton)

		self.setCentralWidget(self.mainWidget)

