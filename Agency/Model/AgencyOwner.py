from RealEstateAgency.Agency.Model.Agent import Agent


class AgencyOwner(Agent):
    def __init__(self, info_dict):
        super().__init__(info_dict)
        self._agents = info_dict.get("agents", [])

    @property
    def agents(self):
        return self._agents
