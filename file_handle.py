#!/usr/bin/env python3
"""Read and Print file content"""
from os.path import isfile
import sys


def fetch_words(path):
    """Get words from file
    Args:
        Get words from the file mmentioned in parameter
    
    Returns:
        List of strings containing words from the file
    """
    file_words = []
    f=open(path,'r')
    file_lines = f.readlines()
    for line in file_lines:
        for word in line.split():
            file_words.append(word)
    f.close()
    return file_words


def print_words(words):
    """Print words list
    Args:
        List of words to be printed"""
    for word in words:
        print(word)


def main():
    """Read and Print Content of File"""
    path = input('Enter path ')
    
    if path == None or not isfile(path):
        print("File is not valid")
        return
    
    words = fetch_words(path)
    print_words(words)


if __name__ == "__main__":
    main()