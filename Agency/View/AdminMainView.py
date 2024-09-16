from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from RealEstateAgency.Agency.View.MessageBox import messageBox
from RealEstateAgency.Agency.Application.config import ADMIN_UI_PATH
from RealEstateAgency.Agency.Model.Enums import UserType

class AdminMainView(QtWidgets.QMainWindow):
    def __init__(self, widget_stack, user, controller):
        super(AdminMainView, self).__init__()
        self._widgetStack = widget_stack
        self._controller = controller
        self._user = user

        loadUi(ADMIN_UI_PATH, self)
        self.setWindowTitle("Admin Dashboard")

        self.add_owner_button.clicked.connect(self.add_owner)
        self.deactivate_account_button.clicked.connect(self.deactivate_account)
        self.hide_property_button.clicked.connect(self.hide_property)
        self.view_reports_button.clicked.connect(self.view_reports)

    def add_owner(self):
        owner_info = {
            'name': 'New Owner',
            'email': 'new_owner@example.com',
            'password': 'owner123',
            'phone_number': '123-456-7890',
            'user_type': UserType.OWNER
        }
        result = self._controller.register_user(owner_info)
        if result:
            messageBox("Success", "Owner Added Successfully")
        else:
            messageBox("Error", "Failed to Add Owner")

    def deactivate_account(self):
        user_id = 1  # Placeholder for selected user id
        result = self._controller.remove_user(user_id)
        if result:
            messageBox("Success", "User Deactivated Successfully")
        else:
            messageBox("Error", "Failed to Deactivate User")

    def hide_property(self):
        property_id = 1  # Placeholder for selected property id
        result = self._controller.hide_property(property_id)
        if result:
            messageBox("Success", "Property Hidden Successfully")
        else:
            messageBox("Error", "Failed to Hide Property")

    def view_reports(self):
        reports = self._controller.get_monthly_reports()
        messageBox("Reports", f"Monthly Reports: {reports}")
