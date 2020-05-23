import pytest
from timetobeat import *

def test_good_game_title():
    game_title = "Mass Effect"
    result = search_hltb(game_title)
    assert result == "game?id=5698"

def test_bad_game_title():
    game_title = "ASDKJasdfasd asdfaena;sdf $"
    result = search_hltb(game_title)
    assert result == False