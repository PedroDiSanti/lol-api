from bottle import Bottle
from app.api.return_api_messages import ReturnMessages
from app.service.summoner_service import SummonerService


summoner_api = Bottle()
summoner_service = SummonerService()


@summoner_api.get('/<summoner_name>')
def get_summoner_info_by_name(summoner_name):
    result = summoner_service.get_summoner_by_name(summoner_name)
    return result if result.status_code == 200 else ReturnMessages.error_get_response()
