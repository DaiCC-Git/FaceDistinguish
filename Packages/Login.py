# -*- coding: utf-8 -*-
import json
import Packages.ToMd5
import cv2 as cv
from mttkinter import mtTkinter as tk
from PIL import Image
import tkinter.messagebox as msg
import os
import time


def AddName(name):
    """
    读写Json
    """
    with open('./Data/Visitor.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    time_now = time.strftime('%Y-%m-%d.%H:M:%S', time.localtime())
    date = time.strftime('%Y-%m-%d')
    data[date].append([name, time_now])
    with open('./Data/Visitor.json', 'w') as jsonFile:
        json.dump(data, jsonFile)


class Login:
    """
    设计要求:
        1.opencv人脸识别
        2.无法登录时
            1.注册
            2.密码登录
                1.重名 -> 使用邮箱登录
    """

    def __init__(self):
        super().__init__()
        # 人脸识别部分
        cv.namedWindow('Login', cv.WINDOW_AUTOSIZE)
        self.model = cv.CascadeClassifier(r'./Data/Model/haarcascade_frontalface_alt2.xml')
        self.capture = cv.VideoCapture(0)
        self.flag = self.video = None
        self.faceList = None
        self.facePath = f''
        self.allFace = self.userFace = None

        # 登陆部分
        self.loginUi = tk.Tk()
        self.emailLabel = tk.Label()
        self.emailInput = tk.Text()
        self.passwordLabel = tk.Label()
        self.passwordInput = tk.Text()
        self.nextButton = tk.Button()

    def FindFace(self):
        self.faceList = os.listdir('./Data/UserData/Image')
        proceed = True
        for face in self.faceList:
            self.facePath = f'./Data/UserData/Image/{face}'
            self.allFace = cv.imread(self.facePath)
            self.userFace = cv.imread(r'./Temp/Login.jpg')
            res = cv.minMaxLoc(cv.matchTemplate(self.userFace, self.allFace, cv.TM_CCORR_NORMED))[0]
            if res >= 0.9:
                if proceed:
                    name = face.replace('\n', '')
                    msg.showinfo("欢迎 Welcome", f"欢迎{name}!\nWelcome! {name}")
                    AddName(name)
                    os.remove('./Temp/Login.jpg')
                    proceed = False
                else:
                    os.remove('./Temp/Login.jpg')
        if proceed:
            msg.showerror('错误 Error', '错误，未找到人脸.\nError, face not found')
            mess = msg.askyesno('是否继续', '是否使用其他方式?\nDo you use other methods?')
            if mess == 'yes':
                self.LoginUi()

    def FaceDistinguish(self):
        while self.capture.isOpened():
            self.flag, self.video = self.capture.read()
            cv.imshow('Login', self.video)
            face = self.model.detectMultiScale(self.video)
            cv.waitKey(10)
            for x, y, w, h in face:
                cv.imwrite('./Temp/Login.jpg', self.video)
                img = Image.open('./Temp/Login.jpg')
                img.crop((x, y, x + w, y + h)).save('./Temp/Login.jpg')
                self.capture.release()
                cv.destroyAllWindows()
                self.FindFace()
                break

    def Check(self):
        with open('./Data/UserData/Info/User.json', 'r') as jsonFile:
            data = json.load(jsonFile)
        success = 0
        for userEmail in data:
            if userEmail == self.emailInput.get('0.0', 'end'):
                success = 1
                name = userEmail[1]
                if userEmail[2] == Packages.ToMd5.ToMd5(self.passwordInput.get('0.0', 'end')):
                    AddName(name)
                    msg.showinfo('登录成功 Success', '登录成功\nSuccess')
                else:
                    msg.showerror('错误 Error', '密码错误, 请重试\nPassword error, please try again')
        if success == 0:
            msg.showerror('错误 Error', '未找到该用户\nThe user was not found')

    def LoginUi(self):
        self.loginUi.title('登录 Login')
        self.loginUi.geometry('320x240')
        # 邮箱
        self.emailLabel = tk.Label(self.LoginUi(), text='邮箱\tE-mail address')
        self.emailLabel.pack()
        self.emailInput = tk.Text(self.LoginUi())
        self.emailInput.pack()
        # 密码
        self.passwordLabel = tk.Label(self.LoginUi(), text='密码\tPassword')
        self.passwordLabel.pack()
        self.passwordInput = tk.Text(self.LoginUi())
        self.passwordInput.pack()
        # 确认
        self.nextButton = tk.Button(self.LoginUi(), text='确认')
        self.nextButton.pack()

        self.Check()  # 检查是否正确,正确将放行
        self.loginUi.mainloop()


if __name__ == '__main__':
    Login().FaceDistinguish()
