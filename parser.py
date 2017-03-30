#!/usr/bin/python
import feedparser

import urllib3
import urllib.request

URL = "http://feeds.gimletmedia.com/hearreplyall?format=xml"
feed = feedparser.parse(URL)

urls = []

for post in feed.entries:
	print(str(post.title)) 
	#print(str(post))
	#print(str(post.description))
	#print(str(post.media_content)) #Media
	#print(str(post.media_content[0]['url']))
	#print(str(post.media_content[0]['filesize']))
	#print(str(post.media_content[0]['type']))
	urls.append(post.media_content[0]['url'])

first = urls[0]
print(first)


#mp3file = urllib3.urlopen(first)
#r = http.request('GET', first)

#with open('./test.mp3','wb') as output:
#  output.write(mp3file.read())

#print(mp3file)
#song = AudioSegment.from_mp3("./test.mp3")
#play(song)

#urllib.request.urlretrieve(first, './test.mp3')



