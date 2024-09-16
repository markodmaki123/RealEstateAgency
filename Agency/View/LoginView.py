from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

from RealEstateAgency.Agency.Model.Enums import UserType
from RealEstateAgency.Agency.View.AgentMainView import AgentMainView
from RealEstateAgency.Agency.View.OwnerMainView import OwnerMainView
from RealEstateAgency.Agency.View.AdminMainView import AdminMainView
from RealEstateAgency.Agency.View.RegisterView import RegisterView
from RealEstateAgency.Agency.View.MessageBox import messageBox
from RealEstateAgency.Agency.Application.config import LOGIN_UI_PATH

class LoginView(QtWidgets.QMainWindow):
    def __init__(self, widget_stack, controller, manager):
        super(LoginView, self).__init__()
        self._widgetStack = widget_stack
        self._controller = controller
        self._manager = manager
        self._user = None

        loadUi(LOGIN_UI_PATH, self)
        self.setWindowTitle("Login")

        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_button.clicked.connect(self.login_btn_pressed)
        self.register_button.clicked.connect(self.switch_to_register)

    def login_btn_pressed(self):
        email = self.email_field.text()
        password = self.password_field.text()

        self._user = self._controller.login_user(email, password)

        if self._user:
            messageBox("Uspela prijava!", "Uspesno")
            if self._user.user_type == UserType.AGENT:
                agent_view = AgentMainView(self._widgetStack, self._user, self._controller)
                self._widgetStack.addWidget(agent_view)
                self._widgetStack.setCurrentWidget(agent_view)
            elif self._user.user_type == UserType.OWNER:
                owner_view = OwnerMainView(self._widgetStack, self._user, self._controller)
                self._widgetStack.addWidget(owner_view)
                self._widgetStack.setCurrentWidget(owner_view)
            elif self._user.user_type == UserType.ADMIN:
                admin_view = AdminMainView(self._widgetStack, self._user, self._controller)
                self._widgetStack.addWidget(admin_view)
                self._widgetStack.setCurrentWidget(admin_view)
        else:
            messageBox("Pogresni kredencijali.", "Error")

    def switch_to_register(self):
        register_view = RegisterView(self._widgetStack, self._controller, self._manager)
        self._widgetStack.addWidget(register_view)
        self._widgetStack.setCurrentWidget(register_view)
