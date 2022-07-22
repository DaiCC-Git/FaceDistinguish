## 项目用途
<ol>
    <li>人脸识别打卡</li>
    <li>疫情防控</li>
</ol>

***
## 迭代版本
<ol>
    <li>2022/7/21 发起项目</li>
    <li>2022/7/22 更新项目, 发布Version 1.0</li>
</ol>

***
## 项目目录
    Face
    │  Main.py  # 主文件
    │  READMR.md
    │
    ├─Data  # 所有数据
    │  │  Visitor.json  # 访问数据库
    │  │
    │  ├─Model  #人脸识别模型
    │  │      haarcascade_eye.xml
    │  │      haarcascade_eye_tree_eyeglasses.xml
    │  │      haarcascade_frontalcatface.xml
    │  │      haarcascade_frontalcatface_extended.xml
    │  │      haarcascade_frontalface_alt.xml
    │  │      haarcascade_frontalface_alt2.xml
    │  │      haarcascade_frontalface_alt_tree.xml
    │  │      haarcascade_frontalface_default.xml
    │  │      haarcascade_fullbody.xml
    │  │      haarcascade_lefteye_2splits.xml
    │  │      haarcascade_licence_plate_rus_16stages.xml
    │  │      haarcascade_lowerbody.xml
    │  │      haarcascade_profileface.xml
    │  │      haarcascade_righteye_2splits.xml
    │  │      haarcascade_russian_plate_number.xml
    │  │      haarcascade_smile.xml
    │  │      haarcascade_upperbody.xml
    │  │
    │  └─UserData   #用户数据库
    │      ├─Image  # 用户人脸
    │      │      Admin.jpg
    │      │
    │      └─Info   #用户信息
    │              User.json
    │
    ├─Packages  # 支持库
    │  │  Login.py
    │  │  Register.py
    │  └─ ToMd5.py
    │
    └─Temp  # 缓存目录
            Temp.tmp

***
## 未来目标
<ol>
    <li>自主训练模型</li>
    <li>优化代码</li>
</ol>

***
***
<a src="http://daicc.freehost.cc">DaiCC的网站</a>