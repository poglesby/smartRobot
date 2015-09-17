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
filename.close()

# public_tweets=api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

# user = api.get_user('thelugal')
#
# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#     print friend.screen_name

# for line in data:
#     # api.update_status(status=line)
#     # time.sleep(60) #Tweets every 10 minutes
#     if len(data) > 140:
#         print "Input exceeds 140 characters."
#         data = data[:140]
#         print data

for x in range(0, len(data)):
    if len(data) > 140:
        api.update_status(status= data[:140])
        time.sleep(60)
        data = data[140:]
