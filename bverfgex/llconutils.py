'''
llconutils.py
---------------------
Kilian Lüders
Contact: kilian.lueders@hu-berlin.de
02.05.2023

This file contains functions to easily handle the decision texts in xml format as they can be found in the LLCon dataset.
'''



import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs

pattern_space = re.compile(r'\s+')

def clean_string(text):
    '''
    Function to clean up string
    '''
    return text.replace('\n','').replace("&lt;","[").replace("&gt;","]").replace("#160"," ").replace(u'\xa0', u' ')

def get_tbeg(eb_attr):
    '''
    Function to extract the information about the sections of the decision text
    '''
    if 'tbeg' in eb_attr.keys():
        return eb_attr['tbeg']
    else:
        return np.nan
    
def clearn_rn_tags(rn_attr):
    '''
    Function to extract the paragraph (Randnummer) information
    '''
    if rn_attr == dict():
        return np.nan
    else: 
        return rn_attr['rn']

def load_llcon_xml(file_path: str) -> pd.DataFrame:
    '''
    Decision is loaded and parsed.
    '''
    data_entscheidung = list()
    # open xml file
    with open(file_path, "r", encoding='utf-8') as fh:
        raw_text = fh.read()
    entscheidungs_name = file_path.split("/")[-1].replace(".xml", "")
    # clean string
    raw_text = clean_string(raw_text)
    # parse xml tags
    soup = bs(raw_text, "xml")
    # check 'ebenen' tags
    if soup.gruende.ebene1 != None:
        for i, ebe in enumerate(soup.gruende.find_all('ebene1')):
            for j, rn in enumerate(ebe.find_all('absatz')):
                text_raw = re.sub(pattern_space, " ",rn.text).strip() #clean raw text
                data_entscheidung.append({
                    'file': entscheidungs_name,
                    'ebene': ebe.attrs['zeichen'],
                    'ebene_nr': i,
                    'tbeg': get_tbeg(ebe.attrs),
                    'rn': clearn_rn_tags(rn.attrs),
                    'text_raw': text_raw,
                    'ebenen_tag': True})
    else: # no ebenen tags
        for j, rn in enumerate(soup.gruende.find_all('absatz')): 
            text_raw = re.sub(pattern_space, " ",rn.text).strip() #clean raw text
            data_entscheidung.append({
                'file': entscheidungs_name,
                'ebene': "",
                'ebene_nr': np.nan,
                'tbeg': np.nan,
                'rn': clearn_rn_tags(rn.attrs),
                'text_raw': text_raw,
                'ebenen_tag': False})
    return pd.DataFrame(data_entscheidung)
