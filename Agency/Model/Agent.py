from RealEstateAgency.Agency.Model.User import User



class Agent(User):
    def __init__(self, info_dict):
        super().__init__(info_dict)
        self._properties = info_dict.get("properties", [])

    @property
    def properties(self):
        return self._properties