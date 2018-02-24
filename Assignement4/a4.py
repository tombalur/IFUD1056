#!/usr/bin/python3
# File name: a4.py
# Author: Tom Are Tørum
# Submission: Assignment 4
import os
import collections
import re

def getfilelist(pathname):
    '''Recurse through file structure, return list with sorted txt files
    :param str pathname: folder path
    :return list txtfiles: sorted list with txt files
    '''
    txtfiles = []
    for root, dirs, files in os.walk(pathname):
        for file in files:
            if file.endswith('.txt'):
                txtfiles.append(os.path.join(root, file))
    return sorted(txtfiles)


def getwordfreqs(filename):
    '''Get frequencies of words in file
    :param str filename: Path to txt files.
    :return dict wordcounter: returns counter (dict) sorted descending.
    '''
    wordcounter = collections.Counter()
    #using regex \w+ to get only alphanumeric characters
    words = re.findall(r'\w+', open(filename).read().lower())
    for word in words:
        wordcounter[word] += 1
    return wordcounter


def getcommonwords(dicts):
    '''Get common top ten words in dictionaries
    :param list dicts: A list of dictionaries to compare
    :return list commonwords: Returns common words between top ten words
    '''
    commonwords = []
    commontest = True
    #Taking the ten most common keys in first dict and converting to list
    wordlist = list(dict(dicts[0].most_common(10)).keys())
    for word in wordlist:
        for worddict in dicts:
            #Checking only top ten words
            if word not in dict(worddict.most_common(10)):
                commontest = False
                break
        #Adding word if its found in al dictionaries.
        if commontest:
            commonwords.append(word)
        commontest = True
    return commonwords


filedicts = []
filelist = getfilelist(pathname='/home/tare/PycharmProjects/IFUD1056/Assignement4/books')
for file in filelist:
    filedicts.append(getwordfreqs(filename=file))
commonwords = getcommonwords(dicts=filedicts)
print(commonwords)