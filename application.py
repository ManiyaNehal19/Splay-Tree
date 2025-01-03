from finalfunctions import *

def find_key(dictionary, value):
    #function made to find key for the given value in the dictionary
    for key, val in dictionary.items():
        if val == value:
            return key
def main(google_searches, dict, notGoogle):
    # all the different variation to write search, delete and recent
    search_variations = [
        "search", "SEARCH", "Search",
        "sEaRcH", "SeArch", "SEARC",
        
        "SearCH", "seARCh", "SEACh",
        "sEaRcH", "sEaRCh", "sEARCH",
        "seARcH", "seARCh", "seARCH",
        "SEaRCH", "SeARch", "SEArcH",
        "SEAch", "sEarCh", "SeARCH"
    ]
    delete_variations = [
        "delete", "DELETE", "Delete",
        "dELeTE", "DeLetE", "DEL",
        "deleTE", "DeLETE", "deLET",
        "dElete", "delETE", "DeletE",
        "DElete", "deLetE", "DELeTe",
        "DeleTe", "dELETE", "DELete",
        "DELETe", "DelETE", "DElETE",
        "DeleTE", "DeLete", "DELete"
    ]
    recent_variations = [
        "recent", "RECENT", "Recent",
        "rEcENt", "ReCent", "REC",
        "recenT", "ReCENT", "recENT",
        "rEcent", "recENT", "ReceNt",
        "REcent", "reCenT", "RECENt",
        "reCent", "RECENt", "REcenT",
        "RecENt", "RECent", "ReCEnt",
        "rECeNT", "RecEnt", "RECenT"
    ]
    #main input to find what the user want to do
    print("Welcome to NotGoogle. You can 'search', 'delete' or see your 'recent' searches by writing either of the keywords below.")
    print("How can I help you?")
    need = input()
    # if the user wants to search
    if need in search_variations:
        print("Search NotGoogle")
        # taking search command
        searchwhat = input()
        # if its already present in the search list we dont do anythinf except splay it 
        if searchwhat in google_searches:
            y = find_key(dict, searchwhat)
            n = Node(y)
            notGoogle.splay(n)
            google_search_url = "https:\\www.google.com/search=q?"+searchwhat
            print("Google Search Results:")
            print("-------------------------------")
            print("Showing results for:" + searchwhat)
            print("Visit the following URL for search results"+ google_search_url)
            print("-------------------------------")

        else:
            # if its not we insert it in the tree as well as we insert it in the dictionary
            length = len(dict)
            x = Node(length+1)
            notGoogle.insert(x)
            google_search_url = "https:\\www.google.com/search=q?"+searchwhat
            print("Google Search Results:")
            print("-------------------------------")
            print("Showing results for:" + searchwhat)
            print("Visit the following URL for search results"+ google_search_url)
            print("-------------------------------")
            dict[length+1] = searchwhat
            google_searches.append(searchwhat)
    
    elif need in delete_variations:
        print("Delete NotGoogle")
        deletewhat = input()
        # Search for the node to delete using the search function
        key = find_key(dict, deletewhat)
        if key!=None:
            # If the node to be deleted is found, remove it from the tree
            notGoogle.delete(Node(key))
            # Remove the search term from the list of Google searches
            google_searches.remove(deletewhat)
            # Remove the search term from the dictionary
            del dict[key]
        else:
            print("The search was not made")
    elif need in recent_variations:
        # we find the most recent ones here 
        print("Your most recent searches")
        x = traversal_from_root(notGoogle)
        j = 1
        for i in x: 
            if j<=5:
                print(dict[i])
                j+=1
            else:
                break
    main(google_searches, dict, notGoogle)
google_searches = [
        "Weather",
        "News",
        "COVID-19",
        "Time",
        "Translate",
        "Calculator",
        "Maps",
        "YouTube",
        "Facebook",
        "Gmail",
        "Amazon",
        "Netflix",
        "Instagram",
        "WhatsApp",
        "Twitter",
        "Bank of America",
        "Wells Fargo",
        "Chase",
        "Capital One",
        "Craigslist",
        "eBay",
        "Target",
        "Walmart",
        "Best Buy",
        "Home Depot",
        "Lowes",
        "IKEA",
        "Zillow",
        "Apartments for rent",
        "Hotels",
        "Restaurants",
        "Gas stations",
        "Flights",
        "Car rental",
        "Uber",
        "Lyft",
        "Bus schedules",
        "Train schedules",
        "Bitcoin",
        "Stocks",
        "Weather forecast",
        "Recipes",
        "How to tie a tie",
        "How to lose weight",
        "How to cook rice",
        "How to play guitar",
        "How to draw"
    ]
dict ={}
j=1
for i in google_searches:
    dict[j] = i
    j+=1

notGoogle =  SplayTree()
for i in dict:
    x = Node(i)
    notGoogle.insert(x)
main(google_searches, dict, notGoogle)


        
            