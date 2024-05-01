#coding=utf-8
#encoding=utf-8
#decoding=utf-8

"""
警告！
米 |
共 山 代 码，看之前请控制好血压！
如感觉不适，请立即停止使用本文件！
"""
#导入模块+初始化变量/标题
import random
import os
from os import system
import time
# from playsound import playsound
title = 'ClassTool/pre system...'
clock = 0




#创建随机小标题函数
def ptitle():
    titleword = open('Title.txt','r')
    a = random.choice(titleword.readlines())
    print(a)
    titleword.close()
#创建打印图标的函数
def logo():
    logo = open('logo.txt','r')
    logoop = logo.readlines()
    for i in logoop:
        i = i.strip('\n')
        print(i)
#创建写日志函数
nowtime = time.ctime()
nowtime = str(nowtime)
log=open('log.txt','a')
log.write("\nlog from "+nowtime+"\n")
log.close()
def wlog(ltype = 'output', loginp = 'HelloWorld'):
    log=open('log.txt','a')
    nowtime = time.ctime()
    nowtime = str(nowtime)
    nowtime = '[' + nowtime + ']'
    log.write(nowtime + "[" + ltype + "]" + ' ' + loginp)
    log.write('\n')
    log.close()
wlog()
#修改标题
system("title 课堂工具箱")
#初始化几个变量
wlog('output','start_reset_variable')
writeboardtxt = None
title = '课堂工具箱'
wlog('output','end_reset_variable')
#读取版本文件
verConfigOpen = open('verInfo.txt','r')
verConfig=verConfigOpen.read()
verConfigOpen.close()
wlog(loginp='read_verConfig_end')
#获取随机学号的最大值
txtr = open('RInfo.txt','r')
read_ran_info = txtr.read()
txtr.close()
wlog(loginp='read_numid_finish')
#转换随机学号最大值变量的类型
read_ran_info = int(read_ran_info)
wlog(loginp='int_numid_finish')
#开始执行主要代码
wlog(loginp='launching ClassToolBox...')
#初始化清屏
def clns():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    wlog(loginp='cleared screen')
#清屏
clns()
#显示欢迎句
#logo()
print('\n')
print('欢迎使用课堂工具箱'+verConfig)
wlog(loginp='printed Hello')
#开始循环执行主代码
while True:
    logo()
    #读取OOBE状态
    OOBEOpen = open('OOBE.txt','r')
    OOBEConfig = OOBEOpen.read()
    OOBEConfig = int(OOBEConfig)
    OOBEOpen.close()
    #改掉系统的默认标题
    system("title 课堂工具箱/主页")
    #判断是否完成OOBE
    if OOBEConfig == 0:
        #否就隐藏随机学号功能
        cpr = open('Copyright.txt','r')
        cprprint = cpr.read()
        str(cprprint)
        print(cprprint)
        print('第一次使用随机学号功能前请先输入info配置最大值\n')
        cpr.close()
        print('是否同意该文本? \n YES === 我同意,继续 \n 其他文本 === 不同意,退出程序')
        if input() == 'YES':
            clns()
            logo()
            time.sleep(2)
            clns()
            print('可用命令： \n info---进行开箱体验 \n exit---退出')
            wlog(loginp='hide random_id,show oobe menu')
        else:
            break
    else:
        ptitle()
        print('可用命令:  \n ran---随机选学号 \n clock---倒计时 \n info---重新启动开箱体验 \n exit---退出')
        wlog(loginp='show random_id,hide oobe menu')
    inp = input('>>')#要求输入
    wlog(loginp='inputting num...')
    clns()
    if inp == 'ran':#随机学号
        system("title 课堂工具箱/随机学号已完成")
        ranNUM1=random.randint(1,read_ran_info+1)
        clns()
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
        print('你好')
        time.sleep(3)
        clns()
        print('我们很高兴见到您！')
        time.sleep(3)
        clns()
        print('当您看到此文本时')
        time.sleep(3)
        clns()
        print('好东西就要来了!')
        time.sleep(3)
        clns()
        print('我们为了您的课程')
        time.sleep(1)
        clns()
        print('下费苦心！')
        print('那么，先去配置随机学号的最大值吧！')
        time.sleep(5)
        clns()
        ranINFO = input('请配置随机选学号的最大值：')
        txt = open('RInfo.txt','w')
        txt.write(ranINFO)
        txt.close()
        OOBEOpen=open('OOBE.txt','w')
        OOBEOpen.write('1')
        OOBEOpen.close()
        clns()
        txtr = open('RInfo.txt','r')
        read_ran_info = txtr.read()
        txtr.close()
        wlog(loginp='read_numid_finish')
        read_ran_info = int(read_ran_info)
        wlog(loginp='int_numid_finish')
        clns()
        print('千门万户曈曈日，总把新桃换旧符。\n我们将会持续更新软件，为您的课程变得更充实！')
        time.sleep(3)
        clns()
        print('尽情使用吧！')
        time.sleep(3)
        clns()
    elif inp == 'clock':
        print('请输入分钟数,小于1填0')
        minute = input()
        minute = int(minute)
        print('请输入秒数')
        second = input()
        second = int(second)
        clock = minute*60 + second
        print('输入start并按ENTER开始，输入其他无效')
        if input() == 'start':
            for i in range(0,clock):
                if second != 0:
                    print(str(minute) + ':' + str(second))
                    second = second - 1
                    time.sleep(1)
                else:
                    second = 60
                    minute = minute - 1
                if minute == 0 and second == 0:
                    print('计时结束啦!')
                    os.system('music1.wav')
        """
        if input() == 'start':
            clock = int(clock)
            for i in range(0,clock):
                time.sleep(1)
                clock = clock-1
                print(clock)
    else:
        print('命令错误-请检查输入的内容是否正确')
        """