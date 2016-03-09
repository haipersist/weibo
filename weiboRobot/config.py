#!/usr/bin/env python
#!-*-coding:utf-8-*-

"""
config.py:set the global varaible that will be used in authorization and operation weibo

Copyright C Haibo Wang.2016

the file has two config class:auth_config and spider_config

"""


class AuthConfig():
	app_key = '513071462'
	app_secret = '18298fdf8d645aadf3e8d01cf85d8059'
	callback_url = 'http://hbnnlove.sinaapp.com'
	userid = '393993705@qq.com'
	passwd = ''



class SpiderConfig():
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
	host = 'api.weibo.com'



	

