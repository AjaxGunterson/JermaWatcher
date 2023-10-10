import requests
import os
from sys import platform
import re
import webbrowser
import random

class youtubeVideo:
    def __init__(self, videoID, videoLength):
      self.videoID = videoID,
      self.videoLength = videoLength
    def __str__(self):
       return f"{self.videoID}({self.videoLength})"

baseChannelURL = "https://www.youtube.com/@{REPLACE_CHANNEL}/videos"
videoURL = "https://www.youtube.com/watch?v="
shutdownTime = 60

artistUsername = "JermaStreamArchive"
channelURL = baseChannelURL.replace("{REPLACE_CHANNEL}", artistUsername)

channelResponse = requests.get(channelURL)



channelResults = re.findall(r'url\"\:\"\/watch\?v\=(.*?(?=\"))', channelResponse.text)


videoList = []

if platform == "linux" or platform == "linux2":
    shutdownCommand = "shutdown -P "
elif platform == "darwin":
    shutdownCommand = "shutdown -s +"
elif platform == "win32":
    shutdownTime *= 60
    shutdownCommand = "shutdown /s /t "
    
for result, i in enumerate(channelResults):
   videoList.append(youtubeVideo(result, str(shutdownTime)))

if len(channelResults) != 0:
  vidIndex = random.randint(0, len(videoList) - 1)
  webbrowser.open(videoURL + videoList[vidIndex].videoID[0], new=0, autoraise=True)
  #os.system(shutdownCommand + str(videoList[vidIndex].videoLength))