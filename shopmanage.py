#!/bin/env python
#_*_coding:utf-8_*_
#Author:swht
#E-mail:qingbo.song@gmail.com
#Date:2015.11.24
#Version:V0.0.1

import shoplogin
import banklogin
import linecache
import time
import random

moneynum = 0

#获取文件的行数
# def countnum(filename):
# 	count = 0
# 	thefile = open(filename, 'rb')
# 	while True:
# 	    buffer = thefile.read(8192*1024)
# 	    if not buffer:
# 	        break
# 	    count += buffer.count('\n')
# 	return count
# 	thefile.close()
def countnum(filename):
	files = open(filename)
	data = files.read()
	files.flush()
	files.close()
	return data.count('\n')
def shopping(choiceshop):
	#获取文件中某一行字符串
	linecache.clearcache()  #刷新缓存数据
	line = linecache.getline('shoplist.txt',choiceshop)
	#将字符串转换成列表
	line = line.split()
	usershoplist = open('usershoplist.txt','a')
	print '''
================================================
你已将%s添加到购物车,消费%s元!
================================================
''' % (line[1],line[2])
	usershoplistline = '''%s %s\n''' % (line[1],line[2])
	usershoplist.write(usershoplistline)
	usershoplist.close()

def clearshopping():	#用户退出购物中心时清空(初始化)购物车
	usershoplist = open('usershoplist.txt','rb+')
	usershoplist.truncate()	#清空文件
	usershoplist.close()

def showshopping(title = "购物车"):  #展示购物车信息
	data = open('usershoplist.txt').read()
	if len(data) == 0:
		print "你的购物车为空,请选择指定指令添加商品!"
	else:
		global moneynum 
		moneynum = 0 #初始化全局变量,防止金额计算多次
		print '*****************%s******************'%(title)
		print '%s\t\t%s%s%s\t\t%s'% (u'商品名称',u'单价',u'*',u'数量',u'总价')
		for num in range(1,countnum('usershoplist.txt')+1):	#countnum() = countnum()+1 表示获取的数值(实际行数)+1(取值范围+1)
			#获取用户购物车列表的每行内容,并将其转换成列表
			linecache.clearcache()  #刷新缓存数据
			usershoplistline = linecache.getline('usershoplist.txt',num).strip('\n').split(' ')
			print "%s\t%s%s%s\t\t%s元\n" % (usershoplistline[0],usershoplistline[1],'*','1',usershoplistline[1]),
			moneynum += int(usershoplistline[1])  #将全局变量moneynum进行了修改,其他函数调用这个变量时就会携带修改后的值
		print "总金额: %d " % moneynum
	

def buyshopping():
	showshopping()
	global moneynum #使用全局变量,目的是将需要支付的钱
	flag = 0
	while flag <= 3:
		choiceshoptry = raw_input('''请确认你本次消费总金额为%s元[y/n]''' % moneynum).strip()
		if len(choiceshoptry) == 0:
			flag += 1
			print "输入不能为空,请重新输入[y/n]确认!"
		else:
			if choiceshoptry == 'Y' or choiceshoptry == 'y' or choiceshoptry == 'N' or choiceshoptry == 'n':
				if choiceshoptry == 'y' or choiceshoptry == 'Y':					
					orders()
					# print '跳转到信用卡支付页面'
					banklogin.bank_login()
				if choiceshoptry == 'n' or choiceshoptry == 'N':
					print '你本次确认不结算购物车内商品!%s' % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) #格式化输出当前时间2015-11-29 15:39:30
					break
			else:
				flag += 1
				print "你的输入有误,请重新输入[y/n]!"
	print "系统将退出购物车!"
	time.sleep(1)

def orders():
	global moneynum
	#创建订单列表
	usrshophistorylist = open('usrshophistorylist.txt','a')
	create_shopID = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) + '' + str(random.randint(100, 200))
	for num in range(1,countnum('usershoplist.txt')+1):	#countnum() = countnum()+1+1 表示获取的数值+1(实际行数)+1(取值范围+1)
		linecache.clearcache()  #刷新缓存数据
		usershoplistline = linecache.getline('usershoplist.txt',num).strip('\n').split(' ')
		form = "%s\t%s\t%s%s%s\t\t%s\n" % (create_shopID,usershoplistline[0],usershoplistline[1],'*','1',usershoplistline[1])
		usrshophistorylist.write(form)
	formall = '''需支付金额为: %d 元\n''' % moneynum
	usrshophistorylist.write(formall)
	usrshophistorylist.close()
