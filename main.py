# -*- coding: utf-8 -*-
# @Version : Python3.6
# @Time    : 2018/8/13 8:55
# @Author  : Guan                  
# @File    : main.py                   
# @SoftWare: PyCharm

"""
用法示例
"""

import requests

from http import cookiejar
from zhihu_login import login as zhihu_login

HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
				   (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}


def main():

    result = zhihu_login()

    session = requests.session()
    session.cookies = cookiejar.LWPCookieJar("./zhihu/cookies")
    # print(result)
    if result:
        session.cookies.load(ignore_discard=True)
        # https://www.zhihu.com/topic 也是一个登陆后才能访问的网页
        response = session.get(url="https://www.zhihu.com/topic", headers=HEADERS)
        print(response.text)


if __name__ == "__main__":
    main()