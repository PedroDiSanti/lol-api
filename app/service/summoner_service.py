from typing import Optional

import requests

from app.settings.configs import create_route, riot_development_api_key


class SummonerService:
    def __init__(self):
        self.riot_url = create_route('summoner')

    def get_summoner_by_name(self, summoner_name):
        try:
            api_response = requests.get(self.riot_url + summoner_name,
                                        headers={"X-Riot-Token": riot_development_api_key})
            return api_response
        except FileNotFoundError as api_response_error:
            raise api_response_error
