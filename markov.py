#!/usr/bin/env python

import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #using corpus instead of "file_string" b/c corpus is the generic argument used for this block of code.  It is replaced w/ whatever is passed in the main function.''

    chain_dict = {}

    sentence_list = massage_corpus(corpus)
    for sentence in sentence_list:
        sentence = sentence.strip()
        list_of_words = sentence.split(" ")
        last_tuple = len(list_of_words) - 2 
        for x in range(0, len(list_of_words) - 2):
           key_tuple = (list_of_words[x], list_of_words[x + 1])
           value_list = [list_of_words[x + 2]]
           chain_dict[key_tuple] = chain_dict.get(key_tuple, []) + value_list
        key_tuple = (list_of_words[last_tuple],list_of_words[last_tuple + 1])
        value_list = ["."]
        chain_dict[key_tuple] = chain_dict.get(key_tuple, []) + value_list
    print chain_dict

    return chain_dict
    
def massage_corpus(corpus):
    """Takes corpus, returns list of sentences"""

    corpus = corpus.replace("\n", " ").replace("!", ".").replace("?", ".").replace('\'', "").replace("(", "").replace(")", "")
    return  corpus.split(".")

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    args = sys.argv

    file_object = open('sample.txt')
    file_string = file_object.read()

    input_text = "sample.txt"

    chain_dict = make_chains(file_string)
    random_text = make_text(chain_dict)
    print random_text


if __name__ == "__main__":
    main()