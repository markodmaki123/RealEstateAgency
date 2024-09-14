import json
from datetime import datetime
from RealEstateAgency.Agency.Application.config import USERS_PATH, PROPERTIES_PATH, VISITS_PATH, AGENCIES_PATH, DATE_FORMAT
from RealEstateAgency.Agency.Model.User import User
from RealEstateAgency.Agency.Model.Agent import Agent
from RealEstateAgency.Agency.Model.AgencyOwner import AgencyOwner
from RealEstateAgency.Agency.Model.RealEstate import RealEstate
from RealEstateAgency.Agency.Model.Visit import Visit
from RealEstateAgency.Agency.Model.Administrator import Administrator
from RealEstateAgency.Agency.Model.Enums import UserType, VisitStatus, RealEstateStatus


class RealEstateAgencyManager:
    def __init__(self):
        self._users_by_email = {}
        self._users = {}
        self._real_estates = {}
        self._visits = {}
        self._agencies = {}
        self._load_database()
        self._load_associations()

    def _create_user(self, user_dict):
        user_type = UserType(user_dict["user_type"])
        if user_type == UserType.AGENT:
            user = Agent(user_dict)
        elif user_type == UserType.OWNER:
            user = AgencyOwner(user_dict)
        elif user_type == UserType.ADMIN:
            user = Administrator(user_dict)
        else:
            user = User(user_dict)

        pk = user_dict["pk"]
        self._users[pk] = user
        email = user_dict["email"]
        self._users_by_email[email] = user

    def _load_users(self):
        with open(USERS_PATH, "r") as users_file:
            users_data = json.load(users_file)
            for user_dict in users_data.values():
                self._create_user(user_dict)

    @staticmethod
    def _load_data(file_path, class_name):
        loaded_data_dict = {}
        with open(file_path, "r") as data_file:
            data = json.load(data_file)
            for data_dict in data.values():
                pk = data_dict["pk"]
                loaded_data_dict[pk] = class_name(data_dict)
        return loaded_data_dict

    def _load_database(self):
        self._load_users()
        self._real_estates = self._load_data(PROPERTIES_PATH, RealEstate)
        self._visits = self._load_data(VISITS_PATH, Visit)
        self._agencies = self._load_data(AGENCIES_PATH, AgencyOwner)

    def _load_user_associations(self):
        for user in self._users.values():
            if isinstance(user, Agent):
                for property_pk in user.properties:
                    user.properties[property_pk] = self._real_estates.get(property_pk)

    def _load_visit_associations(self):
        for visit in self._visits.values():
            visit.user = self._users.get(visit.user.pk)
            visit.real_estate = self._real_estates.get(visit.real_estate.pk)

    def _load_associations(self):
        self._load_user_associations()
        self._load_visit_associations()

    def _users_to_json(self):
        json_users = {}
        for pk, user in self._users.items():
            json_users[str(pk)] = user.to_user_dict()
        return json_users

    def _save_users(self):
        with open(USERS_PATH, "w") as users_file:
            json.dump(self._users_to_json(), users_file, indent=4)

    def _real_estates_to_json(self):
        json_real_estates = {}
        for pk, real_estate in self._real_estates.items():
            json_real_estates[str(pk)] = real_estate.to_dict()
        return json_real_estates

    def _save_real_estates(self):
        with open(PROPERTIES_PATH, "w") as properties_file:
            json.dump(self._real_estates_to_json(), properties_file, indent=4)

    def _visits_to_json(self):
        json_visits = {}
        for pk, visit in self._visits.items():
            json_visits[str(pk)] = visit.to_dict()
        return json_visits

    def _save_visits(self):
        with open(VISITS_PATH, "w") as visits_file:
            json.dump(self._visits_to_json(), visits_file, indent=4)
