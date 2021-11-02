import pandas as pd
import random
import youtube_dl
import numpy
import cv2
from tqdm import tqdm

df = pd.read_csv('../data/video_info_2.csv', delimiter=',')
dict_sample = {}
places_sel = random.sample(df.place.unique().tolist(), 10)
for place in places_sel:
    ids = df.loc[df['place'] == place].id.tolist()
    ids_sample = random.sample(ids, 10)
    dict_sample.update({place : ids_sample})
    
    
for key, value in tqdm(dict_sample.items()):
    
    place = key
    for youtube_id in value:
        print(youtube_id)
        video_url = 'https://www.youtube.com/watch?v=%s' % youtube_id  #The Youtube URL
        ydl_opts = {'format': 'best'}
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        info_dict = ydl.extract_info(video_url, download=False)

        formats = info_dict.get('formats',None)

        f = formats[-1]
        url = f.get('url',None)
        cap = cv2.VideoCapture(url)

        x = 1
        count = info_dict['duration'] / 4

        while x < 4 :

            for i in range(3):

                time = x * info_dict['duration'] + ( 10 * i ) # each time, take 3 shots at 10 sec intervals
                ret, frame = cap.read()
                if not ret:
                    break
                filename = "../data/screenshots/%s-%d.png" % (youtube_id, time)

                cv2.imwrite(filename, frame)
                count += int(info_dict['duration'] / 4)
                cap.set(1,count)

            x += 1

        cap.release()