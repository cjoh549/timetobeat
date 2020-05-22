import requests, bs4, sys

def search_hltb(search_term):

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
    res = requests.post('https://howlongtobeat.com/search_results?page=1', data)
    res.raise_for_status()
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

def get_time_to_beat(path):

    res = requests.get('https://howlongtobeat.com/' + path)
    res.raise_for_status()
    page = bs4.BeautifulSoup(res.text, "html.parser")

    elms = page.find_all('li', 'short')

    if len(elms) == 0:
        return False

    times = []
    for key in elms:
        full_time = key.contents[3].text
        split_time = full_time.split(" ")
        time = split_time[0].replace("½", ".5")
        times.append(time)

    return times    

if len(sys.argv) != 2:
    print("Missing game title.")

search_term = sys.argv[1]
path = search_hltb(search_term)

if path != False:
    times = get_time_to_beat(path)

    print(times)
else:
    print("Game title not found")