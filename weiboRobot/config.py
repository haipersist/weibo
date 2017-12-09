#!/usr/bin/env python
#!-*-coding:utf-8-*-

"""
config.py:set the global varaible that will be used in authorization and operation weibo

Copyright C Haibo Wang.2016

the file has two config class:auth_config and spider_config

"""





CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'

PRE_LOGIN_URL = 'https://login.sina.com.cn/sso/prelogin.php?entry=openapi&callback=sinaSSOController.preloginCallBack' + \
				'&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)'

TICKET_URL = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'

AUTH_URL = 'https://api.weibo.com/oauth2/authorize'



TICKET_POST_DATA =  {
        	'entry': 'openapi',
        	'gateway': '1',
            'from':'',
            'savestate': '0',
            'userticket': '1',
            'pagerefer':'',
            'ct': '1800',
            's':'1',
            'vsnf': '1',
            'vsnval': '',
            'door':'',
            #'appkey':'5lAqHu',
	 		'appkey': '52laFx',
            'service': 'miniblog',
			'pwencode': 'rsa2',
            'sr':'1920*1080',
            'encoding': 'UTF-8',
            'cdult':'2',
            'domain':'weibo.com',
            'prelt':'46',
            'returntype': 'TEXT'
        }

CODE_POST_DATA = {
    'action': 'login',
    'display': 'default',
    'withOfficalFlag': '0',
    'quick_auth': 'null',
    'withOfficalAccount': '',
    'scope': '',
    'isLoginSina': '',
    'response_type': 'code',
    'redirect_uri':CALLBACK_URL,
    'appkey62': '52laFx',
    'state': '',
    'verifyToken': 'null',
    'from': '',
    'switchLogin':'0',
    'userId':'',
    'passwd':''
    }





