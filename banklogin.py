#!/bin/env python
#_*_coding:utf-8_*_
#Author:swht
#E-mail:qingbo.song@gmail.com
#Date:2015.11.24
#Version:V0.0.1

import centerclass
import bankmanage
import main
import time
bankdict = {'ID':1018584989,'Pass':123456,'Yue':15000}
def bank_login():
	centerclass.bank.Print()
	flag = 0
	while flag <= 3:
		creditId = raw_input("请输入你的信用卡号 :").strip()
		creditPass = raw_input(u"请输入你的信用卡密码:").strip()
		#判断输入的字符串是否为纯数字
		if creditId.isdigit():
			ifBankId(creditId,creditPass,flag)
		else:
			print "你输入的信用卡号类型不正确,请重新输入!"
			flag += 1
	print "你输入的错误次数已达3次,程序将退出!"
	main.welcome()
def ifBankId(creditId,creditPass,flag):
	if bankdict['ID'] == int(creditId):
		if bankdict['Pass'] == int(creditPass):
			LoginBankSucess(creditId)
		else:
			# if userId == 'quit':
			# print "系统即将退出!"
			# time.sleep(1)
			# main.welcome()
			# else:
			# 	flag += 1
			# 	print "你输入的密码有误,请重新输入!"
			flag += 1
			print "你输入的密码有误,请重新输入!"
	else:
		flag += 1
		print "你输入的信用卡号有误,请重新输入!"

def LoginBankSucess(creditId):
	flag = 0
	while flag <= 5:
		print '''
\t=========欢迎用户%s登录到信用卡中心=========
\t\t1.取现\t\t2.查询\t\t
\t\t3.还款\t\t4.转账\t\t
\t\t5.购物\t\t6.退出\t\t
''' % creditId
		choicebank = raw_input('''请选择指令:''').strip()
		if len(choicebank) == 0:
			flag += 1
			print "指令不能为空,请重新输入![1-6]"
		else:
			choicebank = int(choicebank)
			if choicebank >= 1 and choicebank <= 6:
				if choicebank == 1:
					bankmanage.draw()
				if choicebank == 2:
					bankmanage.check()
				if choicebank == 3:
					bankmanage.repayment()
				if choicebank == 4: 
					bankmanage.transfer()
				if choicebank == 5:
					bankmanage.shoppay()
				if choicebank == 6:
					print '程序即将退出信用卡中心,欢迎下次使用!'
					time.sleep(1)
					main.welcome()
			else:
				flag += 1
				print "你输入的指令不在规定范围内,请重新输入![1-6]"		
	print "你输入的错误次数已达5次!系统将退出!"
	time.sleep(1)
	bank_login()