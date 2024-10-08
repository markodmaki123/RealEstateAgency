import json
from pathlib import Path
from RealEstateAgency.Agency.Application.config import USERS_PATH, REAL_ESTATES_PATH, VISITS_PATH, AGENCIES_PATH, DATE_FORMAT
from RealEstateAgency.Agency.Model.User import User
from RealEstateAgency.Agency.Model.Agent import Agent
from RealEstateAgency.Agency.Model.AgencyOwner import AgencyOwner
from RealEstateAgency.Agency.Model.RealEstate import RealEstate
from RealEstateAgency.Agency.Model.Visit import Visit
from RealEstateAgency.Agency.Model.Administrator import Administrator
from RealEstateAgency.Agency.Model.Enums import UserType, VisitStatus, RealEstateStatus, Rate


class RealEstateAgencyManager:
    def __init__(self):
        self._users_by_email = {}
        self._users = {}
        self._real_estates = {}
        self._visits = {}
        self._agencies = {}
        self._load_database()
        self._load_associations()

    def _create_user(self, user_dict, owner_pk=None):
        try:
            user_type = UserType(user_dict["user_type"])
            print(f"Creating user of type: {user_type}")
        except KeyError as e:
            print(f"KeyError: {e} - Check if user_type is present in user_dict")
            raise
        pk = max(self._users.keys(), default=0) + 1
        print(f"New user PK: {pk}")

        try:
            if user_type == UserType.AGENT:
                user = Agent(user_dict)
                user.pk = pk
                if owner_pk:
                    owner = self.get_user_by_pk(owner_pk)
                    owner.agents[user.pk] = user
            elif user_type == UserType.OWNER:
                user = AgencyOwner(user_dict)
                user.pk = pk
            elif user_type == UserType.ADMIN:
                user = Administrator(user_dict)
                user.pk = pk
            else:
                user = User(user_dict)
                user.pk = pk

            self._users[pk] = user
            email = user_dict["email"]
            self._users_by_email[email] = user
            self._save_users()
            print(f"User added to users dictionary: {self._users}")
            return user
        except Exception as e:
            print(f"Error creating user: {e}")
            raise

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
        self._real_estates = self._load_data(REAL_ESTATES_PATH, RealEstate)
        self._visits = self._load_data(VISITS_PATH, Visit)
        self._agencies = self._load_data(AGENCIES_PATH, AgencyOwner)

    def _load_user_associations(self):
        for user in self._users.values():
            if isinstance(user, Agent):
                for property_pk in user.properties:
                    user.properties[property_pk] = self._real_estates.get(property_pk)

    def _load_visit_associations(self):
        for visit in self._visits.values():
            visit._user = self._users.get(visit._user)
            visit._real_estate = self._real_estates.get(visit._real_estate)

    def _load_associations(self):
        self._load_user_associations()
        self._load_visit_associations()

    def add_user(self, new_user_info):
        new_user = self._create_user(new_user_info)
        return new_user

    def authenticate(self, email, password):
        user = self._users_by_email.get(email)
        if user and user.password == password:
            return user
        return None

    def search_properties(self, search_params):
        return [
            real_estate for real_estate in self._real_estates.values()
            if real_estate.matches_search(search_params)
        ]

    def get_user_by_pk(self, user_pk):
        return self._users.get(user_pk)

    def get_real_estate_by_id(self, real_estate_id):
        return self._real_estates.get(real_estate_id)

    def schedule_visit(self, visit):
        pk = max(self._visits.keys(), default=0) + 1
        visit.pk = pk
        self._visits[pk] = visit
        self._save_visits()

    def rate_real_estate(self, user_id, real_estate_id, rating):
        real_estate = self.get_real_estate_by_id(real_estate_id)
        real_estate.add_rating(user_id, rating)
        self._save_real_estates()

    def add_real_estate(self, agent_pk, new_real_estate):
        pk = max(self._real_estates.keys(), default=0) + 1
        new_real_estate.pk = pk
        agent = self.get_user_by_pk(agent_pk)
        agent.properties[pk] = new_real_estate
        self._real_estates[pk] = new_real_estate
        self._save_real_estates()

    def view_real_estates(self, agent_id):
        agent = self.get_user_by_pk(agent_id)
        if agent:
            return agent.properties()
        else:
            return []

    def update_real_estate(self, real_estate_id, updated_info):
        real_estate = self.get_real_estate_by_id(real_estate_id)
        real_estate.update(updated_info)
        self._save_real_estates()

    def get_agent_calendar(self, agent_id):
        agent = self.get_user_by_pk(agent_id)
        if agent:
            return agent.get_calendar()
        else:
            return []

    def update_visit_status(self, visit_id, status):
        visit = self._visits.get(visit_id)
        visit.status = status
        self._save_visits()

    def add_agent(self, owner_id, new_agent_info):
        new_agent = self._create_user(new_agent_info, owner_id)
        return new_agent

    def remove_agent(self, owner_id, agent_id):
        owner = self.get_user_by_pk(owner_id)
        if agent_id in owner.agents:
            del owner.agents[agent_id]
            del self._users[agent_id]
            self._save_users()

    def get_popular_real_estates(self):
        return sorted(self._real_estates.values(), key=lambda re: re.rating, reverse=True)

    def get_popular_agents(self):
        return sorted(
            [user for user in self._users.values() if isinstance(user, Agent)],
            key=lambda agent: agent.get_performance_score(),
            reverse=True
        )

    def get_real_estates(self):
        return self._real_estates

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
        with open(REAL_ESTATES_PATH, "w") as properties_file:
            json.dump(self._real_estates_to_json(), properties_file, indent=4)

    def _visits_to_json(self):
        json_visits = {}
        for pk, visit in self._visits.items():
            json_visits[str(pk)] = visit.to_dict()
        return json_visits

    def _save_visits(self):
        with open(VISITS_PATH, "w") as visits_file:
            json.dump(self._visits_to_json(), visits_file, indent=4)

