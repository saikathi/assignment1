# coding=utf-8
import sys
import json
import re
import codecs



def main():
    sent_file = open(sys.argv[1])
    tweets_file = open(sys.argv[2])

    #Sent files parsing
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.values()

    #tweets file
    tweets_conv = []
    score_conv =[]
    tweets = []
    score = 0
    happyState = {}
    for line in tweets_file:
        try:
            text = ""
            score = 0
            tweets = json.loads(line.strip())
            tweets_conv.append(tweets)
        except:
            continue


        try:
            if 'place' in tweets.keys():
               country = tweets['place']['country_code']
               if country == "US":
                   place = tweets['place']['full_name'].split(", ")[1]
                   if len(place) == 2:
                       #print place
                       if 'text' in tweets.keys():
                           text = tweets['text']
                           words = re.split('\s+', text.lower())
                           for word in words:
                               word = re.sub('[^0-9a-zA-Z]+', '', word)
                               if word in scores:
                                   score += scores[word]
                               else:
                                   score += 0
                           #print score
                       if place not in happyState.keys():
                            happyState[place] = score
                       else:
                            happyState[place] = (happyState[place]+score)/2
                            #print happyState[place]



        except (KeyError, TypeError, IndexError):
            continue
    #print happyState
    #print sorted(happyState, key=happyState.get, reverse=True)
    print sorted(happyState, key=happyState.get, reverse=True)[0]
    #sorted(dict.keys())[-1]

   # print len(tweets_conv)
   # print len(score_conv)


if __name__ == '__main__':
    main()
