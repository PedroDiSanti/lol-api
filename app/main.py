from bottle import Bottle

from app.api.summoner import summoner_api
from app.api.match import match_api

App = Bottle()

App.mount('/summoner', summoner_api)
App.mount('/match', match_api)


if __name__ == '__main__':
    App.run(host='0.0.0.0', port=8080, debug=True, reloader=True)
