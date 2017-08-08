import json
import requests
import os  
import urllib2

def request_json(gallery_url):

    print "Requesting data from api.imgur.com..."

    r = requests.get(gallery_url, headers={'Authorization': 'Client-ID 8a98dfaa9554238'})

    data = json.loads(r.content)

    return data

def download_image(imgurl, imgpath):

    if os.path.isfile(imgpath):
        print "%s already exists." % imgpath
    else:
        print "%s -> %s" % (imgurl,imgpath)

        img = urllib2.urlopen(imgurl)
        localFile = open(imgpath, 'wb')
        localFile.write(img.read())
        localFile.close()


imgur_gallery_list = [
    'PGPsQ',
    'f1o0x',
    'GhngQ',
    'vSlrJ',
    'HVSwx',
    '0IO6n',
    'Ffexn',
    '5OS0j',
    'cAGsY',
    'mAoXy',
    'wNTws',
    'WoBWM'
]

if __name__ == '__main__':

    for gallery in imgur_gallery_list :

        response_path = "data/response_other_%s.json" % gallery

        if os.path.isfile(response_path):
            with open(response_path) as data_file:    
                data = json.load(data_file)

            if data['success'] == True : 
                print 'ok!!!'
            
            else : 
                data = request_json('https://api.imgur.com/3/gallery/album/%s/images' % gallery)
                with open(response_path, 'w') as outfile:
                    json.dump(data,outfile, indent=4, sort_keys=True)

        else :
            data = request_json('https://api.imgur.com/3/gallery/album/%s/images' % gallery)
            with open(response_path, 'w') as outfile:
                json.dump(data,outfile, indent=4, sort_keys=True)

        images = data['data']
        image_links = [ item['link'] for item in images ]


        image_folder = 'data/other'

        for link in image_links:
            image_file = "%s_%s" % (gallery,link.split('/')[-1])
            download_image(link, "%s/%s" % (image_folder,image_file))

        #print json.dumps(data, indent=4, sort_keys=True)