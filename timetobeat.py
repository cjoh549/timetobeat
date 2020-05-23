import requests, bs4, difflib
from collections import OrderedDict
from operator import itemgetter

def search_hltb(search_term, fuzz=.95):
    """
    Searches howlongtobeat.com for a game and returns it's path if found or False on failure.
    Defaults to a sorta fuzzy search, pass in a lower number to increase the fuzz
    """

    uri = "https://howlongtobeat.com/search_results?page=1"
    data={'queryString':search_term,
            't':'games',
            'sorthead':'popular',
            'sortd':'Normal Order',
            'plat':'',
            'length_type':'main',
            'length_min':'',
            'length_max':'',
            'detail':''
    }

    res = requests.post(uri, data)
    make_request(uri, data)

    search_results = bs4.BeautifulSoup(res.text, "html.parser")
    elms = search_results.find('a', 'text_green')
    
    if elms != None:
        if elms.text == search_term:
            return elms.get('href')

    else:
        elms = search_results.find_all('a', 'text_white')

        #return if we have an exact match
        if len(elms) == 0:
	        return False
        
        titles = {}
        for key in elms:
            # figure out how close of a title match we are getting and drop it in a dictionary
            titles[key.get('href')] = difflib.SequenceMatcher(None, key.text, search_term).ratio()

            #return if we have an exact match
            if key.text == search_term:
                return key.get('href')

        # sort the dictionary of titles and grab the first one
        otitles = OrderedDict(sorted(titles.items(), key=itemgetter(1), reverse = True))
        first_key = list(otitles.keys())[0] 
        
        # if the first title is close, return it
        if otitles[first_key] >= fuzz:
            return first_key

    # nothing was close enough, so return False
    return False


def make_request(uri, data=""):
    """A wrapper for the requests library with error checking, returns the response object"""

    try:
        res = requests.post(uri, data)
        res.raise_for_status()
        return res
    except requests.exceptions.RequestException as err:
        print ("Connection Error:",err)    


def get_time_to_beat(path):
    """
    Gets the actual time to beat information from the website. Returns a dictionary
    that contains the single player times for the Main Story, Main + Extras, Completionsist
    and All Styles of play or the multiplayer times for Solo, Co-Op and Versus. Depending
    on the game, it may not return all options. Returns False on failure.
    """
    uri = 'https://howlongtobeat.com/' + path

    res = requests.post(uri)
    page = bs4.BeautifulSoup(res.text, "html.parser")

    elms = page.find_all('li', 'short')

    if len(elms) == 0:
        return False

    times = {}
    for key in elms:
        full_time = key.contents[3].text
        split_time = full_time.split(" ")
        time = split_time[0].replace("½", ".5")
        times[key.contents[1].text] = time

    return times