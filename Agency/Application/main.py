from PyQt5 import QtWidgets
import sys
from RealEstateAgency.Agency.View.LoginView import LoginView
from RealEstateAgency.Agency.Controller.UserController import UserController
from RealEstateAgency.Agency.Model.RealEstateAgencyManager import RealEstateAgencyManager

def main():
    app = QtWidgets.QApplication(sys.argv)

    user_service = RealEstateAgencyManager()
    user_controller = UserController(user_service)
    widget_stack = QtWidgets.QStackedWidget()
    login_view = LoginView(widget_stack, user_controller, user_service)
    widget_stack.addWidget(login_view)
    widget_stack.setFixedWidth(1044)
    widget_stack.setFixedHeight(551)
    widget_stack.setWindowTitle("Agencija Mornar")
    widget_stack.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()