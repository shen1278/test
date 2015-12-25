#!/bin/env python
#_*_coding:utf-8_*_
#Author:swht
#E-mail:qingbo.song@gmail.com
#Date:2015.11.24
#Version:V0.0.1

import re
import centerclass
import main
import time
import shopmanage
#登录信息核对
userdict = {'User':'shen1234','Pass':'123456'}
def shop_login():
	centerclass.shop.Print()
	flag = 0
	while flag <= 3:
		userId = raw_input("请输入你的账号:").strip()
		userPass = raw_input(u"请输入你的密码:").strip()
		if len(userId) != 0:
			if  re.match('^[0-9a-zA-Z]+$',userId):
				ifShopId(userId, userPass, flag)
			else:
				print "你输入的账户类型不正确,请重新输入!"
				flag += 1
		else:
			flag += 1
			print "用户名不能为空,请重新输入!"
	print "你输入的错误次数已达3次,程序将退出!"
	main.welcome()
def ifShopId(userId,userPass,flag):
	if userdict['User'] == userId:
		if userdict['Pass'] == userPass:
			LoginShopSucess(userId)
		else:
			flag += 1
			print "你输入的密码错误,请重新输入!"
	else:
		if userId == 'quit':
			print "系统即将退出!"
			time.sleep(1)
			main.welcome()
		else:
			flag += 1
			print "你输入的用户名有误,请重新输入!"
		flag += 1
		print "你输入的用户名有误,请重新输入!"
def LoginShopSucess(userId):
	flag = 0
	while flag <= 5:
		print '''
\t=========欢迎用户%s登录到二手数码产品中心=========
\t1.iphone 6s手机 4500元 	\t\t2.华为荣耀6plus 2200元
\t3.TP-Link无线路由 120元	\t\t4.联想笔记本 2500元
\t5.小米平板 200元       	\t\t6.战神鼠标 100元
\t7.超神机械键盘 200元   	\t\t8.查看购物车
\t9.结算                    \t\t10.退出
''' % userId
		choiceshop = raw_input('请选择指令:').strip()
		if len(choiceshop) == 0:
			flag += 1
			print "指令不能为空,请重新输入![1-10]"
		else:
			choiceshop = int(choiceshop)
			if choiceshop >= 1 and choiceshop <= 10:
				if choiceshop >= 1 and choiceshop <= 7:
					shopmanage.shopping(choiceshop)
				# if choiceshop == 2:
				# 	print '2'
				# if choiceshop == 3:
				# 	print '3'
				# if choiceshop == 4: 
				# 	print '4'
				# if choiceshop == 5:
				# 	print '5'
				# if choiceshop == 6:
				# 	print '6'
				# if choiceshop == 7:	
				# 	print '7'
				if choiceshop == 8:		#查看购物车
					shopmanage.showshopping()
				if choiceshop == 9:		#结算
					shopmanage.buyshopping()
				if choiceshop == 10:	#退出购物中心
					print '程序即将退出二手数码产品中心,欢迎下次光临!'
					shopmanage.clearshopping()
					time.sleep(1)
					main.welcome()
			else:
				flag += 1
				print "你输入的指令不在规定范围内,请重新输入![1-10]"
	print "你输入的错误次数已达5次!系统将退出!"
	time.sleep(1)
	shop_login()
			
