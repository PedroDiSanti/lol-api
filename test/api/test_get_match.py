import unittest
import webtest as webtest
from unittest.mock import patch

from app.main import App
from app.settings.configs import riot_development_api_key


class GetMatchTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.api_client = webtest.TestApp(App)
        self.url = '/match/'
        self.summoner_id = 'LkasidjnjhbJBAI'
        self.mock_response = {
            "matches": [
                {
                    "platformId": "BR1",
                    "gameId": 2207055503,
                    "champion": "Zed",
                    "queue": 830,
                    "season": 13,
                    "timestamp": 1615249569227,
                    "role": "DUO_SUPPORT",
                    "lane": "NONE"
                },
                {
                    "platformId": "BR1",
                    "gameId": 2207092604,
                    "champion": "Mordekaiser",
                    "queue": 830,
                    "season": 13,
                    "timestamp": 1615248551226,
                    "role": "DUO",
                    "lane": "NONE"
                },
                {
                    "platformId": "BR1",
                    "gameId": 2207070563,
                    "champion": "Tristana",
                    "queue": 830,
                    "season": 13,
                    "timestamp": 1615247572524,
                    "role": "DUO_SUPPORT",
                    "lane": "NONE"
                }
            ],
            "startIndex": 0,
            "endIndex": 100,
            "totalGames": 115
        }

    @patch("app.service.match_service.MatchService.get_matches_by_account_id")
    def test_get_memo_with_status_code_200(self, mocker):
        mocker.return_value = self.mock_response
        response: webtest.TestResponse = self.api_client.get(self.url + self.summoner_id,
                                                             headers={"X-Riot-Token": riot_development_api_key})
        self.assertEqual(response.status_code, 200)

    @patch("app.service.match_service.MatchService.get_matches_by_account_id")
    def test_get_memo_with_status_code_404(self, mocker):
        mocker.return_value = None
        response: webtest.TestResponse = self.api_client.get(self.url + self.summoner_id,
                                                             headers={"X-Riot-Token": riot_development_api_key},
                                                             expect_errors=True)
        self.assertEqual(response.status_code, 404)
