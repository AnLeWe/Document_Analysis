#!/usr/bin/env python

"""
Utility classes for the document analysis lecture at the University of Konstanz.
"""
__author__      = "Yannick Metz"
__copyright__   = "Copyright 2022, DBVIS"

from wordcloud import WordCloud
import matplotlib.pyplot as plt


FILEPATH_LOREM_IPSUM = 'data/lorem_ipsum.txt'


def read_lorem_ipsum_text():
    """Read in lorem ipsum text"""
    with open(FILEPATH_LOREM_IPSUM, 'r') as f:
        content = f.read()
        return content


def create_word_cloud(word_frequencies, title):
    print(title + ':')
    wordcloud = WordCloud(width=800, height=400, max_words=None, min_font_size=0.01, max_font_size=100,  
                      background_color='white', random_state=42, 
                      #relative_scaling=1.0,
                      prefer_horizontal=1.0,
                      stopwords = [],
                      color_func=lambda *args, **kwargs: (30,30,30)).generate_from_frequencies(word_frequencies)
    plt.figure(figsize=(16,6))
    plt.axis("off")
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.show()