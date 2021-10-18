import pandas as pd
import numpy as np
import csv
import youtube_dl
import urllib
import urllib.request
import re
import unidecode
from tqdm import tqdm
import pytube
from pytube import YouTube
from __future__ import unicode_literals

inputfile = csv.reader(open('unesco_sites.csv','r'), delimiter=';')

ydl_opts = {
'format': 'bestaudio/best',
'outtmpl': 'tmp/%(id)s.%(ext)s',
'noplaylist': True,
'quiet': True,
'prefer_ffmpeg': True,
'audioformat': 'wav',
'forceduration':True
}

# create an empty dictionnary
video_dict = {}

# open the csv file 
inputfile = csv.reader(open('unesco_sites.csv','r'), delimiter=';')

# read line by line
for row in inputfile:

    # get second column (names of places)
    place = row[1]
    
    # clean string : remove accents
    place_clean1 = unidecode.unidecode(place)
    # clean string : remove spaces
    place_clean2 = place_clean1.replace(' ', '+')
    
    # add key words 
    search_words = place_clean2 + "+drone"
    
    # make a request in youtube, store the results in a list
    results = []
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_words)
    
    # store the results
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    

   # for each video id, find also the duration and title of the video
    durations = []
    titles = []
    dates = []
    
    for video_id in tqdm(video_ids):
        ydl_opts = {'ignoreerrors': True}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            myVideo = YouTube("https://www.youtube.com/watch?v=%s" % video_id)
            if not myVideo.age_restricted:
                dictMeta = ydl.extract_info("https://www.youtube.com/watch?v=%s" % video_id, download=False)
                durations.append(dictMeta['duration'])
                titles.append(dictMeta['title'])
                dates.append(dictMeta['upload_date'])
        video_dict.update({video_id : [place, dictMeta['duration'], dictMeta['title'], dictMeta['upload_date']]})
    
    
video_df = pd.DataFrame.from_dict(video_dict2, orient='index', columns=['id', 'duration', 'title', 'date'])

video_df.to_csv('video_info2.csv', index_label = 'id')