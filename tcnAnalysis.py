import json
import xml.etree.cElementTree as et
import urllib.request
import re
import os


reRule = re.compile(r'[http://]+')
def openxml(site):
	response = urllib.request.urlopen('http://api.t.sina.com.cn/short_url/shorten.xml?source=3271760578&url_long=%s' % (site))
	html = response.read().decode('utf8')
	sitesplit = reRule.split(site)
	write = open('%s.xml' % sitesplit[1], 'w+').write(html)
	return sitesplit[1]+'.xml'


def openjson(site):
	response = urllib.request.urlopen('http://api.t.sina.com.cn/short_url/shorten.json?source=3271760578&url_long=%s' % (site))
	html = response.read().decode('utf8')
	sitesplit = reRule.split(site)
	write = open('%s.json' % sitesplit[1], 'w+').write(html)
	return sitesplit[1]+'.json'


def readjson(jsonfile):
	openJson = open(jsonfile, 'r').read()
	Json2dict = json.loads(openJson)
	return (Json2dict[0]['url_short'], Json2dict[0]['url_long'])

def readxml(xmlfile):
	openxml = et.parse(xmlfile).getroot()
	return (openxml[0][0].text, openxml[0][1].text)


def urlReturn(xorjtotuple):
	deftuple = ('short_url', 'long_url')
	dictsu = dict(zip(deftuple, xorjtotuple))
	dicttojson = json.dumps(dictsu)
	save = open('tcn.json', 'w+')
	save.write(dicttojson)
	save.close()

print('tcn-analysis by iPixelOldC (Blog:http://hoc117.top )')
inputurl = input('Please enter url: ')
if 'http://' in inputurl:
	pass
else:
	inputurl = 'http://'+inputurl
inputJorX = input('xml(x) or json(j): ')
if 'x' == inputJorX:
	demo = readxml(openxml(inputurl))
	print('[!]OK!')
	print('longurl: {0}\nshorturl: {1}'.format(demo[1], demo[0]))
	os.remove(openxml(inputurl))
	needsave = input('Are you need save to json?(tcn.json)[Y]: ').lower()
	if needsave == 'y':
		urlReturn(demo)
	else:
		pass

if 'j' == inputJorX:
	demo = readjson(openjson(inputurl))
	print('[!]OK!')
	print('longurl: {0}\nshorturl: {1}'.format(demo[1], demo[0]))
	os.remove(openjson(inputurl))
	needsave = input('Are you need save to json?(tcn.json)[Y]: ').lower()
	if needsave == 'y':
		urlReturn(demo)
	else:
		pass
print('Exit!')
