class Address:
    def __init__(self, info_dict):
        self._pk = info_dict.get("pk")
        self._place = info_dict.get("place")
        self._street = info_dict.get("street")
        self._number = info_dict.get("number")

    @property
    def pk(self):
        return self._pk

    @property
    def place(self):
        return self._place

    @property
    def street(self):
        return self._street

    @property
    def number(self):
        return self._number

    def to_dict(self):
        return {
            "pk": self._pk,
            "place": self._place,
            "street": self._street,
            "number": self._number
        }

    def address_to_str(self):
        return self._street + ' ' + self._number + ' ' +  ' ' + self._place
