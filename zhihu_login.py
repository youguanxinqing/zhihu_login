# -*- coding: utf-8 -*-
# @Version : Python3.6
# @Time    : 2018/8/13 8:55
# @Author  : Guan
# @File    : main.py
# @SoftWare: PyCharm

import os
import requests

from http import cookiejar
from urllib import error
from PIL import Image
from requests.packages import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning



HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}

# 关闭InsecureRequestWarning 警告
urllib3.disable_warnings(InsecureRequestWarning)

# 设置全局变量
session = None
token = ""

def init():
    """
    初始化
    1. 创建zhihu文件
    2. 加载本地cookies
    :return:
    """

    # 如果不存在目录【zhihu】，则创建
    filename = "zhihu"
    filepath = "{0}/{1}".format(os.path.abspath(os.path.dirname(__file__)), filename)
    if not os.path.exists(filepath):
        os.mkdir(filename)

    # 实例化session对象，用于维持会话
    global session
    session = requests.session()

    # 实例化LWPCookieJar对象，用于存储、读取本地cookies
    session.cookies = cookiejar.LWPCookieJar("./zhihu/cookies")
    # 尝试加载本地cookies，存在返回True，否返回False
    try:
        session.cookies.load(ignore_discard=True)
        return True
    except FileNotFoundError:
        return False

def test_login():
    """
    测试是否登陆状态
    :return:
    """

    # 请求编辑页面
    response = session.get("https://www.zhihu.com/people/edit", headers=HEADERS, allow_redirects=False)
    if response.status_code == 200:
        # print(response.text[:10000])
        return True
    else:
        return False

def request_qrcode():
    """
    请求二维码
    :return:
    """

    try:
        # 第一次请求，为了Cookie(_xsrf，_zap，tgw_17)
        session.get(url="https://www.zhihu.com/signin", headers=HEADERS, verify=False)
        # 第二次请求，为了Cookie(q_c1，d_c0)
        session.post(url="https://www.zhihu.com/udid", headers=HEADERS)
        # 第三次请求，为了Cookie(capsion_ticket)
        session.get(url="https://www.zhihu.com/api/v3/oauth/captcha?lang=cn", headers=HEADERS)
        # 第四次请求，为了token，用于构建二维码图片的请求链接
        response = session.post(url="https://www.zhihu.com/api/v3/account/api/login/qrcode", headers=HEADERS)
        global token
        token = response.json().get("token")
        # print(response.json())

        # 第五次请求，为了二维码图片
        url4QR = "https://www.zhihu.com/api/v3/account/api/login/qrcode/{0}/image".format(token)

        response = session.get(url=url4QR, headers=HEADERS)
        if response.status_code == 200:
            with open("./zhihu/qr.jpg", "wb") as file:
                file.write(response.content)
            print("【保存二维码成功】")
        else:
            print("【请求二维码图片错误】")

    except error.HTTPError:
        print("【请求二维码过程中，出现HTTP错误】")

def show_qr():
    """
    自动显示二维码图片
    :return:
    """

    # 尝试自动打开二维码
    try:
        img = Image.open("./zhihu/qr.jpg")
        
    except FileNotFoundError:
        print("【没有二维码图片】")
    except Exception:
        print("【打开二维码图片出错】")
    
    else:
        # show()操作后，会阻塞程序，直到关闭图片才往后执行
        print("【请扫描二维码】")
        img.show()
        # 第六次请求，为了Cookie(z_c0)
        response = session.get("https://www.zhihu.com/api/v3/account/api/login/qrcode/{0}/scan_info".format(token), headers=HEADERS)

def login():
    """
    负责控制程序的逻辑
    :return:
    """

    # 如果存在本地cookies，尝试用此访问
    if init():
        result = test_login()
        if result:
            print("【在登陆状态】")
            return True
        else:
            print("【cookies已过期，重新登陆】")

    else:
        while True:

            request_qrcode()
            show_qr()

            if test_login():
                print("【登陆成功】")

                # 登陆成功，将cookies本地保存
                session.cookies.save()
                return True

            else:
                print("【登陆失败，正在重新登陆】")


if __name__ == "__main__":
    login()
