from timetobeat import *

search_term = "Animal Crossing: New Horizons"  
path = search_hltb(search_term)

if path != False:
    times = get_time_to_beat(path)

    if times != False:
        print(times)
    else:
        print("Unable to parse times from game title.")
else:
    print("Game title not found")