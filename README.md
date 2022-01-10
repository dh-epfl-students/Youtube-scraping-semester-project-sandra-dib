# Scrapping YouTube + Key-Frame Selection Project  

projet de semestre-youtube_scraping

## Introduction 

Photogrammetry is a tool to measure our environment in 3D. It uses a set of images of an object seen from various PoV to reconstruct a 3D point cloud (or mesh). YouTube contains billions of hours of records gathered around the globe since many years (+ digitised archives). It 
represents a substantial basis for photogrammetry as many videos contain shots of places from various angles (drone 
flights, vlogs, walking tours…) 

## Objectives and tasks 

This project consists mainly on finding videos with a high potential for videogrammetry (long shots, smooth travellings). A database of videos downloaded from YouTube is built, , visually covering the world in space and time. Then the frames are extracted from these videos, keeping only the necessary ones but with enough visual information. Finally, the images from different videos of the same places are pre-processed to harmonise the colorimetry among the sets. 

## Libraries used 

The most important ones are beautifulsoup, pandas, and requests. Beautifulsoup allows us to navigate, search and modify a parse tree in HTML file. Requests library is used to send an HTTP request to the server of the page I want to scrape (which is in this project the unesco sites website). The server responds by sending the HTML content of the web page. The library pandas is widely used in this project, it is used in general for data analysis tasks because it deals with dataframe and go through reading data, analyze it, manipulate, and finally store it.

## Results

1) unesco_sites_cleaned.csv file contains all the places of the unesco sites in the format [URL; name; coordinates] with a total of 1195 URLs.

2) video_info.csv file contains all the video ids found on YouTube, along with place, duration, title, date, height and filesize of each video, in the format [id,place,duration,title,date], with a total of 28 493 videos, around 30 videos for each location.

3) venice_info.csv file contains all the videos ids found on Youtube for the specific place Venice, along with the duration, title and date of each video, in the format [id,duration,title,date] with a total of 28 videos.
