# -*- coding: utf-8 -*-
'''
Python 3.x
Mr.BelieVe Created on 2019年11月25日
描述：模拟系统运行银行家算法
@author: Mr.BelieVe
@link: mrbelieve128.github.io
'''
import numpy as np
import os
import time
class Process:
    def __init__(self, ANum=0, BNum=0, CNum=0):
        self.Max = {'A': ANum, 'B': BNum, 'C': CNum}
        self.Need = {'A': ANum, 'B': BNum, 'C': CNum}
        self.Allocation = {'A': 0, 'B': 0, 'C': 0}
        

    def Allocate(self, ANum, BNum, CNum):
        self.Allocation['A'] = ANum
        self.Allocation['B'] = BNum
        self.Allocation['C'] = CNum
        self.Need['A'] = self.Need['A'] - ANum
        self.Need['B'] = self.Need['B'] - BNum
        self.Need['C'] = self.Need['C'] - CNum
    def DisAllocate(self, ANum, BNum, CNum):
        self.Allocation['A'] = int(self.Allocation['A']) - ANum
        self.Allocation['B'] = int(self.Allocation['B']) - BNum
        self.Allocation['C'] = int(self.Allocation['C']) - CNum
        self.Need['A'] = self.Need['A'] + ANum
        self.Need['B'] = self.Need['B'] + BNum
        self.Need['C'] = self.Need['C'] + CNum


