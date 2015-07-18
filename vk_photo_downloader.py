# -*- coding: UTF-8 -*-
# !/usr/bin/env python
# Simple VK Photo Downloader
# Before  usage change 'DOWNLOAD_PATH' to your value

import requests
import json

DOWNLOAD_PATH = 'C:\photos\\'

print ('Hello,what you want to do?')
print ('1-Download,2-About')

choice = int(raw_input('Please,enter your choice: '))

if choice == 1:

    id = str(raw_input('Please, enter your VK ID: '))

    url = 'https://api.vk.com/method/photos.get?owner_id=' + id + '&album_id=wall&v=5'
    request = requests.get(url)  # Send the request to the server
    json = request.json()  # got a response from the server in JSON format
    photos_count = json['response']['count']  # Number of photos
    print ('You have {0} photos'.format(photos_count))
    count = int(raw_input('Please enter the number of photos to download: '))

    for i in range(0, count):  # In this cycle we check
        n = json['response']['items'][i]  # Do photos available
        if n.has_key('photo_1280') == True:  # With these resolutions
            s = n['photo_1280']  # If nothing is found, write error.
            filename = s[len(s) - 15:]
            addr = s[0:len(s) - 15]
            down_url = n['photo_1280']
            p = requests.get(down_url)
            out = open(DOWNLOAD_PATH + filename, "wb")
            out.write(p.content)
            out.close()
        elif n.has_key('photo_807') == True:
            s = n['photo_807']
            filename = s[len(s) - 15:]
            addr = s[0:len(s) - 15]
            down_url = n['photo_807']
            p = requests.get(down_url)
            out = open(DOWNLOAD_PATH + filename, "wb")
            out.write(p.content)
            out.close()
        elif n.has_key('photo_604') == True:
            s = n['photo_604']
            filename = s[len(s) - 15:]
            addr = s[0:len(s) - 15]
            down_url = n['photo_604']
            p = requests.get(down_url)
            out = open(DOWNLOAD_PATH + filename, "wb")
            out.write(p.content)
            out.close()
        elif n.has_key('photo_130') == True:
            s = n['photo_1280']
            filename = s[len(s) - 15:]
            addr = s[0:len(s) - 15]
            down_url = n['photo_1280']
            p = requests.get(down_url)
            out = open(DOWNLOAD_PATH + filename, "wb")
            out.write(p.content)
            out.close()
        elif n.has_key('photo_75') == True:
            s = n['photo_1280']
            filename = s[len(s) - 15:]
            addr = s[0:len(s) - 15]
            down_url = n['photo_1280']
            p = requests.get(down_url)
            out = open(DOWNLOAD_PATH + filename, "wb")
            out.write(p.content)
            out.close()
        else:
            print ('Error')

        print ('Downloading..')

elif choice == 2:
    print ('VKPhoto Downloader by Ilya Ivanov\n')
    print ('(c) 2015 ')
