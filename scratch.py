import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'


# Doesnot execute Javascript and hence the data doesn't get loaded dynamically
response = requests.get(YOUTUBE_TRENDING_URL)

print('Status Code:', response.status_code)

#print('Output:', response.text[:1000])

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page title:', doc.title)

print('Page title:', doc.title.text)

video_divs = doc.find_all('div', class_ = 'style-scope ytd-video-renderer')

# Find all the video divs
print(f'Found {len(video_divs)} videos')

'''
We need to create a fake browser or a headless browser and hence simulate an entire browser
A browser which doesn't have the UI ,i.e doesn't display the page, but still runs all the Javascript on the page. Then we need to pick info from the page that is loaded in the fake browser. This is where Selenium comes into picture. Selenium automates browser.

We will use it for extracting info from the trending page on youtube.

Selenium is a python API which uses the drivers to interact with the web browsers.

'''



'''

video = videos[0]
  


  print('Title:', title)
  print('URL:', url)
  print('Thumbnail URL:', thumbnail_url)
  print('Channel Name:', channel_name)
  print('Description:', description)
  print('Views:',views)
  print('Uploaded Duration:',uploaded)


'''