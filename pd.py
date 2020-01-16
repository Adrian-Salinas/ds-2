#! /usr/bin/python3
from wordcloud import WordCloud,STOPWORDS
import sys
import requests
from bs4 import BeautifulSoup

# Create a list of word
print ("You are currently running %s" % (sys.argv[0]))
if len(sys.argv) < 2:
    print("You should supply the name of an html file to extract the text from!")
    sys.exit()
else:
    text = open(sys.argv[1], "r")

print("Reading in %s " % str(sys.argv[1]))

soup=BeautifulSoup(text, 'html.parser')

tweets = [p.text for p in soup.findAll('p')]
txt = ' '.join(tweets)
stop_words = ["https", "co", "RT"] + list(STOPWORDS)

# Create the wordcloud object
wordcloud = WordCloud(stopwords=stop_words, width=480, height=480, margin=0).generate(txt)

# Display the generated image:
pngname = "CT_tweets.png"
print("Creating file " + pngname)
wordcloud.to_file(pngname )
