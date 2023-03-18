import urllib.request
request_url = urllib.request.urlopen('https://api.thingspeak.com/channels/2071274/feeds.json?api_key=UJG4FP1L1XVSO0GO&results=2')
print(request_url.read())