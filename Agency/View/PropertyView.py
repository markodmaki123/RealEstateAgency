from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
from RealEstateAgency.Agency.View.MessageBox import messageBox
from RealEstateAgency.Agency.Application import config


class PropertyView(QtWidgets.QMainWindow):
    def __init__(self, widget_stack, controller, manager, user):
        super(PropertyView, self).__init__()
        self._widgetStack = widget_stack
        self._controller = controller
        self._manager = manager
        self._user = user

        loadUi(config.PROPERTY_UI_PATH, self)
        self.setWindowTitle("Property")

        self.add_property.clicked.connect(self.add_property)
        self.select_image.clicked.connect(self.select_image_file)

    @property
    def widget(self):
        return self._widgetStack

    def select_image_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)",
                                                   options=options)
        if file_name:
            self.imagesTxt.setText(file_name)

    def add_property(self):
        real_estate_info = {
            'pk': None,
            'location': self.locationTxt.text(),
            'price': self.priceTxt.text(),
            'status': self.statusTxt.text(),
            'type': self.typeTxt.text(),
            'agent': self._user,
            'images': self.imagesTxt.text(),
        }

        result = self._controller.add_real_estate(self._user, real_estate_info)
        if result:
            messageBox("Registration success", "Success")
            self._widgetStack.setCurrentIndex(1)
        else:
            messageBox("Registration failed", "Error")