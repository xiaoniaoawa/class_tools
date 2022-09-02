"""
警告！
屎山代码，看之前请控制好血压！
如感觉不适，请立即停止观看本文件！






























"""
import random
#------------------
print('欢迎使用课堂工具箱1.0')
print('第一次使用随机学号功能前请先输入info配置最大值!\n 没配置导致的报错我不管!!!')
while True:
    print('可用命令: \n ran---随机选学号 \n exit---退出 \n info---设置')
    inp = input('>>')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    if inp == 'ran':
        txtr = open('RInfo.txt','r')
        read_ran_info = txtr.readline(2)
        txtr.close()
        read_ran_info = int(read_ran_info)
        ranNUM1=random.randint(1,read_ran_info+1)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('随机学号的值是：'+str(ranNUM1))
        pass
    elif inp == 'exit':
        break
    elif inp == 'info':
        ranINFO = input('请配置随机选学号的最大值：')
        txt = open('RInfo.txt','w')
        txt.write(ranINFO)
        txt.close()
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        