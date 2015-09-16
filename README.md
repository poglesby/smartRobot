This is my README for my twitter bot: smart robot.
TODO:
- make a bot
- make it smart
- get it to start tweeting
- problems with tweepy

Traceback (most recent call last):
  File "helloworld.py", line 21, in <module>
    api.update_status(line)
  File "/usr/local/lib/python2.7/site-packages/tweepy/api.py", line 193, in update_status
    )(post_data=post_data, *args, **kwargs)
  File "/usr/local/lib/python2.7/site-packages/tweepy/binder.py", line 243, in _call
    return method.execute()
  File "/usr/local/lib/python2.7/site-packages/tweepy/binder.py", line 227, in execute
    raise TweepError(error_msg, resp)
tweepy.error.TweepError: [{u'message': u'media_ids parameter is invalid.',
u'code': 44}]
