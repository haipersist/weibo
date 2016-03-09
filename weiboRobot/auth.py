#!/usr/bin/env python
#-*-coding:utf-8-*-


from weibo import APIClient
import requests
from config import AuthConfig,SpiderConfig

class WeiboAuth():

	def __init__(self):
		self._set_session()
		self._set_client()
	
	def _set_session(self):
		self.session = requests.session()
		self.spi_cfg = SpiderConfig()
		self.session.headers['User-Agent'] = self.spi_cfg.user_agent
		self.session.headers['Host'] = self.spi_cfg.host

	def _set_client(self):
		self.auth_cfg = AuthConfig()
		self.client = APIClient(
				app_key=self.auth_cfg.app_key,
				app_secret=self.auth_cfg.app_secret,
				redirect_uri=self.auth_cfg.callback_url)


	def get_authorize_url(self):
		return self.client.get_authorize_url()

	def get_code(self):
		data = {
			'client_id':self.auth_cfg.app_key,
			'redirect_url':self.auth_cfg.callback_url,
			'userId':self.auth_cfg.userid,
			'passwd':self.auth_cfg.passwd,
			'isLoginSina':'0',
			'action':'submit',
			'response_type':'code'
		}	
		print 'refer_url',self.get_authorize_url()
		self.session.headers['Referer'] = self.get_authorize_url()
		resp = self.session.post(
				url = 'https://api.weibo.com/oauth2/authorize',
				data = data
				)
		return resp.url[-32:]

		
	def set_token(self):
		token = self.client.request_access_token(self.get_code())
		print 'token',token
		self.client.set_access_token(token.access_token,token.expires_in)

	def send_weibo(self):
		self.client.statuses.update.post(status='test program')



if __name__ == "__main__":
	weiboRobot = WeiboAuth()
	print weiboRobot.get_authorize_url()
#	weiboRobot.set_token()
#	weiboRobot.send_weibo()

	

	

