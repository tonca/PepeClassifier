import json
import requests
import os  
import urllib2

def request_json():

    print "Requesting data from api.imgur.com ..."

    r = requests.get('https://api.imgur.com/3/album/U2dTR#n8McQ1A/images', headers={'Authorization': '8a98dfaa9554238'})

    data = json.loads(r.content)

    return data

def download_image(imgurl, imgpath):

    img = urllib2.urlopen(imgurl)
    localFile = open(imgpath, 'wb')
    localFile.write(img.read())
    localFile.close()


response_path = "data/response_pepes.json"

if __name__ == '__main__':

    if os.path.isfile(response_path):
        with open(response_path) as data_file:    
            data = json.load(data_file)

        if data['success'] == True : 
            print 'ok!!!'
        
        else : 
            data = request_json()
            with open(response_path, 'w') as outfile:
                json.dump(data,outfile, indent=4, sort_keys=True)

    else :
        data = request_json()
        with open(response_path, 'w') as outfile:
            json.dump(data,outfile, indent=4, sort_keys=True)



    images = data['data']['images']
    image_links = [ item['link'] for item in images ]


    image_folder = 'data/images'

    for link in image_links:
        image_file = link.split('/')[-1]
        download_image(link, "%s/%s" % (image_folder,image_file))
        print "%s -> %s" % (link,image_file)
    #print json.dumps(data, indent=4, sort_keys=True)