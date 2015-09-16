#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, ctypes
argfile = str(sys.argv[1])

def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxA(0, text, title, style)

#enter the corresponding info from your Twitter application
CONSUMER_KEY = '1mrDAlzvTxbJIgzXlYv2mObaE'
CONSUMER_SECRET = 'nqiNdnGdMyAFZYBDpPRGMMSxf6BIrDC8c08cPsTRzciWWjQnAx'
ACCESS_KEY = '1119375529-v632xD4cM5x2o6tNZe1yGqjnNP91PJYB2EKXz86'
ACCESS_SECRET = '02lASoJmg61nOyTdTRfMUCrZINEemAVwleSVu4HZZ2MJY'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

public_tweets=api.home_timeline()
for tweet in public_tweets:
    print tweet.text

# user = api.get_user('thelugal')
#
# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#     print friend.screen_name

for line in f:
    api.update_status(status=line)
    time.sleep(600) #Tweets every 10 minutes

Mbox('TweetBot', 'The program is done',0)
