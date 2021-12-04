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

def test_api_target():
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    assert result is not None
