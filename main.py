from simplejustwatchapi.justwatch import search
import pandas

df = pandas.read_csv("watchlist.csv")

titles = df["Name"]

watchlist = titles.to_list()



#watchlist = ["Avatar", "Contra", "Kraven-the-Hunter", "Basic-Instinct"]

services = ["Netflix", "Disney Plus", "Youtube", "ARD Mediathek", "Amazon Video"]

result = {}
count = 0
for movie in watchlist:
	   
    count = count + 1
    search_results = search(movie, "DE", "de", 3, True) 
    movie_item = search_results[0]	

    if count > 10:
        break

    for offer in movie_item.offers:
	   
        if not hasattr(offer, 'package') or not hasattr(offer.package, 'name'):
            continue
	   
        streamer = offer.package.name

        if offer.monetization_type == 'FLATRATE' and streamer in services:
			
            movie_found = True

            if streamer not in result:
				
                result[streamer] = []
            result[streamer].append(f"{movie})")

print(result)	
