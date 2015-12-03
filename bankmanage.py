#!/bin/env python
#_*_coding:utf-8_*_
#Author:swht
#E-mail:qingbo.song@gmail.com
#Date:2015.12.02
#Version:V0.0.1

import banklogin
import shopmanage
import linecache
import time

#取款
def draw():
	#最后一行的索引值 int
	lastline = shopmanage.countnum('bank.txt')
	# print "lastline:",lastline
	# print u"lastline类型:",type(lastline)
	#当前余额 str->int
	linecache.clearcache()
	bankYue = int(linecache.getline('bank.txt',lastline).split('\t')[4])
	print u"你的信用卡当前余额为:%d元" % bankYue
	flag = 0
	while flag <= 3:
		choicelsit = raw_input('''
\t================================================\t
\t\t\t1.继续取款\t\t2.退出\t\t\t
\t================================================\t
\t请选择指令进行操作[1/2]:''').strip()
		if len(choicelsit) == 0:
			flag += 1
			print "指令不能为空,请重新输入[1/2]!"
		else:
			if choicelsit.isdigit():
				choicelsit = int(choicelsit)
				if choicelsit >= 1 and choicelsit <=2:
					if choicelsit == 1:
						# 取款条件判断
						flag = 0
						while flag <= 3:
							drawMoney = raw_input('''请输入你要取现的金额[100-%d]:''' % bankYue).strip()
							if len(drawMoney) == 0:  #判断用户输入的字符长度
								flag += 1
								print "金额不能为空,请重新输入[100-%d]!" % bankYue
							else: #字符长度不为0
								if drawMoney.isdigit(): #判断用户输入的金额是否为纯数字
									drawMoney = int(drawMoney) #纯数字转换成整数类型
									if drawMoney % 100 == 0: #判断用户输入的整数是否是100的倍数
										if drawMoney >= 100 and drawMoney <= bankYue: #判断用户输入的整数是否在余额范围内
											# 进行取款操作
											bankCar = open('bank.txt','a')
											bankDraw = '''%s\t%s\t%d\t%d\n''' %(time.strftime('%Y-%m-%d\t%H:%M:%S',time.localtime(time.time())),'取款',drawMoney,bankYue-drawMoney)
											bankCar.write(bankDraw)
											bankCar.close()
											time.sleep(2)
											print "取现成功!请取走你的钞票!"
											bankYue -= drawMoney
											time.sleep(1)
											break
										else: #不在余额范围内
											# if drawMoney > bankYue: #判断用户输入的整数是否超出余额
											print "余额不足,请减少取现数目[100-%d]!" % bankYue
									else: #非100的倍数输出异常
										flag += 1
										print "请输入整百的取现金额[100-%d]!" % bankYue
								else: #非纯数字输入异常
									flag += 1
									print "你的输入有误,金额只接收整百数字,请重新输入[100-%d]!" % bankYue
							
					if choicelsit == 2:
						print "系统将退出!"
						time.sleep(1)
						break
				else:
					flag += 1
					print "请输入正确的数字指令[1/2]!"
			else:
				flag += 1
				print "指令仅限整型数字[1/2]!"
	else:
		print "你输入的错误次数已达3次,系统将退出!"


#查询
def check():
	flag = 0
	while flag <= 3:
		#最后一行的索引值 int
		lastline = shopmanage.countnum('bank.txt')
		choicelsit = raw_input('''
\t===================================================\t
\t\t1.查询余额\t2.查询消费记录\t3.退出\t\t
\t===================================================\t
请选择指令进行操作[1-3]:''').strip()
		if len(choicelsit) == 0:
			flag += 1
			print "指令不能为空,请重新输入[1/2]!"
		else:
			if choicelsit.isdigit():
				choicelsit = int(choicelsit)
				if choicelsit >= 1 and choicelsit <= 3:
					if choicelsit == 1:
						#当前余额 str->int
						linecache.clearcache()
						bankYue = int(linecache.getline('bank.txt',lastline).split('\t')[4])
						print "你的信用卡当前余额为:%d元" % bankYue
					if choicelsit == 2:
						bankhislinenum = shopmanage.countnum('bank.txt')
						print "\t=====================消费记录=======================\t"
						for line in range(1,bankhislinenum+1):
							print '\t%s' % linecache.getline('bank.txt',line),
							# print type(line)
					if choicelsit == 3:
						print "系统将退出!"
						time.sleep(1)
						break
				else:
					flag += 1
					print "请输入正确的数字指令[1-3]!"
			else:
				flag += 1
				print "指令仅限整型数字[1-3]!"
	else:
		print "你输入的错误次数已达3次,系统将退出!"

