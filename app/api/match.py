from bottle import Bottle
from app.service.match_service import MatchService


match_api = Bottle()
match_service = MatchService()


@match_api.get('/<account_id>')
def get_summoner_info_by_name(account_id):
    try:
        result = match_service.get_matches_by_account_id(account_id)
    except FileNotFoundError as error:
        return error

    return result
