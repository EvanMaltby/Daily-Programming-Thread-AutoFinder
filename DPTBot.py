import urllib
import sys
import webbrowser
List = [] 
loop = 1
if len(sys.argv) > 1:
  page = int(sys.argv[1])
else:
  page = 0
while page != 11:
	sock = urllib.urlopen("http://boards.4chan.org/g/" + str(page))
	htmlSource = sock.read()
	if htmlSource.find("Daily Programming Thread") != -1 or htmlSource.find("DPT") != -1:
		x = htmlSource[htmlSource.find("Daily Programming Thread"):]
		i = x.split("data-utc")
		j = i[1].split("href=")
		k = j[1].split("\"")
		x = i[1].split("<")
		i = x[0].split(">")
		print "DPT Was found at page: " + str(page) + " created at:" + i[1] 
		webbrowser.open("http://boards.4chan.org/g/" + k[1])
	else:
		print "DPT was not found at page " + str(page)
	page += 1
