import requests
import os
from sys import platform
import re
import webbrowser
import random
from datetime import datetime
import time

MAX_SHUTDOWN_TIME = 180#max shutdown time in minutes

class youtubeVideo:
    def __init__(self, videoID, videoLength):
      self.videoID = videoID,
      self.videoLength = videoLength
    def __str__(self):
       return f"{self.videoID}({self.videoLength})"
    
def remove_non_time(inputList):
   filteredList = []
   for i, input in enumerate(inputList):
      if ":" in input:
         filteredList.append(input)
   return filteredList

#Removes every other time because there was 2 of each :(
def remove_duplicates(inputList):
   filteredList = []
   for i, input in enumerate(inputList):
      if (i % 2) == 1:
         filteredList.append(input)
   return filteredList

def time_to_sec(times):
    convertedList = []
    for t in times:
        try:
            newTime = datetime.strptime(t, '%H:%M:%S')
        except ValueError:
            newTime = datetime.strptime(t, '%M:%S')
        convertedList.append((newTime.hour * 60) + newTime.minute + 1)
    return convertedList

baseChannelURL = "https://www.youtube.com/@{REPLACE_CHANNEL}/videos"
videoURL = "https://www.youtube.com/watch?v="

artistUsername = "JermaStreamArchive"
channelURL = baseChannelURL.replace("{REPLACE_CHANNEL}", artistUsername)

channelResponse = requests.get(channelURL)



channelResults = re.findall(r'url\"\:\"\/watch\?v\=(.*?(?=\"))', channelResponse.text)
channelTimes = re.findall(r'simpleText\":\"(.*?(?=\"))', channelResponse.text) #ds\"\}\},\"simpleText\":\"(.*?(?=\"))
channelTimes = remove_non_time(channelTimes)
channelTimes = remove_duplicates(channelTimes)
channelTimes = time_to_sec(channelTimes)

videoList = []

if platform == "linux" or platform == "linux2":
    shutdownCommand = "shutdown -P "
elif platform == "darwin":
    shutdownCommand = "shutdown -s +"
elif platform == "win32":
    shutdownCommand = "shutdown /s /t "
    
for i, result in enumerate(channelResults):
    if channelTimes[i] > MAX_SHUTDOWN_TIME:
       channelTimes[i] = MAX_SHUTDOWN_TIME
    if platform == "win32":
      videoList.append(youtubeVideo(result, channelTimes[i] * 60))
    else:
        videoList.append(youtubeVideo(result, channelTimes[i]))

if len(channelResults) != 0:
  vidIndex = random.randint(0, len(videoList) - 1)
  webbrowser.open(videoURL + (str)(videoList[vidIndex].videoID[0] + "&t=0"), new=0, autoraise=True)
  os.system(shutdownCommand + (str)(videoList[vidIndex].videoLength))