import threading
import time
import urllib
import os


def download_image(url, save_name):
    try:
        urlopen = urllib.URLopener()
        fp = urlopen.open(url)
        data = fp.read()
        fp.close()

        print url + ' downloading...'
        fid = open(save_name, 'w+b')
        fid.write(data)
    except IOError:
        print url + 'downloading error...'

fid = open('./faceScrub/facescrub_actors.txt', 'r')
line = fid.readline()
count = 1
while line:
    line = fid.readline()
    tmp = line.split("\t")
    file = tmp[0]
    file = file.replace(' ', '_')
    image_id = tmp[1]
    url = tmp[3]
    fr = tmp[4]
    tmp_url = url.split('.')
    sha256 = tmp[5]
    sha256 = sha256.replace('\n', '')
    file_path = './faceScrub/image/'+file
    if not os.path.exists(file_path):
        os.mkdir(file_path)
        count = 1
    image_path = file_path+'/'+file+image_id+'.'+tmp_url[-1]
    count = int(count) + 1
    download_image(url, image_path)

fid.close()



