from bottle import Bottle
from app.service.match_service import MatchService
from app.api.return_api_messages import ReturnMessages
from app.utils.riot_terms_mapper import RiotTermsMapper

match_api = Bottle()
match_service = MatchService()


@match_api.get('/<account_id>')
def get_summoner_info_by_name(account_id):
    result = match_service.get_matches_by_account_id(account_id)
    return RiotTermsMapper().get_champion_name(
        result.json()) if result.status_code == 200 else ReturnMessages.error_get_response()
