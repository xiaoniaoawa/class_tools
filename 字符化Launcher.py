"""
警告！
屎山代码，看之前请控制好血压！
如感觉不适，请立即停止浏览本文件！
"""
#导入模块+初始化变量/标题
import random
#! /usr/bin/env python
#coding=utf-8
import os
from os import system
import time


#修改标题
system("title 课堂工具箱")
#初始化几个变量
writeboardtxt = None
title = '课堂工具箱'
#提前读取随机学号的最大值
txtr = open('RInfo.txt','r')
read_ran_info0 = txtr.read
txtr.close()
#转换随机学号最大值变量的类型
print(read_ran_info0)
"""
read_ran_info = float(read_ran_info)
read_ran_info = int(read_ran_info)
#读取版本文件
verConfigOpen = open('verInfo.txt','r')
verConfig=verConfigOpen.read()
verConfigOpen.close()
#---开始执行主要代码
print('Loading...')
#清屏
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
#显示欢迎句
print('欢迎使用课堂工具箱'+verConfig)
#显示提示
print('第一次使用随机学号功能前请先输入info配置最大值\n')
#开始循环执行主代码
while True:
    system("title 课堂工具箱/主页")
    print('可用命令: \n ran---随机选学号 \n info---设置 \n wb---记事本 \n exit---退出')
    inp = input('>>')#要求输入
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    if inp == 'ran':#随机学号
        system("title 课堂工具箱/随机学号已完成")
        ranNUM1=random.randint(1,read_ran_info+1)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('随机学号的值是：'+str(ranNUM1))
        time.sleep(0.1)
        pass
    elif inp == 'exit':#退出
        system("title 课堂工具箱/退出/按任意键关闭")
        print('正在关闭...')
        print('正在完成...')
        os.system('pause')
        break
    elif inp == 'info':
        system("title 课堂工具箱/设置")
        ranINFO = input('请配置随机选学号的最大值：')
        txt = open('RInfo.txt','w')
        txt.write(ranINFO)
        txt.close()
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    elif inp == 'wb':
        system("title 课堂工具箱/记事本")
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        wfliename = input('请输入文件名，若无则创建，已自动创建文件后缀(.txt)')
        writetxt = open('writeboard创建的文本文档'+ '/' + wfliename +'.txt','a')
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('Tips:因为是测试版，暂时不做readline读取以前写入的内容，3.0会加。')
        print('本版本仅供测试，修改/删除已写的行内容暂时无法实现！若要修改，请使用电脑自带的“记事本(Notepad)”进行修改。\n本版本暂时只支持下一行和写本行 \n\n欢迎使用课堂工具箱，当前路径为/writeboard/'+'wfliename')
        print('使用"save()"保存并退出')
        system("title 课堂工具箱/记事本/"+wfliename+'.txt')
        while True:
            writes=input()
            if writes == 'save()':
                writetxt.close()
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                break
            writeboardtxt = writetxt.write(writes + '\n')

                


"""