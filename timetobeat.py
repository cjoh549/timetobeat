import requests, bs4

def search_hltb(search_term):
    """Searches howlongtobeat.com for a game and returns it's path if found or False on failure."""

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

        if len(elms) == 0:
	        return False
        
        for key in elms:
            if key.text == search_term:
                return key.get('href')

    return False


def make_request(uri, data=""):
    """A wrapper for the requests library with error checking, returns the response object"""

    try:
        res = requests.post(uri, data)
        res.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Connection Error:",err)

    return res


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