import requests

from requests.packages import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

session = requests.session()

HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
				   (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}

# 第一次请求，为了Cookie(_xsrf，_zap，tgw_17)
session.get(url="https://www.zhihu.com/signin", headers=HEADERS, verify=False)
# 第二次请求，为了Cookie(q_c1，d_c0)
session.post(url="https://www.zhihu.com/udid", headers=HEADERS)
# 第三次请求，为了Cookie(capsion_ticket)
session.get(url="https://www.zhihu.com/api/v3/oauth/captcha?lang=cn", headers=HEADERS)
# 第四次请求，为了token，用于构建二维码图片的请求链接
response = session.post(url="https://www.zhihu.com/api/v3/account/api/login/qrcode", headers=HEADERS)
token = response.json().get("token")
# print(response.json())

# 第五次请求，为了二维码图片
url4QR = "https://www.zhihu.com/api/v3/account/api/login/qrcode/{0}/image".format(token)

response = session.get(url=url4QR, headers=HEADERS)
if response.status_code == 200:
	with open("qr.jpg", "wb") as file:
		file.write(response.content)
	print("【保存二维码成功】")
else:
	print("【请求二维码图片错误】")

# 阻塞程序，给予用户扫描二维码的时间
input("请随便输入后回车")

# 请求scan_info文件，并打印状态码
print(session.get("https://www.zhihu.com/api/v3/account/api/login/qrcode/{0}/scan_info".format(token), headers=HEADERS).status_code)

# 请求编辑页面
response = session.get("https://www.zhihu.com/people/edit", headers=HEADERS, allow_redirects=False)
if response.status_code == 200:
	print("登陆成功")

	print(response.text[:10000])
