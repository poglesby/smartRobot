#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
argfile = str(sys.argv[1])

#enter the corresponding info from your Twitter application
CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
ACCESS_KEY = 'YOUR_ACCESS_KEY'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

text = ''.join(f)
string = text.split(".")
for l in string:
    api.update_status(status=l[:134] + " #elit")
    time.sleep(random.randrange(900))


# for line in f:
#     api.update_status(status=line)
#     time.sleep(900) #Tweets every 15 minutes
