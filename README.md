# Time to Beat

Given a video game title, Time to Beat will search the https://howlongtobeat.com/ website and grab the length of time it takes to beat the game entered. If an exact match isn't found, it will search with a small amount of fuzziness, which is adjustable via code.

**Basic Search**

```
search_term = "Mass Effect"  
path = search_hltb(search_term)

if path != False:
    times = get_time_to_beat(path)

    if times != False:
        print(times)
    else:
        print("Unable to parse times from game title.")
else:
    print("Game title not found")
```

Output: {'Main Story': '17', 'Main + Extras': '28.5', 'Completionist': '44', 'All Styles': '27'}

**Fuzzy Search**

```
search_term = "Halo Combat Evolved" # Actual name is Halo: Combat Evolved
path = search_hltb(search_term)

if path != False:
    times = get_time_to_beat(path)

    if times != False:
        print(times)
    else:
        print("Unable to parse times from game title.")
else:
    print("Game title not found")
```

Results: {'Main Story': '10', 'Main + Extras': '11', 'Completionist': '13', 'All Styles': '10.5'}
This is the correct information for Halo: Combat Evolved

**Extra Fuzzy Search**

```
search_term = "Halo"
path = search_hltb(search_term, .80)

if path != False:
    times = get_time_to_beat(path)

    if times != False:
        print(times)
    else:
        print("Unable to parse times from game title.")
else:
    print("Game title not found")
```
Results: {'Main Story': '9', 'Main + Extras': '12', 'Completionist': '18', 'All Styles': '9.5'}
This will return the information for Halo 3, which is the most likely match for that search
