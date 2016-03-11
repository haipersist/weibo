#!/usr/bin/env python
#!-*-coding:utf-8-*-

"""
config.py:set the global varaible that will be used in authorization and operation weibo

Copyright C Haibo Wang.2016

the file has two config class:auth_config and spider_config

"""


import os



CUR_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])

class AuthConfig():
	app_key = '3318682448'
	app_secret = '3d8c513a2dc2358322a25cb40f1790e4'
	callback_url = 'https://api.weibo.com/oauth2/default.html'
	post_url = 'https://api.weibo.com/oauth2/authorize'
	userid = '393993705@qq.com'
	passwd = ''



class SpiderConfig():
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
	host = 'api.weibo.com'



	

