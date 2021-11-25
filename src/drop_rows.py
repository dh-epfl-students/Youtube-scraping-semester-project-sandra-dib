import pandas as pd
import random
import youtube_dl
import numpy

df = pd.read_csv('../data/video_info.csv', delimiter=',')
for youtube_id in df['id']:
    count = 0
    
    video_url = 'https://www.youtube.com/watch?v=%s' % youtube_id  #The Youtube URL
    ydl_opts = {}
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    info_dict = ydl.extract_info(video_url, download=False)
    formats = info_dict.get('formats',None)
    
    for f in formats:
        if f.get('height') == None or f.get('height') < 1080:
            count=count+1
        elif f.get('height') >= 1080: 
            break
         
    if count == len(formats):
        print('test3')
        df = df[df['id'] != youtube_id]    