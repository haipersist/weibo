#!/usr/bin/env python
#-*-coding:utf-8-*-


import requests
import os
import urllib
import urllib2
import json
import sys
from weibo import APIClient
from config import AuthConfig,SpiderConfig,CUR_DIR

class WeiboAuth():

	def __init__(self,passwd):
		self.passwd = passwd
		self._set_session()
		self._set_client()
	
	def _set_session(self):
		self.session = requests.Session()
		self.spi_cfg = SpiderConfig()
		self.headers = {}
		self.headers['User-Agent'] = self.spi_cfg.user_agent
		self.headers['Host'] = self.spi_cfg.host
		self.headers['path'] = '/oauth2/authorize'
		self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
		self.headers['origin'] = 'https://api.weibo.com'

	def _set_client(self):
		self.auth_cfg = AuthConfig()
		self.client = APIClient(
				app_key=self.auth_cfg.app_key,
				app_secret=self.auth_cfg.app_secret,
				redirect_uri=self.auth_cfg.callback_url)


	def get_authorize_url(self):
		return self.client.get_authorize_url()

	def get_code(self):
		self.headers['Referer'] = self.get_authorize_url()
		print self.get_authorize_url()
		data = {
				'action':'login',
				'display':'default',
				'withOfficalFlag':'0',
				'ticket':'',
				'isLoginSina':'',
				'response_type':'code',
				'regCallback':'',
				'redirect_uri':'https%3A%2F%2Fapi.weibo.com%2Foauth2%2Fdefault.html',
				'client_id':'3318682448',
				'appkey62':'5lAqHu',
				'state':'',
				'verifyToken':'null',
				'from':'',
				'switchLogin':'0',
				'userId':self.auth_cfg.userid,
				'passwd':self.passwd
		}
		post_data = urllib.urlencode(data)
		req = urllib2.Request(self.auth_cfg.post_url)
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		header_list = [(key,self.headers[key]) for key in self.headers.keys()]
		print header_list
		opener.addheaders = header_list
		#urllib2.install_opener(opener)
		resp = opener.open(req,post_data)
		return resp.read()
		
		
	def get_token(self):
		#By far, I can not get code automatically by posting form data
		#so I got code mannually first,then get token uding this code,and store token 
		#token can be valid for 5 years.		
		code = 'd6bc6fe270576aa5a39f61258f73ebd1'  # get code mannually by visiting referer url
		token = self.client.request_access_token(code)
		json_token = json.dumps(token)
		print >>file(os.path.join(CUR_DIR,'token.json'),'w'),json_token



if __name__ == "__main__":
	weiboRobot = WeiboAuth(sys.argv[1])
	print weiboRobot.get_authorize_url()
	weiboRobot.get_token()
	

	

	

