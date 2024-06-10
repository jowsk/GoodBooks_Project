import pandas as pd
import numpy as np 
import re

import spacy
from collections import Counter
import re
from tqdm import tqdm


def preprocess_df(data, column_name='tag_name'):
    data[column_name] = data[column_name].str.lower()
    data[column_name] = data[column_name].str.replace('-', ' ')
    data = years_to_decades(data, column_name)
    data = remove_stopwords(data, column_name)
    data = special_cases(data, column_name)

    return data



def years_to_decades(data, column_name='tag_name'):
    for ten in range(1900, 2020, 10):
        for year in range(0, 10):
            i = ten + year
            data[column_name] = data[column_name].str.replace(f'{i}', f"{ten}s")
            data[column_name] = data[column_name].str.replace(f'{ten}ss', f"{ten}s")
    print(len(data))
    return data

def remove_stopwords(data, column_name='tag_name'):
    nlp = spacy.load('en_core_web_sm')
    for tag in tqdm(data[column_name]):
        doc = nlp(tag)
        words = [token.text for token in doc if not token.is_stop]
        data.loc[data[column_name] == tag, column_name] = ' '.join(words)
    return data

def special_cases(data, column_name='tag_name'):
    for tag in tqdm(data[column_name]):
        if 'e book' in tag:
            data.loc[data[column_name] == tag, column_name] = tag + 'ebook'
        if 'sf' in tag:
            data.loc[data[column_name] == tag, column_name] = tag + 'scifi'
        if 'sci fi' in tag:
            data.loc[data[column_name] == tag, column_name] = tag + 'scifi'
    return data