# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 00:38:27 2021

@author: patel
"""


from typing import Optional
from pydantic import BaseModel

# local imports
#import scraper.scraper as scr
import src.scraper.scraper_mt as scr

# response type define
class jsonScraps(BaseModel):
    timestamp: str
    title: str
    price: str
    website: str
    link: Optional[str] = None
    
def search_items_API(
    site: str,
    item_name: str,
    relevant: Optional[str] = None,
    order_by_col: Optional[str] = None,
    reverse: Optional[bool] = False,
    listLengthInd: Optional[int] = 10,
    export: Optional[bool] = False
):
    '''Wrapper API to fetch AMAZON, WALMART and TARGET query results

    Parameters
    ----------
    item_name: string of item to be searched

    Returns
    ----------
    itemListJson: JSON List
        list of search results as JSON List
    '''
    # logging in file
    file = open("logger.txt", "a")
    file.write('amazon query:' + str(item_name)+'\n')

    # building argument
    args = {
        'search': item_name,
        'sort': 'pr' if order_by_col == 'price' else 'pr',  # placeholder TDB
        'des': reverse,  # placeholder TBD
        'num': listLengthInd,
        'relevant': relevant
    }

    scrapers = []

    if site == 'az' or site == 'all':
        scrapers.append('amazon')
    if site == 'wm' or site == 'all':
        scrapers.append('walmart')
    if site == 'tg' or site == 'all':
        scrapers.append('target')
    if site == 'cc' or site == 'all':
        scrapers.append('costco')
    if site == 'bb' or site == 'all':
        scrapers.append('bestbuy')
    if site == 'eb' or site == 'all':
        scrapers.append('ebay')

    # calling scraper.scrape to fetch results
    itemList = scr.scrape(args=args, scrapers=scrapers)
    if not export and len(itemList) > 0:
        file.close()
        return itemList
#    elif len(itemList) > 0:
#        # returning CSV
#        with open('slash.csv', 'w', encoding='utf8', newline='') as f:
#            dict_writer = csv.DictWriter(f, itemList[0].keys())
#            dict_writer.writeheader()
#            dict_writer.writerows(itemList)
#        return FileResponse('slash.csv', media_type='application/octet-stream', filename='slash_'+item_name+'.csv')
    else:
        # No results
        return None