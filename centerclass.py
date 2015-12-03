#!/bin/env python
#_*_coding:utf-8_*_
#Author:swht
#E-mail:qingbo.song@gmail.com
#Date:2015.11.24
#Version:V0.0.1

class Center(object):	
	"""docstring for Center"""
	def __init__(self,center):
		self.center = center
	def Print(self):
		print u'''\t\t\t===欢迎光临%s===\t\t\t''' %self.center

#信用卡中心
class Credit(Center):
	"""docstring for Credit"""
	def __init__(self,center):
#		Center.__init__(self,center)
		super(Credit, self).__init__(center)
		self.center = center

	def Print(self):
		Center.Print(self)
		print '''\t\t请登录信用卡中心\t\t退出:quit'''

class ShopCenter(Center):
	"""docstring for ShopCenter"""
	def __init__(self,center):
		super(ShopCenter, self).__init__(center)
		self.center = center

	def Print(self):
		Center.Print(self)
		print '''\t\t请登录二手数码产品中心\t\t退出:quit'''


shop = ShopCenter(u"二手数码产品中心")
bank = Credit(u"信用卡中心")