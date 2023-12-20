import urllib.request
import pprint

nasaurl = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
apodurlobj = urllib.request.urlopen(nasaurl)
dir(apodurlobj)
apodurlobj.code
apodurlobj.msg
apodurlobj.length
apod = apodurlobj.read().decode("utf-8")
pprint.pprint(apod)

