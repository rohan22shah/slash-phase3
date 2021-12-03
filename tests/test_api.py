# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 00:03:30 2021

@author: Rohan Shah
"""
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from src.main_streamlit import search_items_API
    
def test_api_amazon():
    product = 'dell'
    site = 'az'
    result = search_items_API(site, product)
    assert result is not None
    
def test_api_bestbuy():
    product = 'laptop'
    site = 'bb'
    result = search_items_API(site, product)
    assert result is not None
    
def test_api_costco():
    product = 'ketchup'
    site = 'cc'
    result = search_items_API(site, product)
    assert result is not None
    
def test_api_ebay():
    product = 'lenovo'
    site = 'eb'
    result = search_items_API(site, product)
    assert result is not None
    
def test_api_target():
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    assert result is not None

def test_api_walmart():
    product = 'bulb'
    site = 'wm'
    result = search_items_API(site, product)
    assert result is not None

def test_api_all():
    product = 'bulb'
    site = 'all'
    result = search_items_API(site, product)
    assert result is not None