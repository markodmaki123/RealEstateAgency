from RealEstateAgency.Agency.Model.User import User


class Administrator(User):
    def __init__(self, info_dict):
        super().__init__(info_dict)

