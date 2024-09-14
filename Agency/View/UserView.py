from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class UserView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.name_field = QLineEdit(self)
        self.name_field.setPlaceholderText("Enter Name")
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_field)

        self.email_field = QLineEdit(self)
        self.email_field.setPlaceholderText("Enter Email")
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_field)

        self.password_field = QLineEdit(self)
        self.password_field.setPlaceholderText("Enter Password")
        self.password_field.setEchoMode(QLineEdit.Password)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_field)

        self.register_button = QPushButton("Register", self)
        self.register_button.clicked.connect(self.register_user)
        layout.addWidget(self.register_button)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login_user)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def register_user(self):
        user_info = {
            'name': self.name_field.text(),
            'email': self.email_field.text(),
            'password': self.password_field.text(),
        }
        result = self.controller.register_user(user_info)
        if result:
            QMessageBox.information(self, "Success", "User Registered Successfully")
        else:
            QMessageBox.warning(self, "Error", "Failed to Register User")

    def login_user(self):
        email = self.email_field.text()
        password = self.password_field.text()
        result = self.controller.login_user(email, password)
        if result:
            QMessageBox.information(self, "Success", "Login Successful")
        else:
            QMessageBox.warning(self, "Error", "Invalid Credentials")

