#from RealEstateAgency.Agency.Application.config import DATE_FORMAT
from datetime import datetime
from RealEstateAgency.Agency.Model.Enums import VisitStatus


class Visit:
    def __init__(self, info_dict):
        DATE_FORMAT = "%d.%m.%Y."
        self._pk = info_dict["pk"]
        self._user = info_dict["user"]
        self._real_estate = info_dict["real_estate"]
        self._visit_time = datetime.strptime(info_dict["visit_time"],DATE_FORMAT)
        self._type = VisitStatus(info_dict["status"])


    @property
    def pk(self):
        return self._pk

    @property
    def user(self):
        return self._user

    @property
    def real_estate(self):
        return self._real_estate

    @property
    def visit_time(self):
        return self._visit_time

    @property
    def status(self):
        return self._status
