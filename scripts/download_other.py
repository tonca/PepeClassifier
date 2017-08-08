import json
import requests
import os  
import urllib2
import download_images as dm


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
                data = dm.request_json('https://api.imgur.com/3/gallery/album/%s/images' % gallery)
                with open(response_path, 'w') as outfile:
                    json.dump(data,outfile, indent=4, sort_keys=True)

        else :
            data = dm.request_json('https://api.imgur.com/3/gallery/album/%s/images' % gallery)
            with open(response_path, 'w') as outfile:
                json.dump(data,outfile, indent=4, sort_keys=True)

        images = data['data']
        image_links = [ item['link'] for item in images ]


        image_folder = 'data/other'

        for link in image_links:
            image_file = "%s_%s" % (gallery,link.split('/')[-1])
            dm.download_image(link, "%s/%s" % (image_folder,image_file))

        #print json.dumps(data, indent=4, sort_keys=True)