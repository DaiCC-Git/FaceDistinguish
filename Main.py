# -*- coding: utf-8 -*-
"""
人脸识别系统
DaiCC
发起时间: 2022/7/21
结束时间: 2022/7/22
"""
import json
import threading as thr
import time

# 导入包
from mttkinter import mtTkinter as tk

# 导入文件
import Packages.Login as login
import Packages.Register as register


def Login():
    login.Login().FaceDistinguish()


def Register():
    register.Register().RegisterUi()


def ReadJsonFile():
    with open('./Data/Visitor.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    return data


def WriteJsonFile(data):
    with open('./Data/Visitor.json', 'w') as jsonFile:
        json.dump(data, jsonFile)


class Main:

    def __init__(self):
        super().__init__()
        self.mainUi = tk.Tk()
        self.welcomeLabel = tk.Label()
        self.timeLabel = tk.Label()
        self.visitor_num = tk.Label()
        self.loginButton = tk.Button()
        self.registerButton = tk.Button()
        self.haveDate = False
        self.date = None
        self.data = {}

    def Update(self):
        self.timeLabel.config(text=time.ctime())  # 更新时间

        self.date = time.strftime('%Y-%m-%d', time.localtime())
        self.data = ReadJsonFile()
        try:
            self.visitor_num.config(text='今日访问人数: {0}'.format(len(self.data[self.date])))  # 更新访问人数
        except KeyError:
            for day in self.data:  # 检测是否有今日日期
                if self.date in day:
                    self.haveDate = True
            if not self.haveDate:  # 将日期添加到Json文件
                self.data[self.date] = []
                WriteJsonFile(self.data)
        timer = thr.Timer(1, self.Update)
        timer.start()

    def MainUi(self):
        """
        主界面UI
        功能:
            1.Label欢迎标签
            2.Label显示时间
            3.Label显示当天登陆人数
            4.Button登录按键
            5.Button注册按键
        """
        # 设置窗口
        self.mainUi.geometry('640x480')  # 设置大小
        self.mainUi.title('人脸识别系统')  # 设置标题

        # 设置欢迎标签
        self.welcomeLabel = tk.Label(self.mainUi, text='Welcome!\t欢迎!',
                                     anchor='n',
                                     font=('', 32))
        self.welcomeLabel.pack()

        # 设置时间
        self.timeLabel = tk.Label(self.mainUi, text=time.ctime(), font=('', 32))
        self.timeLabel.pack(padx=0, pady=100)
        self.Update()

        # 设置当天登陆人数
        self.visitor_num = tk.Label(self.mainUi,
                                    text='今日访问人数: {0}'.format(len(self.data[self.date])),
                                    font=('', 20))
        self.visitor_num.pack()

        # 设置登录按键
        self.loginButton = tk.Button(self.mainUi, text='登录\nLogin', command=Login, width=50)
        self.loginButton.pack()

        # 设置注册按键
        self.registerButton = tk.Button(self.mainUi, text='注册\nRegister', command=Register, width=50)
        self.registerButton.pack()

        self.mainUi.mainloop()  # 显示并循环


if __name__ == '__main__':
    Main().MainUi()
