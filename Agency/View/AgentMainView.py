from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from RealEstateAgency.Agency.View.MessageBox import messageBox
from RealEstateAgency.Agency.Application import config
from RealEstateAgency.Agency.View.PropertyView import PropertyView
from RealEstateAgency.Agency.View.VisitsView import VisitsView

class AgentMainView(QtWidgets.QMainWindow):
    def __init__(self, widget_stack, user, controller):
        super(AgentMainView, self).__init__()
        self._widgetStack = widget_stack
        self._controller = controller
        self._user = user

        loadUi(config.AGENT_UI_PATH, self)
        self.setWindowTitle("Agent")

        self.view_properties_button.clicked.connect(self.view_properties)
        self.add_properties_button.clicked.connect(self.add_property)
        self.view_calendar_button.clicked.connect(self.view_calendar)
        self.manage_visits_button.clicked.connect(self.manage_visits)

    @property
    def widget(self):
        return self._widgetStack

    def add_property(self):
        property_view = PropertyView(self._widgetStack, self._controller, self._manager, self._user)
        self._widgetStack.addWidget(property_view)
        self._widgetStack.setCurrentIndex(2)

    def view_properties(self):
        properties = self._controller.view_real_estate(self._user.pk)
        if properties:
            messageBox(f"Found {len(properties)} properties", "Properties")
        else:
            messageBox("No properties found", "Error")

    def view_calendar(self):
        try:
            calendar = self._controller.view_calendar(self._user.pk)
            if calendar and isinstance(calendar, list):
                messageBox(f"Found {len(calendar)} visit requests", "Calendar")
            else:
                messageBox("No visits found", "Error")
        except Exception as e:
            messageBox(f"Error occurred: {str(e)}", "Error")

    def manage_visits(self):
        visits_view = VisitsView(self._widgetStack, self._controller, self._manager, self._user)
        self._widgetStack.addWidget(visits_view)
        self._widgetStack.setCurrentIndex(2)
