# -*- coding:utf-8 -*-

"""
the module can get code automatically instead of getting from url manually.
meanwhile,set token for client

Usage:
	weibo = WeiboAuth('39q.com','n','33186','3d8c513a2dc2e4')
	#weibo.set_token()

Copyright(c) 2017. Haibo Wang

"""

from weibo import APIClient
import config
from ticket4code import Ticket


class WeiboAuth(object):

	def __init__(self,username,passwd,app_key,app_secret,callback_url=None):
		self.passwd,self.username  = passwd, username
		self.app_key, self.app_secret = app_key,app_secret
		self.callback_url = callback_url
		self.client = self._set_client()
		self.ticket = Ticket(self.username,self.passwd)
		self._set_session()

	def _set_session(self):
		self.session = self.ticket.session
		self.headers = {
   			 "User-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
             "Referer": self.client.get_authorize_url(),
             "Content-Type": "application/x-www-form-urlencoded"
		}

	def _set_client(self):
		if self.callback_url is None:
			self.callback_url = config.CALLBACK_URL

		return  APIClient(
				app_key=self.app_key,
				app_secret=self.app_secret,
				redirect_uri=self.callback_url)

	@property
	def code(self):
		ticket = self.ticket.ticket
		REG_CALLBACK_URL_FOR_TICKET = 'https://api.weibo.com/2/oauth2/authorize?client_id=' +\
			self.app_key + \
			'&response_type=code&display=default&redirect_uri=' + \
			config.CALLBACK_URL + \
			'&from=&with_cookie=',
		data = config.CODE_POST_DATA
		data.update(
			{
				 'ticket': ticket,
				'regCallback': REG_CALLBACK_URL_FOR_TICKET,
				'client_id':self.app_key,
			}
		)
		get_code_url = self.session.post(config.AUTH_URL,data=data,headers=self.headers)
		return get_code_url.url[47:]

	def set_token(self):
		code = self.code
		#By far, I can not get code automatically by posting form data
		#so I got code mannually first,then get token using this code,and store token
		#token can be valid for 5 years.
		token = self.client.request_access_token(code)
		self.client.set_access_token(token['access_token'],token['expires_in'])



if __name__ == "__main__":
	#weibo = WeiboAuth('39q.com','n','33186','3d8c513a2dc2e4')
	#weibo.set_token()
	pass


	

