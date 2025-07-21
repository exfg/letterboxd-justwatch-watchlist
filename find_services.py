from simplejustwatchapi.justwatch import search
import pandas as pd
from tkinter import filedialog
import pprint

#Streaming services you own
services = ["Netflix", "Disney Plus", "Youtube", "ARD Mediathek", "Amazon Prime Video"]

result = {}

#Fetch your watchlist
#Watchlist can be exported in your letterboxd profile as a cvs file
def get_watchlist ():

    watchlist = filedialog.askopenfilename(title = "Select watchlist",filetypes = (("CSV Files","*.csv"),))
    df = pd.read_csv(watchlist)
    titles = df["Name"]
    watchlist = titles.to_list()

    return(watchlist)

#Find streaming services for your movies
#Only looks for titles that are available via a subscription, paid or rental movies are not taken into account
def find_services (watchlist):

    for movie in watchlist[:100]:
	   
        #Using the api to look up the titles, focusing on german titles and german subsciption services
        search_results = search(movie, "DE", "de", 3, True) 
        movie_entry = search_results[0]	
        
        #Fetch all offers for each movie
        for offer in movie_entry.offers:
	   
            if not hasattr(offer, 'package') or not hasattr(offer.package, 'name'):
                continue
            
            #Get name of the subsciption service
            streamer = offer.package.name

            #Movies that are available via a subscription
            if offer.monetization_type == 'FLATRATE' and streamer in services:
			
                if streamer not in result:
				
                    result[streamer] = []
                
                result[streamer].append(f"{movie})")
    
    return(result)

def main():
	
    titles_by_sevice = find_services(get_watchlist())
    
    pprint.pprint(titles_by_sevice)
    

if __name__ == "__main__":
	main()	
