# espn_functions/api_setup.py
from espn_api.football import League
from config import LEAGUE_ID, YEAR, ESPN_S2, SWID

def initialize_league():
    return League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
