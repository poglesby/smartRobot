#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
argfile = str(sys.argv[1])

#enter the corresponding info from your Twitter application
CONSUMER_KEY = '1mrDAlzvTxbJIgzXlYv2mObaE'
CONSUMER_SECRET = 'nqiNdnGdMyAFZYBDpPRGMMSxf6BIrDC8c08cPsTRzciWWjQnAx'
ACCESS_KEY = '1119375529-v632xD4cM5x2o6tNZe1yGqjnNP91PJYB2EKXz86'
ACCESS_SECRET = '02lASoJmg61nOyTdTRfMUCrZINEemAVwleSVu4HZZ2MJY'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900) #Tweets every 15 minutes