class System:
    def __init__(self):
        self.Process = []
        self.ProcessNum = -1
        self.ProcessArray = np.array(['  '])
        self.Available = np.array(['A', 'B', 'C'])
        # self.Available = {'A': 100, 'B': 100, 'C': 100} #可利用资源
        self.Max = np.array(['A', 'B', 'C'])  # 各进程最大需求
        self.Allocation = np.array(['A', 'B', 'C'])  # 分配给各进程数量
        self.Need = np.array(['A', 'B', 'C'])  # 需求

    def init_Available(self, ANum=0, BNum=0, CNum=0):
        _ = np.array([ANum, BNum, CNum])
        self.Available = np.vstack((self.Available, _))

    def init_Process(self, ANum=0, BNum=0, CNum=0):
        _ = np.array([ANum, BNum, CNum])
        self.Max = np.vstack((self.Max, _))  # 初始化Max矩阵相连
        self.Need = np.vstack((self.Need, _))  # 初始化Need
        _ = np.array([0, 0, 0])
        self.Allocation = np.vstack((self.Allocation, _))  # 初始化Allocation
        _ = np.array(['P' + str(self.ProcessNum)])
        self.ProcessArray = np.vstack((self.ProcessArray, _))

    def AddProcess(self, ANum=0, BNum=0, CNum=0):
        self.ProcessNum += 1
        _ = Process(ANum, BNum, CNum)
        self.Process.append(_)
        self.init_Process(ANum, BNum, CNum)

    def Allocate(self, ProcessNum, ANum, BNum, CNum):  # 设置分配并且在Need中减去
        self.Allocation[ProcessNum+1][0] = int(self.Allocation[ProcessNum+1][0]) + ANum
        self.Allocation[ProcessNum+1][1] = int(self.Allocation[ProcessNum+1][1]) + BNum
        self.Allocation[ProcessNum+1][2] = int(self.Allocation[ProcessNum+1][2]) + CNum
        self.Need[ProcessNum+1][0] = int(self.Need[ProcessNum+1][0]) - ANum
        self.Need[ProcessNum+1][1] = int(self.Need[ProcessNum+1][1]) - BNum
        self.Need[ProcessNum+1][2] = int(self.Need[ProcessNum+1][2]) - CNum
        self.Process[ProcessNum].Allocate(ANum, BNum, CNum) #分配进进程的数据中
    def DisAllocate(self, ProcessNum, ANum, BNum, CNum):
        self.Allocation[ProcessNum+1][0] = int(self.Allocation[ProcessNum+1][0]) - ANum
        self.Allocation[ProcessNum+1][1] = int(self.Allocation[ProcessNum+1][1]) - BNum
        self.Allocation[ProcessNum+1][2] = int(self.Allocation[ProcessNum+1][2]) - CNum
        self.Need[ProcessNum+1][0] = int(self.Need[ProcessNum+1][0]) + ANum
        self.Need[ProcessNum+1][1] = int(self.Need[ProcessNum+1][1]) + BNum
        self.Need[ProcessNum+1][2] = int(self.Need[ProcessNum+1][2]) + CNum
        self.Process[ProcessNum].DisAllocate(ANum, BNum, CNum) #进程的数据中加回
   
    def PrintAva(self):
        print('|  Available |')
        print(self.Available)

    def PrintAll(self):
        _ = np.hstack((self.ProcessArray, self.Max))
        _ = np.hstack((_, self.Allocation))
        _ = np.hstack((_, self.Need))
        print("| PNum|     Max   |Allocation |    Need   |")
        print(_)

    def AllocateCheck(self, ProcessNum, ANum, BNum, CNum):
        flag = 1
        if not int(self.Max[ProcessNum+1][0]) >= ANum:
            flag = 0
        if not int(self.Max[ProcessNum+1][1]) >= BNum:
            flag = 0
        if not int(self.Max[ProcessNum+1][2]) >= CNum:
            flag = 0
        return flag


    def Request(self, ProcessNum, ANum, BNum, CNum):
        print('进行银行家算法......')
        flag = 1
        if not (int(self.Need[ProcessNum+1][0]) >= ANum):  # 银行家算法 1
            flag = 0
        if not (int(self.Need[ProcessNum+1][1]) >= BNum):
            flag = 0
        if not (int(self.Need[ProcessNum+1][2]) >= CNum):
            flag = 0
        if flag:
            self.Allocate(ProcessNum, ANum, BNum, CNum)
            self.Available[1][0] = int(self.Available[1][0]) - ANum
            self.Available[1][1] = int(self.Available[1][1]) - BNum
            self.Available[1][2] = int(self.Available[1][2]) - CNum
            if not self.SafeCheck(ProcessNum) == (self.ProcessNum + 1):
                self.DisAllocate(ProcessNum, ANum, BNum, CNum)
                return 0
            else:
                return 1
        else:
            print()
            print("申请的大于程序所需要的！！")
            print()
            return 0 

    def SafeCheck(self,ProcessNum):
        Work = self.Available
        _ = 0
        Count = 0
        Finish = []
        for i in range(0,self.ProcessNum + 1):
            Finish.append(False)
        print('Process '+ str(ProcessNum)+ ' is done')
        Work[1][0] = int(Work[1][0]) + int(self.Allocation[ProcessNum+1][0])
        Work[1][1] = int(Work[1][1]) + int(self.Allocation[ProcessNum+1][1])
        Work[1][2] = int(Work[1][2]) + int(self.Allocation[ProcessNum+1][2])
        while Count < self.ProcessNum + 1 :         #安全性算法第二步
            for i in range(0,self.ProcessNum + 1):
                if i == ProcessNum:
                    Finish[i] = True
                    continue
                if not Finish[i]:
                    flag = 1
                    if self.Process[i].Need['A'] > int(Work[1][0]):#对应的A
                        flag = 0
                    if self.Process[i].Need['B'] > int(Work[1][1]):#对应的B
                        flag = 0
                    if self.Process[i].Need['C']> int(Work[1][2]):#对应的C
                        flag = 0
                    if flag:                    #安全性算法第三步
                        Work[1][0] = int(Work[1][0]) + int(self.Allocation[i+1][0])
                        Work[1][1] = int(Work[1][1]) + int(self.Allocation[i+1][1])
                        Work[1][2] = int(Work[1][2]) + int(self.Allocation[i+1][2])
                        Finish[i] = True
                        print('Process '+str(i)+' can be done.')
                        _ += 1
                continue
                if(_ == self.ProcessNum):
                    break   
            Count += 1
            if(_ == self.ProcessNum):
                break   
        print()
        return _ + 1

def Demo():
    Demo = System()
    print("-"*20+"Demo"+"-"*20)
    print("本系统包含三个资源，A、B、C")
    input("在回车后运行Demo")
    Demo.AddProcess(7, 5, 3)
    Demo.Allocate(0, 0, 1, 0)
    Demo.AddProcess(3, 2, 2)
    Demo.Allocate(1, 2, 0, 0)
    Demo.AddProcess(9, 0, 2)
    Demo.Allocate(2, 3, 0, 2)
    Demo.AddProcess(2, 2, 2)
    Demo.Allocate(3, 2, 1, 1)
    Demo.AddProcess(4, 3, 3)
    Demo.Allocate(4, 0, 0, 2)
    Demo.PrintAll()  # 按书上进行初始化
    Demo.init_Available(3, 3, 2)
    # Sys.PrintAll()
    print('-'*44)
    Demo.PrintAva()
    print('-'*44)
    print(("进程{} 申请A类资源{}个，B类资源{}个，C类资源{}个").format(1,1,2,2))
    print('-'*44)
    Demo.Request(1, 1, 2, 2)
    print('-'*44)
    Demo.PrintAll()
    print('-'*44)
    Demo.PrintAva()
    print('-'*44)

