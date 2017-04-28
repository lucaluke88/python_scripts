import requests
import sys
import json
import os

# save the json of the museum
def download_json(url,file_path):
    print("Crawling : " + url)
    data = requests.get(url).json()
    with open(file_path, 'w') as outfile:
     json.dump(data, outfile)
     print("Saved as "+file_path)
    return data

argNumber = len(sys.argv)
if(argNumber == 0):
    print("You must specify an URL and a file name!")

url = sys.argv[1]
file = sys.argv[2]

json_data = download_json(url,file)