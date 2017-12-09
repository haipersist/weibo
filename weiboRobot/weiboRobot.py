#-*-coding:utf-8-*-


"""
weiborobot:the module providesone base class ,every user can user it to send weibo

you must have username,password,app_key,app_serret,callback_url

app_key,app_serret,callback_url is set in weibo platform,you should set up your app first

Of Course,you can inherit from the base class


Copyright C Haibo wang.2017

"""

from auth import WeiboAuth




class WeiboRobot(object):

	def __init__(self,username,passwd,app_key,app_secret,callback_url=None,domain=u'http://hbnnforever.cn'):
		"""
		the class is one api to weiboauth
		domain:the domain is used to add http for sending weibo.because from 2017.6.26 on,sending weibo api
		is statuses/share.so you must add one domain in text.
		the default value is my website.you can add value whatever you want to add.
		"""
		#the text must have http.
		self.domain = domain
		self.weibo = WeiboAuth(username,passwd,app_key,app_secret,callback_url)
		self.robot = self._client_robot

	@property
	def _client_robot(self):
		#when the instance is created ,the instance should create code,set token for the client
		#the class use proxy design ,the robot does everyting that client does
		self.weibo.set_token()
		return self.weibo.client

	def publish_text(self,text):
		if not isinstance(text,unicode):
			text = unicode(text,'utf-8')
		self.robot.statuses.share.post(status=u'{1}//程序发送自{0}'.format(self.domain,text))

	def publish_pic(self,text,photo):
		pass




if __name__ == "__main__":
	robot = WeiboRobot('***','****','***','***')
	text = u'test. @今日头条'
	robot.publish_text(text)


