from bottle import Bottle
from app.service.summoner_service import SummonerService


summoner_api = Bottle()
summoner_service = SummonerService()


@summoner_api.get('/<summoner_name>')
def get_summoner_info_by_name(summoner_name):
    try:
        result = summoner_service.get_summoner_by_name(summoner_name)
    except FileNotFoundError as error:
        return error

    return result
