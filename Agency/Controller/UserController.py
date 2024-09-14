from RealEstateAgency.Agency.Model.User import User
from RealEstateAgency.Agency.Model.Enums import UserType, Rate, VisitStatus
from RealEstateAgency.Agency.Model.RealEstate import RealEstate
from RealEstateAgency.Agency.Model.Visit import Visit
from RealEstateAgency.Agency.Model.Agent import Agent

class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def register_user(self, info_dict):
        new_user = User(info_dict)
        return self.user_service.add_user(new_user)

    def login_user(self, email, password):
        return self.user_service.authenticate(email, password)

    def search_real_estate(self, search_params):
        return self.user_service.search_properties(search_params)

    def schedule_visit(self, user_id, real_estate_id, visit_time):
        visit_info = {
            'user': self.user_service.get_user_by_id(user_id),
            'real_estate': self.user_service.get_real_estate_by_id(real_estate_id),
            'visit_time': visit_time,
            'status': VisitStatus.PENDING,
        }
        visit = Visit(visit_info)
        return self.user_service.schedule_visit(visit)

    def rate_real_estate(self, user_id, real_estate_id, rating):
        return self.user_service.rate_real_estate(user_id, real_estate_id, Rate(rating))

    def add_real_estate(self, agent_id, real_estate_info):
        new_real_estate = RealEstate(real_estate_info)
        return self.user_service.add_real_estate(agent_id, new_real_estate)

    def edit_real_estate(self, real_estate_id, updated_info):
        return self.user_service.update_real_estate(real_estate_id, updated_info)

    def view_calendar(self, agent_id):
        return self.user_service.get_agent_calendar(agent_id)

    def respond_to_visit_request(self, visit_id, status):
        return self.user_service.update_visit_status(visit_id, status)

    def add_agent(self, owner_id, agent_info):
        new_agent = Agent(agent_info)
        return self.user_service.add_agent(owner_id, new_agent)

    def remove_agent(self, owner_id, agent_id):
        return self.user_service.remove_agent(owner_id, agent_id)

    def view_popular_real_estates(self):
        return self.user_service.get_popular_real_estates()

    def view_popular_agents(self):
        return self.user_service.get_popular_agents()