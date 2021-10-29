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

