import json
import requests
import os  
import urllib2

def request_json(gallery_url):

    print("Requesting data from api.imgur.com...")

    r = requests.get(gallery_url, headers={'Authorization': 'Client-ID 8a98dfaa9554238'})

    data = json.loads(r.content)

    return data

def download_image(imgurl, imgpath):

    if os.path.isfile(imgpath):
        print("%s already exists." % imgpath)
    else:
        print("%s -> %s" % (imgurl,imgpath))

        img = urllib2.urlopen(imgurl)
        localFile = open(imgpath, 'wb')
        localFile.write(img.read())
        localFile.close()