def main():
    Demo()
    input('                回车后进行仿真             ')
    #os.system('clear')#mac
    os.system('cls')  #win
    while 1:
        Sys = System()
        #os.system('clear')#mac
        os.system('cls')  #win  
        while 1 :
            print('-'*14 + '当前系统所有进程' + '-'*14)
            Sys.PrintAll()
            print('-'*44)
            Sys.PrintAva()   
            print('-'*44)
            print('''请输入数字选择选项：
1.创建进程  2.分配资源  3.模拟进程申请资源并进行银行家算法
4.初始化当前系统拥有资源数量    5.重新开始系统    6.退出系统''')
            try:
                Chose = int(input())
            except:
                Chose = 0
                print()
                print("ERROR:请检查输入!!")
                time.sleep(5)
                #os.system('clear')#mac
                os.system('cls')  #win 
  
            if Chose == 1:
                try:
                    ANum = int(input('请输入A资源最大所需数量：'))
                    BNum = int(input('请输入B资源最大所需数量：'))
                    CNum = int(input('请输入C资源最大所需数量：'))
                    Sys.AddProcess(ANum,BNum,CNum)
                except:
                    print()
                    print("ERROR:请检查输入!!")
                    time.sleep(5)
                    #os.system('clear')#mac
                    os.system('cls')  #win 
                    
            if Chose == 2:
                try:
                    ProcessNum = int(input('请输入进程号：'))
                    ANum = int(input('请输入A资源所分配数量：'))
                    BNum = int(input('请输入B资源所分配数量：'))
                    CNum = int(input('请输入C资源所分配数量：'))
                except:
                    print()
                    print("ERROR:请检查输入!!")
                    time.sleep(5)
                    #os.system('clear')#mac
                    os.system('cls')  #win 
                try:
                    if Sys.AllocateCheck(ProcessNum,ANum,BNum,CNum):
                        Sys.Allocate(ProcessNum,ANum,BNum,CNum)
                    else:
                        print()
                        print("ERROR:请检查输入是否大于最大所需!!")
                        time.sleep(5)
                    
                except:
                    print()
                    print("ERROR:请检查进程号是否已存在!!")
                    time.sleep(5)
                    #os.system('clear')#mac
                    os.system('cls')  #win 

            if Chose == 3:
                try:
                    ProcessNum = int(input('请输入进程号：'))
                    ANum = int(input('请输入A资源所申请数量：'))
                    BNum = int(input('请输入B资源所申请数量：'))
                    CNum = int(input('请输入C资源所申请数量：')) 
                except:
                    print()
                    print("ERROR:请检查输入!!")
                    time.sleep(5)
                    #os.system('clear')#mac
                    os.system('cls')  #win 
                try:
                    print(("进程{} 申请A类资源{}个，B类资源{}个，C类资源{}个").format(ProcessNum,ANum,BNum,CNum))
                    print('-'*44)
                    if Sys.Request(ProcessNum,ANum,BNum,CNum):
                        print("此时进程可以申请资源并且安全！！")
                        print('-'*14 + '当前系统所有进程' + '-'*14)
                        Sys.PrintAll()
                        print('-'*44)
                        Sys.PrintAva()   
                        print('-'*44)
                        input('回车后将进行重启系统')
                        break
                    else:
                        print("此时进程申请资源会导致不安全！！")
                        input('回车后将进行重启系统')
                        break
                except IndexError:
                    print()
                    print("ERROR:请检查进程号是否已存在!!")
                    time.sleep(5)
                    #os.system('clear')#mac
                    os.system('cls')  #win 
                except ValueError:
                    print()
                    print("ERROR:请检查是否有可分配资源!!")
                    Sys.DisAllocate(ProcessNum,ANum,BNum,CNum)
                    time.sleep(5)
                    #os.system('clear')#mac
                    os.system('cls')  #win 

            if Chose == 4:
                try:
                    ANum = int(input('请输入A资源目前拥有数量：'))
                    BNum = int(input('请输入B资源目前拥有数量：'))
                    CNum = int(input('请输入C资源目前拥有数量：')) 
                    Sys.init_Available(ANum,BNum,CNum)   
                except:
                    print()
                    print("ERROR:请检查输入!!")
                    time.sleep(5)
                    #os.system('clear')#mac
                    os.system('cls')  #win                  
            if Chose == 5:
                break
            if Chose == 6:
                return 
            if Chose > 6 or Chose < 1:
                print('请检查输入选择！！')
                time.sleep(5)

if __name__ == '__main__':
    main()
