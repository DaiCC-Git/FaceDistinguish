# -*- coding: utf-8 -*-
import json
import os
import tkinter.messagebox as msg

import cv2 as cv
from PIL import Image
from mttkinter import mtTkinter as tk

import Packages.ToMd5


def FaceInput(name):
    # 初始化窗口
    capture = cv.VideoCapture(0)
    model = cv.CascadeClassifier(r'./Data/Model/haarcascade_frontalface_alt2.xml')
    cv.namedWindow('Register', cv.WINDOW_AUTOSIZE)
    # 检测人脸并绘出, 保存
    while capture.isOpened():
        flag, video = capture.read()
        face = model.detectMultiScale(video)
        cv.imshow('Register', video)
        cv.waitKey(10)
        for x, y, w, h in face:
            cv.imwrite('./Temp/face.jpg', video)
            tmp_image = Image.open('./Temp/face.jpg')
            tmp_image.crop((x, y, x + w, y + h)).save(f'./Data/UserData/Image/{name}.jpg')
            cv.destroyAllWindows()
            os.remove('./Temp/face.jpg')
            capture.release()
            return True


class Register:

    def __init__(self):
        super().__init__()
        self.registerUi = tk.Tk()
        self.nameLabel = tk.Label()
        self.phoneLabel = tk.Label()
        self.emailLabel = tk.Label()
        self.passwordLabel = tk.Label()
        self.nameInput = tk.Text()
        self.phoneInput = tk.Text()
        self.emailInput = tk.Text()
        self.passwordInput = tk.Text()
        self.registerButton = tk.Button()

    def register(self):
        name = self.nameInput.get('0.0', 'end')
        phone = self.phoneInput.get('0.0', 'end')
        email = self.emailInput.get('0.0', 'end')
        password = self.passwordInput.get('0.0', 'end')
        proceed = 1
        # 检测是否合格
        if '@' not in email:
            msg.showerror('错误 Error', '邮箱地址错误,请重试\nYour email address was wrong. Please check it and try again')
            proceed = 0
        if len(password) < 8 and not password.isdigit():
            msg.showerror('错误 Error', '密码过于简单\nYour password is too simple')
            proceed = 0
        if not FaceInput(name.replace('\n', '')):
            msg.showerror('错误 Error', '人脸识别失败\nFace recognition failed')
            proceed = 0

        if proceed == 1:
            # 合成列表
            with open('./Data/UserData/Info/User.json', 'r') as jsonFile:
                data = json.load(jsonFile)
            data[email.replace('\n', '')] = [phone.replace('\n', ''),
                                             name.replace('\n', ''),
                                             Packages.ToMd5.ToMd5(password.replace('\n', ''))]
            with open('./Data/UserData/Info/User.json', 'w') as jsonFile:
                json.dump(data, jsonFile)  # 写入Json文件
            self.registerUi.quit()

    def RegisterUi(self):
        """
        窗口设计:
            1.姓名
            2.手机
            3.邮箱
            4.密码
            5.注册按钮
        """
        # 设置窗口
        self.registerUi.title('注册 Register')
        self.registerUi.geometry('256x320')

        # 姓名框
        self.nameLabel = tk.Label(self.registerUi, text='姓名  Name')
        self.nameInput = tk.Text(self.registerUi, width=20, height=1)
        self.nameLabel.pack()
        self.nameInput.pack()

        # 手机框
        self.phoneLabel = tk.Label(self.registerUi, text='手机  Phone Number')
        self.phoneInput = tk.Text(self.registerUi, width=20, height=1)
        self.phoneLabel.pack()
        self.phoneInput.pack()

        # 邮箱框
        self.emailLabel = tk.Label(self.registerUi, text='邮箱  E-mail Address')
        self.emailInput = tk.Text(self.registerUi, width=20, height=1)
        self.emailLabel.pack()
        self.emailInput.pack()

        # 密码框
        self.passwordLabel = tk.Label(self.registerUi, text='密码  Password')
        self.passwordInput = tk.Text(self.registerUi, width=20, height=1)
        self.passwordLabel.pack()
        self.passwordInput.pack()

        # 注册按钮
        self.registerButton = tk.Button(self.registerUi, text='注册\nregister', command=self.register)
        self.registerButton.pack()

        self.registerUi.mainloop()


if __name__ == '__main__':
    Register().RegisterUi()
