from RealEstateAgency.Agency.Model.Enums import RealEstateStatus
from RealEstateAgency.Agency.Model.Enums import RealEstateType


class RealEstate:
    def __init__(self, info_dict):
        self._pk = info_dict["pk"]
        self._location = info_dict["location"]
        self._price = info_dict["price"]
        self._type = RealEstateType(info_dict["type"])
        self._status = RealEstateStatus(info_dict["status"])
        self._agent = info_dict["agent"]


    @property
    def pk(self):
        return self._pk

    @property
    def location(self):
        return self._location

    @property
    def price(self):
        return self._price

    @property
    def type(self):
        return self._type

    @property
    def status(self):
        return self._status

    @property
    def agent(self):
        return self._agent