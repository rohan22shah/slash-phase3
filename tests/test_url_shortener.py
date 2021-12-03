from src.url_shortener import shorten_url

def test_url_shortener():
    url = 'https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038'
    s_url = shorten_url(url)
    assert 'tinyurl.com' in s_url