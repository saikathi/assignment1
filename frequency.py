# coding=utf-8
import sys
import json
import re
import codecs



def main():
    tweets_file = open(sys.argv[1])


    #tweets file
    tweets_conv = []
    score_conv =[]
    tweets_text = []
    tweets = []
    score = 0
    tweet_dict = {}
    freq = {}
    for line in tweets_file:
        totalWords = 0
        try:
            text = ""
            score = 0
            tweets = json.loads(line.strip())
            tweets_conv.append(tweets)
        except:
            continue
    #tweets file parsing
        if 'text' in tweets.keys():
               text = tweets['text']
               words = re.split('\s+', text.lower())
               for word in words:
                   word = re.sub('[^0-9a-zA-Z]+', '', word)
                   if word not in freq:
                       freq[word] = 1
                   else:
                       freq[word] += 1
    Total = sum(freq.values())
    for k, v in freq.items():
	 	print "%s %s" % (k, float(v) /Total)

if __name__ == '__main__':
    main()
