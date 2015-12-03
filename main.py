#!/bin/env python
#_*_coding:utf-8_*_
#Author:swht
#E-mail:qingbo.song@gmail.com
#Date:2015.11.24
#Version:V0.0.1

'''
	网站入口
'''
import shoplogin
import banklogin
import time
import sys

def welcome():
	flag = 0
	while flag < 5:
		userInput = raw_input('''
	\t\t\t欢迎光临"南非波波小屋"\t\t\t 
	在这里你可以购买二手数码产品，还可以进入信用卡交易中心进行相应操作！
	请选择相应的指令进入不同的界面！
	\t二手数码产品:1\t信用卡中心:2\t退出:3\t
	请输入你要进入的界面指令[1-3]:''').strip()
		if userInput.isdigit():
			if int(userInput) == 1:
				shoplogin.shop_login()
			if int(userInput) == 2:
				banklogin.bank_login()
			if int(userInput) == 3:
				print "系统即将退出,欢迎下次光临!"
				time.sleep(1)
				sys.exit()
			if int(userInput) != 1 and int(userInput) != 2 and int(userInput) != 3:
				print "你输入的指令数字已超出范围!请输入正确的指令[1-3].."
				flag += 1
		else:
			print "系统只接受数字类型指令,请输入正确的指令[1-3]!"
			flag += 1
	print "你输入的错误次数已达5次,程序即将退出!感谢你的使用!"
	time.sleep(1)
	sys.exit(1)


if __name__ == '__main__':
	welcome()