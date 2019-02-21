import json
import requests
import os  
import urllib2
import download_images as dm

# LINK ISN'T WORKING ANYMORE
# found the same data at url https://archive.org/details/PepeImgurAlbum

response_path = "data/response_pepes.json"

if __name__ == '__main__':

    if os.path.isfile(response_path):
        with open(response_path) as data_file:    
            data = json.load(data_file)

        if data['success'] == True : 
            print('ok!!!')
        
        else : 
            data = dm.request_json('https://api.imgur.com/3/album/U2dTR#n8McQ1A/images')
            with open(response_path, 'w') as outfile:
                json.dump(data,outfile, indent=4, sort_keys=True)

    else :
        data = dm.request_json('https://api.imgur.com/3/album/U2dTR#n8McQ1A/images')
        with open(response_path, 'w') as outfile:
            json.dump(data,outfile, indent=4, sort_keys=True)


    print(data)

    images = data['data']['images']
    image_links = [ item['link'] for item in images ]


    image_folder = 'data/pepes'

    for link in image_links:
        image_file = link.split('/')[-1]
        dm.download_image(link, "%s/%s" % (image_folder,image_file))
    #print(json.dumps(data, indent=4, sort_keys=True))