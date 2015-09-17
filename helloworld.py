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
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open (argfile, "r") as filename:
    data=filename.read().replace('\n', ' ')
    # splitline = data.split(';',139)
filename.close()

def split_by_n(seq, n):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]

tweets = list(split_by_n(data, 140))

for line in tweets:
    api.update_status(status=line)
    time.sleep(600) #This will tweet 140 characters every 10 minutes
