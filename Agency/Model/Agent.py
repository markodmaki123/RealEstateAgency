from RealEstateAgency.Agency.Model.User import User
from RealEstateAgency.Agency.Model.RealEstate import RealEstate

class Agent(User):
    def __init__(self, info_dict):
        super().__init__(info_dict)
        self._properties = info_dict.get("properties", [])
        self._calendar = info_dict.get("calendar", [])

    @property
    def properties(self):
        return self._properties

    @property
    def calendar(self):
        return self._calendar

    def get_calendar(self):
        return self._calendar

    def add_visit_to_calendar(self, visit):
        self._calendar.append(visit)

    def add_property(self, images, location, price, property_type, status=0, agent=None):
        agent = self
        new_property = RealEstate({
            "images": images,
            "location": location,
            "price": price,
            "type": property_type,
            "agent": agent,
            "status": status
        })
        self._properties.append(new_property)
