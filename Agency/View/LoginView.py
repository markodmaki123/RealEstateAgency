from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

from RealEstateAgency.Agency.Model.Enums import UserType
from RealEstateAgency.Agency.View.MessageBox import messageBox
from RealEstateAgency.Agency.View.AgentMainView import AgentMainView
from RealEstateAgency.Agency.View.OwnerMainView import OwnerMainView
from RealEstateAgency.Agency.View.AdminMainView import AdminMainView
from RealEstateAgency.Agency.View.UserMainView import UserMainView
from RealEstateAgency.Agency.View.RegisterView import RegisterView
from RealEstateAgency.Agency.Application import config


class LoginView(QtWidgets.QMainWindow):
    def __init__(self, widget_stack, controller, manager):
        super(LoginView, self).__init__()
        self._widgetStack = widget_stack
        self._controller = controller
        self._manager = manager
        self._user = None

        loadUi(config.LOGIN_UI_PATH, self)
        self.setWindowTitle("Login")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_button.clicked.connect(self.login_btn_pressed)
        self.register_button.clicked.connect(self.switch_to_register)

    @property
    def widget(self):
        return self._widgetStack

    def login_btn_pressed(self):
        try:
            email = self.email_field.text()
            password = self.password_field.text()
            self._user = self._controller.login_user(email, password)

            if self._user:
                messageBox("Login successful!", "Success")
                if self._user.user_type == UserType.AGENT:
                    agent_view = AgentMainView(self._widgetStack, self._user, self._controller)
                    self._widgetStack.addWidget(agent_view)
                    self._widgetStack.setCurrentIndex(1)
                elif self._user.user_type == UserType.OWNER:
                    owner_view = OwnerMainView(self._widgetStack, self._user, self._controller)
                    self._widgetStack.addWidget(owner_view)
                    self._widgetStack.setCurrentIndex(1)
                elif self._user.user_type == UserType.ADMIN:
                    admin_view = AdminMainView(self._widgetStack, self._user, self._controller)
                    self._widgetStack.addWidget(admin_view)
                    self._widgetStack.setCurrentIndex(1)
                elif self._user.user_type == UserType.REGULAR:
                    user_view = UserMainView(self._widgetStack, self._user, self._controller)
                    self._widgetStack.addWidget(user_view)
                    self._widgetStack.setCurrentIndex(1)
            else:
                messageBox("Incorrect credentials.", "Error")
        except Exception as e:
            messageBox(f"An error occurred: {str(e)}", "Error")


    def switch_to_register(self):
        register_view = RegisterView(self._widgetStack, self._controller, self._manager)
        self._widgetStack.addWidget(register_view)
        self._widgetStack.setCurrentIndex(1)
