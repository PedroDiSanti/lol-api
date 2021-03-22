import os
from dotenv import load_dotenv

load_dotenv()

riot_development_api_key = os.getenv('DEVELOP_API_KEY')
riot_domain = os.getenv('RIOT_DOMAIN')
route_domain_dict = {
    "summoner": os.getenv('SUMMONER_URL'),
    "match": os.getenv('MATCH_URL')
}


def create_route(route_name):
    return riot_domain + route_domain_dict.get(route_name)
