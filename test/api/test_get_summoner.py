import unittest
import webtest as webtest
from unittest.mock import patch

from app.main import App
from app.settings.configs import riot_development_api_key


class GetSummonerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.api_client = webtest.TestApp(App)
        self.url = '/summoner/'
        self.summoner_name = 'Bengi'
        self.mock_response = {"id": "5Hsdfasdfasdf5a", "accountId": "LkasidjnjhbJBAI", "puuid": "FA5asdas_Cmausdhyaf23",
                              "name": "Bengi", "profileIconId": 897, "revisionDate": 1615221624000,
                              "summonerLevel": 100}

    @patch("app.service.summoner_service.SummonerService.get_summoner_by_name")
    def test_get_memo_with_status_code_200(self, mocker):
        mocker.return_value = self.mock_response
        response: webtest.TestResponse = self.api_client.get(self.url + self.summoner_name,
                                                             headers={"X-Riot-Token": riot_development_api_key})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get('name'), self.summoner_name)

    @patch("app.service.summoner_service.SummonerService.get_summoner_by_name")
    def test_get_memo_with_status_code_404(self, mocker):
        mocker.return_value = None
        response: webtest.TestResponse = self.api_client.get(self.url + self.summoner_name,
                                                             headers={"X-Riot-Token": riot_development_api_key},
                                                             expect_errors=True)
        self.assertEqual(response.status_code, 404)
