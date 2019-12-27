# for now, just work on downloading top image of the day from r/hikinh
"""
script to download the top image of the day from r/hiking,
which will then be used in another script to post the image to twitter
"""
import os
import requests
from PIL import Image
from io import BytesIO

def scrape(i):
    """
    main function for the scraping script
    """
    url = 'https://www.reddit.com/r/hiking/top.json'
    response = requests.get(url, headers={'User-agent': 'scraper 0.1'})
    if not response.ok:
        print('error', response.status_code)
        exit()
    # array of posts on the page
    data = response.json()['data']['children']
    # index zero is the top post
    top_post = data[i]['data']
    #don't want to upload a video, so return false if it is a video
    if top_post['is_video']:
        is_video = True
    else:
        is_video = False
    # get the image url of the top post from past 24 hours
    image_url = top_post['url']

    # need to check image url and set approprate file extension
    if '.png' in image_url:            
        extension = '.png'        
    elif '.jpg' in image_url or '.jpeg' in image_url:            
        extension = '.jpeg'
    else:            
        image_url += '.jpeg'           
        extension = '.jpeg'
    # prevents removed images from being downloaded    
    image_response = requests.get(image_url)
    im = Image.open(BytesIO(image_response.content))
    im.show()
    """
    if image.status_code == 200:
        try:
            # now try to write it to the 'images' folder, which is stored locally on my drive
            os.chdir('images')
            output_filehandle = open(top_post['title'] + extension, mode='bx')
            output_filehandle.write(image_response.content)
        except:
            pass
    user = top_post['author']
    title = top_post['title']
    # if the media is a video, adding an image file exension causes things to break, so just return 0 instead
    if not is_video:
        # TODO: can't download image because app is now hosted on heroku, not my own local OS. 
        # This will probably require a database, maybe? or heroku's "ephemeral disk"
        file_size = os.path.getsize(title+extension)
    else:
        file_size = 0
    # need to return the size of the file of the image incase it is greater than 3072KB, 
    # because tweepy doesn't like files larger than 3072KB
    return title, user, extension, file_size, is_video
    """
scrape(0)

