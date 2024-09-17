from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import sys
from RealEstateAgency.Agency.View.LoginView import LoginView
from RealEstateAgency.Agency.Application.config import ICON, STYLE
from RealEstateAgency.Agency.Controller.UserController import UserController
from RealEstateAgency.Agency.Model.RealEstateAgencyManager import RealEstateAgencyManager

def main():
    user_service = RealEstateAgencyManager()
    user_controller = UserController(user_service)
    app = QtWidgets.QApplication(sys.argv)
    widget_stack = QtWidgets.QStackedWidget()
    login_view = LoginView(widget_stack, user_controller, user_service)
    widget_stack.addWidget(login_view)
    widget_stack.setFixedWidth(1200)
    widget_stack.setFixedHeight(700)
    app.setWindowIcon(QIcon(ICON.as_posix()))
    widget_stack.setWindowTitle("Agencija Mornar")
    with open(STYLE.as_posix(), 'r') as style_file:
        app.setStyleSheet(style_file.read())
    widget_stack.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()