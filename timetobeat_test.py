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

def test_default_fuzzy_search():
    game_title = "Halo Combat Evolved" #action title Halo: Combat Evolved
    result = search_hltb(game_title)
    assert result == "game?id=4269"

def test_extra_fuzzy_search():
    game_title = "Halo"
    result = search_hltb(game_title, .80)
    assert result == "game?id=4263"

def test_good_game_url():
    game_url = "game?id=5698"
    result = get_time_to_beat(game_url)
    assert isinstance(result, dict) == True

def test_bad_game_url():
    game_url = "game?id=abc"
    result = get_time_to_beat(game_url)
    assert result == False

def test_multiplayer():
    game_url = "game?id=29358"
    result = get_time_to_beat(game_url)
    assert result['Co-Op'] == "26"

def test_single():
    game_url = "game?id=5698"
    result = get_time_to_beat(game_url)
    assert result['Main Story'] == "17"