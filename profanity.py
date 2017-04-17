import urllib

def read_text():
    quotes = open("J:\Python\ud036-L2-use functions\movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check(contents)

def check(text):
    connect = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output=connect.read()
    print(output)
    connect.close()
read_text()
