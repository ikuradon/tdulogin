#/bin/env python
# -*- coding: utf-8 -*-
import urllib
import yaml
LOGIN_URL = 'https://auth-wlc.ntwk.dendai.ac.jp/login.html'
#LOGIN_URL = 'http://geekhost.net/checkparams.php'
pd = yaml.load(open('config.yaml').read().decode('utf-8'))
pd['buttonClicked'] = '4'
pd['redirect_url'] = 'http://google.com/'
pd["err_flag"] = "0" 
pd["err_msg"] = ""
pd["info_flag"] = "0"
pd["info_msg"] = ""
params = urllib.urlencode(pd)
#print repr(params)
up = urllib.urlopen(LOGIN_URL, params)
print up.read()
#curl -d 'username=09rd216' -d 'password=lvd3nda4' -d 'buttonClicked=4' -d 'redirect_url=google.com' https://auth-wlc.ntwk.dendai.ac.jp/login.html
