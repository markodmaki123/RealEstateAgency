from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from RealEstateAgency.Agency.Application.config import REGISTER_UI_PATH

class RegisterView(QtWidgets.QMainWindow):
    def __init__(self, stackedWidgetP, controller, manager):
        super(RegisterView, self).__init__()
        self._widgetStack = stackedWidgetP
        self._controller = controller
        self._manager = manager

        loadUi(REGISTER_UI_PATH, self)

        self.registerBtn.clicked.connect(self.registerBtnPressed)
        self.cancelBtn.clicked.connect(self.cancelBtnPressed)

    def registerBtnPressed(self):
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

        result = self._controller.register_user(user_info)
        if result:
            QtWidgets.QMessageBox.information(self, "Success", "User Registered Successfully")
            self._widgetStack.setCurrentIndex(0)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to Register User")

    def cancelBtnPressed(self):
        self._widgetStack.setCurrentIndex(0)
