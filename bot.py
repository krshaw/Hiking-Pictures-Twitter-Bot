"""
importing the module that downloads the top image of the past 24 hours from r/hiking
"""
import os
import scraper
import time
import tweepy

def post():
    """
    function to post the image obtained the the scraper.py module
    """
    i = 0
    title, user, extension, size, is_video = scraper.scrape(i)
    # keep searching for media to upload that is less than 3072KB and is not a video
    # uses OR so that the conditional in the while loop will remain true if the media is not a video,
    # but the size condition is satisfies. the while loop will only stop looking for a media once it is
    # less than 3072KB AND is not a video
    while size > 3072000 or is_video:
        # move on to the second highest post of the day, because the first one is too large for tweepy
        i += 1
        print("file was probably too large, trying to find a small enough image...")
        title, user, extension, size, is_video = scraper.scrape(i)
    consumer_key = ''
    consumer_secret = ''

    access_token = '1175485721307693056-My4D7tpWW4bQKlPIx2ElPvFhtEqYlF'
    access_secret = 'bIKKWTKWtvm1CCjMbSguQHNuDT00NScB86Qj63UFKPdmg'

    # just functions that allow us to sign into twitter account
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    # creates a tweepy api object that has various functions to tweet, interact with followers, etc. 
    api = tweepy.API(auth)
    
    api.update_with_media(title+extension, "{}, by u/{} on r/hiking. #hiking".format(title, user))

    print("post was successful!")
    # delete file after, no need to keep it
    os.remove(title + extension)
# post the image every 25 hours, ensuring it will be a new image every time
INTERVAL = 60 * 60 * 25
while(True):
    print("About to post to twitter...")
    post()
    time.sleep(INTERVAL)
