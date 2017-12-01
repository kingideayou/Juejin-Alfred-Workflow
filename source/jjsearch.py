# encoding: utf-8
 # -*- coding: utf-8 -*-  

import sys
import argparse
from workflow import Workflow, ICON_WEB, web

ICON_JUEJIN = 'icon.png'

# iOS 5597838ae4b08a686ce23139
# Kotlin 56c40b1d2e958a0059a1b719
# Android 5597838ee4b08a686ce2319d
# Java 559a7207e4b08a686d25703e
# 前端 5597a05ae4b08a686ce56f6f
# JavaScript 55964d83e4b08a686cc6b353
# Vue 555e9a98e4b00c57d9955f68
# 算法 55cd843d60b203b0519307a9
# 掘金翻译计划 56b5a7f3df0eea00544e1993
# 机器学习 55e2a9f600b04a63ffb7b443
# 面试 55979fe6e4b08a686ce562fe

def tag(key):
    if 'android' in key.lower():
        return '5597838ee4b08a686ce2319d'
    elif 'ios' in key.lower():
        return '5597838ae4b08a686ce23139'
    elif 'kotlin' in key.lower():
        return '56c40b1d2e958a0059a1b719'
    elif 'java' in key.lower():
        return '559a7207e4b08a686d25703e'
    elif 'vue' in key.lower():
        return '555e9a98e4b00c57d9955f68'
    elif '前端'.decode("utf-8") in key.lower():
        return '5597a05ae4b08a686ce56f6f'
    elif 'qianduan' in key.lower():
        return '5597a05ae4b08a686ce56f6f'
    elif '算法'.decode("utf-8") in key.lower():
        return '55cd843d60b203b0519307a9'
    elif 'suanfa' in key.lower():
        return '55cd843d60b203b0519307a9'
    elif '翻译'.decode("utf-8") in key.lower():
        return '56b5a7f3df0eea00544e1993'
    elif 'fanyi' in key.lower():
        return '56b5a7f3df0eea00544e1993'
    elif '面试'.decode("utf-8") in key.lower():
        return '55979fe6e4b08a686ce562fe'
    elif 'mianshi' in key.lower():
        return '55979fe6e4b08a686ce562fe'
    else:
        return '56b5a7f3df0eea00544e1993'

def get_post_by_tag(query):
    url = 'http://timeline-merger-ms.juejin.im/v1/get_tag_entry?src=alfred&tagId=%s&page=0&pageSize=20&sort=rankIndex' % query 
    r = web.get(url)

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    r.raise_for_status()

    # Parse the JSON returned by pinboard and extract the posts
    result = r.json()
    posts = result['d']['entrylist']
    return posts

def main(wf):
 
 # Get query from Workflow
 if len(wf.args):
     posts = get_post_by_tag(tag(''.join(wf.args)))
 else:
     posts = get_post_by_tag('5597a05ae4b08a686ce56f6f')
     

 # Loop through the returned posts and add an item for each to
 # the list of results for Alfred
 for post in posts:
     wf.add_item(title=post['title'],
                 valid=True,
                 arg=post['originalUrl'],
                 subtitle=post['originalUrl'],
                 icon=ICON_JUEJIN)

 # Send the results to Alfred as XML
 wf.send_feedback()


if __name__ == u"__main__":
 wf = Workflow()
 sys.exit(wf.run(main))