from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from RealEstateAgency.Agency.View.MessageBox import messageBox
from RealEstateAgency.Agency.Application.config import AGENT_UI_PATH

class AgentMainView(QtWidgets.QMainWindow):
    def __init__(self, widget_stack, user, controller):
        super(AgentMainView, self).__init__()
        self._widgetStack = widget_stack
        self._controller = controller
        self._user = user

        loadUi(AGENT_UI_PATH, self)
        self.setWindowTitle("Agent Dashboard")

        self.view_properties_button.clicked.connect(self.view_properties)
        self.view_calendar_button.clicked.connect(self.view_calendar)
        self.manage_visits_button.clicked.connect(self.manage_visits)

    def view_properties(self):
        properties = self._controller.search_real_estate({'agent_id': self._user.id})
        if properties:
            messageBox(f"Found {len(properties)} properties", "Properties")
        else:
            messageBox("No properties found", "Error")

    def view_calendar(self):
        calendar = self._controller.view_calendar(self._user.id)
        if calendar:
            messageBox(f"Found {len(calendar)} visit requests", "Calendar")
        else:
            messageBox("No visits found", "Error")

    def manage_visits(self):
        visit_requests = self._controller.view_calendar(self._user.id)
        if visit_requests:
            messageBox(f"Found {len(visit_requests)} visit requests", "Visits")
        else:
            messageBox("No visits found", "Error")
