#! /usr/bin/env python
# coding=utf-8

import tweepy
import random
import os
import time

#set keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

def twitter_img_bot():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # set the image path
    path = '/root/Desktop/4chan/pics'

    # random images gathering
  
    n = 0
    file_list = [] 
    for filename in os.listdir(path):
        n = n + 1
        file_list.append(filename)
    
    a = random.randint(0,n)
    wholepath = str(path)+'/'+str(file_list[a])
    random_img = os.path.abspath(wholepath)
    api = tweepy.API(auth)
    media = api.media_upload(random_img)
    api.update_status(status='[random image]', media_ids=[media.media_id])
    
    time_wait()
    
def time_wait():
    print 'successful tweet, now sleeping for 1 hour...'
    while True:
        time.sleep(3600);
        print 'start tweeting'
        twitter_img_bot()
        
if __name__ == '__main__':
    twitter_img_bot()
