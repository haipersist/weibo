# -*- coding:utf-8 -*-

"""
the module provides two functions ,which is used to get su and sp.

CopyRight (c) 2017. Haibo Wang

"""

import rsa
import binascii
import  base64



def get_su(username):
	return base64.encodestring(username)

def get_sp(pwd,pubkey,servertime,nonce):
	rsaPublickey = int(pubkey, 16)
	key = rsa.PublicKey(rsaPublickey, 65537)
	message = ''.join(
		[
			str(servertime),
		   '\t' ,
			str(nonce) ,
			'\n' ,
			str(pwd)
		]
	)
	return binascii.b2a_hex(rsa.encrypt(message, key))

