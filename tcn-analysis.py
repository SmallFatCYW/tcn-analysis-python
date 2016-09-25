#!/usr/bin/env python

"""
t.cn JSON and XML Analysis - v0.2
By iPixelOldC & http://hoc117.top
License: MIT
"""

import json
import xml.etree.cElementTree as et
import urllib.request
import re
import os

reRule = re.compile(r'(http://+)(.*)')
xj = ['x', 'j']

def JSONReturn(site):
    """
    json analysis: JSONReturn(site='Website URL(format:http[s]://xxx)')
    return: {'url_short': 'http://t.cn/xxx', 'url_long': site, 'type': 0, "result": True}
    type: 链接的类型，0：普通网页(site page)、1：视频(video)、2：音乐(music)、3：活动(activity)、5、投票(vote)
    """
    response = urllib.request.urlopen('http://api.t.sina.com.cn/short_url/shorten.json?source=3271760578&url_long=%s' % (site))
    html = response.read().decode('utf8')
    loads = json.loads(str(html))
    return loads[0]
def XMLReturn(site):
    """
    xml analysis: XMLReturn(site='Website URL(format:http[s]://xxx)')
    return: {'url_short': 'http://t.cn/xxx', 'url_long': site}
    """
    response = urllib.request.urlopen('http://api.t.sina.com.cn/short_url/shorten.xml?source=3271760578&url_long=%s' % (site))
    html = response.read().decode('utf8')
    loads = et.fromstring(str(html))[0]
    return {"url_short": loads[0].text, "url_long": loads[1].text, "type": loads[2].text}

if __name__ == "__main__":
    print('T.cn-Analysis by iPixelOldC (Blog: http://hoc117.top )')
    inputurl = input('>>Please enter url: ')
    if 'http://' in inputurl:
        pass
    else:
        inputurl = 'http://'+inputurl
    while True:
        inputJorX = input('>>xml(x) or json(j): ').lower()
        if inputJorX not in xj:
            print("> Please enter 'x' or 'j'!")
        else:
            break
    if 'x' == inputJorX:
        r_xml = XMLReturn(inputurl)
        print(">>%s: \n> Short URL: %s" % (r_xml["url_long"], r_xml["url_short"]))
    if 'j' == inputJorX:
        r_json = JSONReturn(inputurl)
        print(">>%s: \n> Short URL: %s" % (r_json["url_long"], r_json["url_short"]))
        while True:
            save_yn = input('>>Do you want to save it?[Y/n]').lower()
            if save_yn != 'y':
                print("> Please enter 'y' or 'n'!")
            else:
                print("> Saving...")
                open('%s.json' % (reRule.search(inputurl).group(2)), 'w+').write(str(JSONReturn(inputurl)))
                print("> OK")
                break
