#!/usr/bin/env python
#-*-coding:utf-8-*-


import datetime
import os
from send_weibo import Send_Weibo




class Robot():
	
	def __init__(self):
		self.now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
		self.weibo_robot = Send_Weibo()

	def ontime_reminder(self):
		text = "现在是北京时间：%s，我亲爱的朋友们，不要熬夜啦，赶紧睡觉。祝你们新的一天一切顺利，WonderfulDay！Behind you forever!@妞是回不去旧时光 ，@dudu19172 ,@Sherlyn1990 ，@dailinadia ,@天空之城hp。怕打扰到其他人，就不@了，也要早点休息哈." % self.now
		self.weibo_robot.send_weibo(text)
		


	

if __name__ == "__main__":
	robot = Robot()
	robot.ontime_reminder()

