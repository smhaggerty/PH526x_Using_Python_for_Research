# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 17:06:16 2017

@author: Shane
"""
from collections import Counter
import os

text = "Foo bar lorem ipsum"

def count_words(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary
    where keys are unique words and values are word counts
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
        
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def count_words_fast(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary
    where keys are unique words and values are word counts
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
        
    word_counts = Counter(text.split(" "))
    
    return word_counts

def read_book(title_path):
    """Read a abook and return it as a string"""
    with open(title_path, "r", encoding='utf-8') as current_file:
        text = current_file.read()
        for char in ["\n", "\r"]:
            text = text.replace(char, "")
    return text

def word_stats(word_counts):
    """Return the number of unique words and word frequencies"""
    
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

book_dir = "./Books"

import pandas as pd

stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words_fast(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1