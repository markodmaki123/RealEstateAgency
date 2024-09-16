from PyQt5.QtWidgets import QApplication
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from RealEstateAgency.Agency.View.LoginView import LoginView
from RealEstateAgency.Agency.View.RegisterView import RegisterView
from RealEstateAgency.Agency.Controller.UserController import UserController
from RealEstateAgency.Agency.Model.RealEstateAgencyManager import RealEstateAgencyManager

def main():
    app = QtWidgets.QApplication(sys.argv)

    user_service = RealEstateAgencyManager()
    user_controller = UserController(user_service)
    widgetStack = QtWidgets.QStackedWidget()
    user_view = LoginView(widgetStack, user_controller , user_service)
    widgetStack.addWidget(user_view)
    widgetStack.setFixedWidth(1044)
    widgetStack.setFixedHeight(551)
    widgetStack.window().setWindowTitle("Agencija Mornar")
    widgetStack.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()