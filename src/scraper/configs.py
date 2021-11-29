# package imports
from datetime import datetime
import requests
from ebaysdk.finding import Connection

# local imports
from scraper.formattr import formatTitle

# configs
WALMART = {
    'site': 'walmart',
    'url': 'https://www.walmart.com/search?q=',
    'item_component': 'div',
    'item_indicator': {
        'data-item-id': True
    },
    'title_indicator': 'span.lh-title',
    'price_indicator': 'div.lh-copy',
    'link_indicator': 'a'
}

AMAZON = {
    'site': 'amazon',
    'url': 'https://www.amazon.com/s?k=',
    'item_component': 'div',
    'item_indicator': {
        'data-component-type': 's-search-result'
    },
    'title_indicator': 'h2 a span',
    'price_indicator': 'span.a-price span',
    'link_indicator': 'h2 a.a-link-normal'
}

COSTCO = {
    'site': 'costco',
    'url': 'https://www.costco.com/CatalogSearch?dept=All&keyword=',
    'item_component': 'div',
    'item_indicator': {
        'class': 'product-tile-set'
    },
    'title_indicator': 'span a',
    'price_indicator': 'div.price',
    'link_indicator': 'span.description a',
}

BESTBUY = {
    'site': 'bestbuy',
    'url': 'https://www.bestbuy.com/site/searchpage.jsp?st=',
    'item_component': 'li',
    'item_indicator': {
        'class': 'sku-item'
    },
    'title_indicator': 'h4.sku-header a',
    'price_indicator': 'div.priceView-customer-price span',
    'link_indicator': 'a.image-link',
}


# individual scrapers
def scrape_target(query):
    """Scrape Target's api for data

    Parameters
    ----------
    query: str
        Item to look for in the api

    Returns
    ----------
    items: list
        List of items from the dict
    """

    api_url = 'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1'

    page = '/s/' + query
    params = {
        'key': 'ff457966e64d5e877fdbad070f276d18ecec4a01',
        'channel': 'WEB',
        'count': '24',
        'default_purchasability_filter': 'false',
        'include_sponsored': 'true',
        'keyword': query,
        'offset': '0',
        'page': page,
        'platform': 'desktop',
        'pricing_store_id': '3991',
        'useragent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'visitor_id': 'AAA',
    }

    data = requests.get(api_url, params=params).json()

    items = []
    for p in data['data']['search']['products']:
        item = {
            'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'title': formatTitle(p['item']['product_description']['title']),
            'price': '$' + str(p['price']['current_retail']),
            'website': 'target'
        }
        items.append(item)

    return items


def scrape_ebay(query):
    """Scrape Target's api for data

    Parameters
    ----------
    query: str
        Item to look for in the api

    Returns
    ----------
    items: list
        List of items from the dict
    """

    EBAY_APP = 'BradleyE-slash-PRD-2ddd2999f-2ae39cfa'

    try:
        api = Connection(appid=EBAY_APP, config_file=None, siteid='EBAY-US')
        response = api.execute('findItemsByKeywords', {'keywords': query})
    except ConnectionError as e:
        print(e)
        return []

    data = response.dict()

    items = []
    for p in data['searchResult']['item']:
        item = {
            'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'title': formatTitle(p['title']),
            'price': '$' + p['sellingStatus']['currentPrice']['value'],
            'website': 'ebay',
            'link': p['viewItemURL']
        }
        items.append(item)

    return items


CONFIGS = [WALMART, AMAZON, COSTCO, BESTBUY]
