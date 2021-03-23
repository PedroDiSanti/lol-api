import requests
from app.settings.configs import create_route, riot_development_api_key


class MatchService:
    def __init__(self):
        self.riot_url = create_route('match')

    def get_matches_by_account_id(self, account_id):
        try:
            api_response = requests.get(self.riot_url + account_id, headers={"X-Riot-Token": riot_development_api_key})
            return api_response
        except FileNotFoundError as api_response_error:
            raise api_response_error
