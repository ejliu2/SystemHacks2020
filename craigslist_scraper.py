from craigslist import CraigslistForSale
import sys
import json

import scipy.stats as stats

def generate_craig_search(searchinput1):
    word = searchinput1.split()

    vancouver = CraigslistForSale(site='vancouver', filters={'query': word })

    craigslist_price = []

    i = 0

    for result in vancouver.get_results(geotagged=True):
       
        search_output = result

        search_output['price'] = search_output["price"].replace("$", "")
        
        craigslist_price.append(float(search_output['price']))

        print(search_output)

        i = i + 1

        if i == 30:
            break

    return craigslist_price


# def execute_search(searchinput2): 
#     vancouver = CraigslistForSale(site='vancouver', filters={'query': searchinput2 })

#     return searchinput2

def price_store(searchinput2):
    # craigslist_price = []

    # for result in vancouver.get_results(geotagged=True):
    #     search_output = result

    #     search_output['price'] = search_output.replace("$", "")
        
    #     craigslist_price.append = craigslist_price

    return craigslist_price

def main():
    search_string = 'macbook pro 2016'
    
    craigslist_price = generate_craig_search(search_string)

    print(craigslist_price)

    craiglist_stats = stats.describe(craigslist_price)

    print(craiglist_stats)





if __name__ == '__main__':
    main()
    


    
        
    


