from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
from RealEstateAgency.Agency.View.MessageBox import messageBox
from RealEstateAgency.Agency.Application import config


class VisitsView(QtWidgets.QMainWindow):
    def __init__(self, widget_stack, controller, manager, user):
        super(VisitsView, self).__init__()
        self._widgetStack = widget_stack
        self._controller = controller
        self._manager = manager
        self._user = user