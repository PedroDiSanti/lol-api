import requests
from app.settings.configs import create_route, riot_development_api_key
from app.utils.riot_terms_mapper import RiotTermsMapper


class MatchService:
    def __init__(self):
        self.riot_url = create_route('match')

    def get_matches_by_account_id(self, account_id):
        api_response = requests.get(self.riot_url + account_id, headers={"X-Riot-Token": riot_development_api_key})
        api_response_translated = RiotTermsMapper().get_champion_name(api_response.json())
        if api_response:
            return api_response_translated
        else:
            raise FileNotFoundError()
