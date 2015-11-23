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
    for line in tweets_file:
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
                   if word in scores:
                       score += scores[word]
                   else:
                       score += 0
        print score
        score_conv.append(score)
   # print len(tweets_conv)
   # print len(score_conv)








if __name__ == '__main__':
    main()
