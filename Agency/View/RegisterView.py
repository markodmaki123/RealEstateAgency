from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from RealEstateAgency.Agency.Application import config
from RealEstateAgency.Agency.View.MessageBox import messageBox


class RegisterView(QtWidgets.QMainWindow):
    def __init__(self, widget_stack, controller, manager):
        super(RegisterView, self).__init__()
        self._widgetStack = widget_stack
        self._controller = controller
        self._manager = manager

        loadUi(config.REGISTER_UI_PATH, self)
        self.setWindowTitle("Register")

        self.registerBtn.clicked.connect(self.register_btn_pressed)
        self.cancelBtn.clicked.connect(self.cancel_btn_pressed)

    @property
    def widget(self):
        return self._widgetStack

    def register_btn_pressed(self):
        user_info = {
            'pk': None,
            'name': self.nameTxt.text(),
            'surname': self.surnameTxt.text(),
            'address': self.addressTxt.text(),
            'email': self.emailTxt.text(),
            'password': self.passwordTxt.text(),
            'phone_number': self.phoneTxt.text(),
            'user_type': 0
        }

        print("Collected user information for registration:")
        for key, value in user_info.items():
            print(f"{key}: {value}")

        result = self._controller.register_user(user_info)
        if result:
            messageBox("Registration success", "Success")
            self._widgetStack.setCurrentIndex(0)
        else:
            messageBox("Registration failed", "Error")

    def cancel_btn_pressed(self):
        self._widgetStack.setCurrentIndex(0)
