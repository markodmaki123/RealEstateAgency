from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
from RealEstateAgency.Agency.View.MessageBox import messageBox
from RealEstateAgency.Agency.Application.config import USER_UI_PATH
from RealEstateAgency.Agency.Model.Enums import SearchData, Rate

class UserMainView(QtWidgets.QMainWindow):
    def __init__(self, widget_stack, user, controller):
        super(UserMainView, self).__init__()
        self._widgetStack = widget_stack
        self._user = user
        self._controller = controller
        self._data = None
        self._properties = []
        self._agents = []

        loadUi(USER_UI_PATH, self)

        self.search_button.clicked.connect(self.search_properties)
        self.schedule_visit_button.clicked.connect(self.schedule_visit)
        self.like_button.clicked.connect(lambda: self.rate_property(Rate.LIKE))
        self.dislike_button.clicked.connect(lambda: self.rate_property(Rate.DISLIKE))
        self.rate_agent_button.clicked.connect(self.rate_agent)
        self.load_data()

    def load_data(self):
        self._data = self._controller.get_all_real_estates()
        self.property_list_widget.clear()
        if self._data:
            for prop in self._data:
                self.property_list_widget.addItem(prop[1])

    def search_properties(self):
        search_params = {
            SearchData.LOCATION: self.location_input.text(),
            SearchData.PRICE: (self.min_price_input.value(), self.max_price_input.value()),
            SearchData.AREA: (self.min_area_input.value(), self.max_area_input.value()),
            SearchData.TYPE: self.property_type_input.currentText(),
            SearchData.SALE: self.sale_checkbox.isChecked(),
            SearchData.RENT: self.rent_checkbox.isChecked()
        }
        properties = self._controller.search_real_estate(search_params)
        self.property_list_widget.clear()
        self._properties = properties
        if properties:
            for prop in properties:
                self.property_list_widget.addItem(prop.name)
            messageBox(f"Found {len(properties)} properties", "Search Results")
        else:
            messageBox("No properties found", "Search Results")

    def schedule_visit(self):
        selected_property = self.get_selected_property()
        if selected_property:
            date = self.visit_date_input.date()
            time = self.visit_time_input.time()
            visit_scheduled = self._controller.schedule_visit(self._user.pk, selected_property.pk, date, time)
            if visit_scheduled:
                messageBox(f"Visit scheduled for {date.toString()} at {time.toString()}", "Visit Scheduled")
            else:
                messageBox("Failed to schedule visit", "Error")

    def rate_property(self, rate):
        selected_property = self.get_selected_property()
        if selected_property:
            self._controller.rate_property(self._user.pk, selected_property.pk, rate)
            messageBox(f"Property {rate.name}d", "Rating")

    def rate_agent(self):
        selected_agent = self.get_selected_agent()
        if selected_agent:
            rating = self.agent_rating_input.value()
            feedback = self.agent_feedback_input.toPlainText()
            self._controller.rate_agent(self._user.pk, selected_agent.pk, rating, feedback)
            messageBox("Agent rated successfully", "Rating")

    def get_selected_property(self):
        selected_items = self.property_list_widget.selectedItems()
        if selected_items:
            selected_property_name = selected_items[0].text()
            for prop in self._properties:
                if prop.name == selected_property_name:
                    return prop
        messageBox("Please select a property", "Error")
        return None

    def get_selected_agent(self):
        selected_items = self.agent_list_widget.selectedItems()
        if selected_items:
            selected_agent_name = selected_items[0].text()
            for agent in self._agents:
                if agent.name == selected_agent_name:
                    return agent
        messageBox("Please select an agent", "Error")
        return None
