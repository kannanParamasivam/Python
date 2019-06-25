from urllib.request import urlopen

def fetch_words():
    url = 'http://sixty-north.com/c/t.txt'
    story_words = []
    with urlopen(url) as story:
        for line in story:
            for word in line.decode('utf-8').split():
                story_words.append(word)
    return story_words

def print_words(items):
    for item in items:
        print(item)

def main():
    print(__name__)
    words = fetch_words()
    print_words(words)

if __name__ == "__main__":
    main()


        
