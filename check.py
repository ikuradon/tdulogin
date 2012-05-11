#!/bin/env python

import urllib
import re
url = "http://geekhost.net/OK"
f = urllib.urlopen(url)

data = f.read()
print data
abcPattern = re.compile(r'OK')

if abcPattern.match(data):
    print 'match'
else:
    print 'not match'
