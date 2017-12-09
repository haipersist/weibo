# -*- coding:utf-8 -*-

"""
the class mainly  create ticket,which is used to get code from sina server.
you must provide two parameters:username and password.

Usage:
		ticket = Ticket('username','password')
		print ticket.ticket

Copyright(c) 2017. Haibo Wang

"""


import requests
import config
from utils import get_su,get_sp



class Ticket(object):

	def __init__(self,username,passwd,callback_url=None):
		self.passwd,self.username  = passwd, username
		self.callback_url = callback_url
		self._set_session()

	def _set_session(self):
		self.session = requests.Session()
		self.headers = {}

	@property
	def su(self):
		return get_su(self.username)

	def sp(self,*args):
		servertime,nonce,pubkey,rsakv = args
		return get_sp(self.passwd,pubkey,servertime,nonce)

	def get_para_for_ticket(self):
		url = config.PRE_LOGIN_URL + '&su={0}'.format(self.su)
		content = self.session.get(url).content.split(',')
		servertime = content[1].split(':')[1]
		nonce = content[3].split(':')[1][1:-1]
		pubkey = content[4].split(':')[1][1:-1]
		rsakv = content[5].split(':')[1][1:-1]
		return servertime,nonce,pubkey,rsakv

	@property
	def ticket(self):
		#self.headers['Referer'] = self.get_authorize_url()
		servertime,nonce,pubkey,rsakv = paras = self.get_para_for_ticket()
		data = config.TICKET_POST_DATA
		data.update({
			'su': self.su,
            'servertime': servertime,
            'nonce': nonce,
            'rsakv' : rsakv,
            'sp': self.sp(*paras),
		})
		#print 'data',data
		#post_data = urllib.urlencode(data)
		r = self.session.post(config.TICKET_URL,data)
		return r.content.split(',')[1].split(':')[1][1:-1]



if __name__ == "__main__":
	ticket = Ticket('****','********')
	print ticket.ticket



