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
        entity = {}
        entities = {}
       # texts = ""
      #  print tweets.keys()
        if 'entities' in tweets.keys():
            entities = tweets['entities']
            if 'hashtags' in entities.keys():
                tweet_hastags = entities['hashtags']
                for tags in tweet_hastags:
                    text = tags['text']
                    #print text
                    if text not in freq:
                        freq[text] = 1
                    else:
                        freq[text] += 1
    #print freq
    freq =  sorted(freq.items(), key=lambda x: x[1], reverse=True)[0:10]
    #print freq
    for k, v in freq:
	  	print "%s %s" % (k, v)

    # for k, v in freq.items():
	 # 	print "%s %s" % (k, float(v) /Total)

if __name__ == '__main__':
    main()
