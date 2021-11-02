import numpy as np
import youtube_dl
import urllib
import urllib.request
import re
import unidecode
from tqdm import tqdm
import pytube
import pandas as pd


# create an empty dictionnary
video_dict = {}

inputfile = pd.read_csv('../data/unesco_sites_cleaned.csv',delimiter=';', header= None)
for place in tqdm(inputfile[1]):
    
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
  
    for video_id in video_ids:
        try:
            video_url = 'https://www.youtube.com/watch?v=%s' % video_id  #The Youtube URL
            ydl_opts = {}
            ydl = youtube_dl.YoutubeDL(ydl_opts)
            info_dict = ydl.extract_info(video_url, download=False)
            formats = info_dict.get('formats',None)

            x = 1080 # HD -> change to 2160 for 4k

            for f in formats:
                height = f.get('height')
                if height is not None and height >= x and f.get('filesize') is not None:
                # add conditions : "drone" must be in title OR description
                
                    print('passed')
                    filesize = f.get('filesize')
                    x = height
                    video_dict[video_id] =  [place_clean1, info_dict.get('duration'), info_dict.get('title'), info_dict.get('upload_date'), height, filesize ]
                    
        except:
            pass


        
    
video_df = pd.DataFrame.from_dict(video_dict, orient='index', columns=['place', 'duration', 'title', 'date', 'height', 'filesize'])

video_df.to_csv('../data/video_info_2.csv', index_label = 'id')
