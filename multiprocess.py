#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import multiprocessing
import random
import urllib
import re
import yaml

class NeetsDaemon(object):

	def __init__(self, processes):
		self.processes = processes
		self.queue = multiprocessing.Queue()

	def start(self):
		for i in range(self.processes):
			# 新しいプロセスを作る
			p = multiprocessing.Process(target=self._child_main_loop,
										args=(self.queue, ))
			# デーモンフラグを有効にすると親プロセスが死んだとき一緒に死ぬようになる
			p.daemon = True
			# プロセスを開始する
			p.start()
		# 自分もメインループに入る
		self._parent_main_loop()

	# 親プロセスのループ
	def _parent_main_loop(self):
		while True:
			print self.queue.get()

	# 子プロセスのループ
	def _child_main_loop(self, queue):
		while True:
			url = "http://geekhost.net/OK"
			f = urllib.urlopen(url)
			data = f.read()
			#print data
			abcPattern = re.compile(r'OK')
			if abcPattern.match(data):
				queue.put('Already logined')
			else:
				queue.put('Need login')
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
				print repr(params)
				up = urllib.urlopen(LOGIN_URL, params)
			# あとは寝てる
			time.sleep(yaml.load(open('config.yaml').read().decode('utf-8'))['threadtime'])

if __name__ == '__main__':
	neetsd = NeetsDaemon(1)
	# デーモンを開始する
	neetsd.start()