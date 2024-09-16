from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from RealEstateAgency.Agency.View.MessageBox import messageBox
from RealEstateAgency.Agency.Model.Enums import UserType
from RealEstateAgency.Agency.Application.config import OWNER_UI_PATH

class OwnerMainView(QtWidgets.QMainWindow):
    def __init__(self, widget_stack, user, controller):
        super(OwnerMainView, self).__init__()
        self._widgetStack = widget_stack
        self._controller = controller
        self._user = user

        loadUi(OWNER_UI_PATH, self)
        self.setWindowTitle("Owner Dashboard")

        self.add_agent_button.clicked.connect(self.add_agent)
        self.view_properties_button.clicked.connect(self.view_properties)
        self.view_popular_agents_button.clicked.connect(self.view_popular_agents)
        self.view_popular_properties_button.clicked.connect(self.view_popular_properties)

    def add_agent(self):
        agent_info = {
            'name': 'New Agent',
            'email': 'new_agent@example.com',
            'password': 'agent123',
            'phone_number': '123-456-7890',
            'user_type': UserType.AGENT
        }
        result = self._controller.add_agent(self._user.id, agent_info)
        if result:
            messageBox("Agent added successfully!", "Success")
        else:
            messageBox("Error adding agent.", "Error")

    def view_properties(self):
        properties = self._controller.search_real_estate({'owner_id': self._user.id})
        if properties:
            messageBox(f"Found {len(properties)} properties", "Properties")
        else:
            messageBox("No properties found", "Error")

    def view_popular_agents(self):
        agents = self._controller.view_popular_agents()
        messageBox(f"Found {len(agents)} popular agents", "Popular Agents")

    def view_popular_properties(self):
        properties = self._controller.view_popular_real_estates()
        messageBox(f"Found {len(properties)} popular properties", "Popular Properties")