#还款
def repayment():
	#最后一行的索引值 int
	lastline = shopmanage.countnum('bank.txt')
	#当前余额 str->int
	linecache.clearcache()  #刷新缓存数据
	bankYue = int(linecache.getline('bank.txt',lastline).split('\t')[4])
	print u"你的信用卡当前余额为:%d元" % bankYue
	flag = 0
	while flag <= 3:
		choicelsit = raw_input('''
\t================================================\t
\t\t\t1.继续还款\t\t2.退出\t\t\t
\t================================================\t
\t请选择指令进行操作[1/2]:''').strip()
		if len(choicelsit) == 0:
			flag += 1
			print "指令不能为空,请重新输入[1/2]!"
		else:
			if choicelsit.isdigit():
				choicelsit = int(choicelsit)
				if choicelsit >= 1 and choicelsit <=2:
					if choicelsit == 1:
						repaymoney = raw_input(u"请输入你的还款金额[1-%d]:" % bankYue).strip()
						if len(repaymoney) == 0:
							flag += 1
							print "金额不能为空,请重新输入[1-%d]!" % bankYue
						else:
							if repaymoney.isdigit():
								repaymoney = int(repaymoney)
								if repaymoney >= 1 and repaymoney <= bankYue:
									bankCar = open('bank.txt','a')
									bankRepay = '''%s\t%s\t%d\t%d\n''' %(time.strftime('%Y-%m-%d\t%H:%M:%S',time.localtime(time.time())),'还款',repaymoney,bankYue-repaymoney)
									bankCar.write(bankRepay)
									bankCar.close()
									time.sleep(2)
									print "还款成功!"
									# bankYue -= bankRepay
									time.sleep(1)
									break
								else:
									print "余额不足,请重新输入[1-%d]!" % bankYue
							else:
								flag += 1
								print "你的输入有误,金额只接收整数,请重新输入[1-%d]!" % bankYue
					if choicelsit == 2:
						print "系统将退出!"
						time.sleep(1)
						break
				else:
					flag += 1
					print "请输入正确的数字指令[1/2]!"
			else:
				flag += 1
				print "指令仅限整型数字[1/2]!"
	else:
		print "你输入的错误次数已达3次,系统将退出!"
#转账
def transfer():
	#最后一行的索引值 int
	linecache.clearcache()
	lastline = shopmanage.countnum('bank.txt')
	#当前余额 str->int
	bankYue = int(linecache.getline('bank.txt',lastline).split('\t')[4])
	print u"你的信用卡当前余额为:%d元" % bankYue
	flag = 0
	while flag <= 3:
		choicelsit = raw_input('''
\t================================================\t
\t\t\t1.继续转账\t\t2.退出\t\t\t
\t================================================\t
\t请选择指令进行操作[1/2]:''').strip()
		if len(choicelsit) == 0:
			flag += 1
			print "指令不能为空,请重新输入[1/2]!"
		else:
			if choicelsit.isdigit():
				choicelsit = int(choicelsit)
				if choicelsit >= 1 and choicelsit <=2:
					if choicelsit == 1:
						transmoney = raw_input(u"请输入你的转账金额[1-%d]:" % bankYue).strip()
						if len(transmoney) == 0:
							flag += 1
							print "金额不能为空,请重新输入[1-%d]!" % bankYue
						else:
							if transmoney.isdigit():
								transmoney = int(transmoney)
								if transmoney >= 1 and transmoney <= bankYue:
									bankCar = open('bank.txt','a')
									bankTrans = '''%s\t%s\t%d\t%d\n''' %(time.strftime('%Y-%m-%d\t%H:%M:%S',time.localtime(time.time())),'还款',transmoney,bankYue-transmoney)
									bankCar.write(bankTrans)
									bankCar.close()
									time.sleep(2)
									print "转账成功!"
									# bankYue -= bankRepay
									time.sleep(1)
									break
								else:
									print "余额不足,请重新输入[1-%d]!" % bankYue
							else:
								flag += 1
								print "你的输入有误,金额只接收整数,请重新输入[1-%d]!" % bankYue
					if choicelsit == 2:
						print "系统将退出!"
						time.sleep(1)
						break
				else:
					flag += 1
					print "请输入正确的数字指令[1/2]!"
			else:
				flag += 1
				print "指令仅限整型数字[1/2]!"
	else:
		print "你输入的错误次数已达3次,系统将退出!"

#支付
def shoppay():
	#最后一行的索引值 int
	lastline = shopmanage.countnum('usrshophistorylist.txt')
	#当前余额 str->int
	linecache.clearcache()
	bankYue = int(linecache.getline('bank.txt',shopmanage.countnum('bank.txt')).split('\t')[4])
	shopID = linecache.getline('usrshophistorylist.txt',lastline-1).split('\t')[0]
	shoppaymoney = int(linecache.getline('usrshophistorylist.txt',lastline).split(' ')[1])
	flag = 0
	while flag <= 3:
		choicelsit = raw_input("你即将为订单%s进行支付%d元,请你确认[y/n]:" % (shopID,shoppaymoney)).strip()
		if len(choicelsit) == 0:
			flag += 1
			print "输入不能为空,请重新输入[y/n]确认!"
		else:
			if choicelsit == 'Y' or choicelsit == 'y' or choicelsit == 'N' or choicelsit == 'n':
				if choicelsit == 'y' or choicelsit == 'Y':
					# 进行取款操作
					bankCar = open('bank.txt','a')
					bankDraw = '''%s\t%s\t%d\t%d\n''' %(time.strftime('%Y-%m-%d\t%H:%M:%S',time.localtime(time.time())),'购物',shoppaymoney,bankYue-shoppaymoney)
					bankCar.write(bankDraw)
					bankCar.close()
					time.sleep(2)
					print "支付成功!"
					# bankYue -= drawMoney
					time.sleep(1)
					break
				if choicelsit == 'n' or choicelsit == 'N':
					print '你本次确认不结算订单%s!' % shopID
					break
			else:
				flag += 1
				print "你的输入有误,请重新输入[y/n]!"
	else:
		print "你输入的错误次数已达3次,系统将退出!"
		time.sleep(1)