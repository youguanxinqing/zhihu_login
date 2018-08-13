import requests

headers = {
	
	'Cookie': 'tgw_l7_route=8605c5a961285724a313ad9c1bbbc186; _zap=bde65003-27f5-4499-b9d5-3fc0285aa8fe; _xsrf=3885b220-95d4-439b-a414-5814e49e9140; q_c1=9745e17900094bc992b0a25416e39dab|1534081576000|1534081576000; d_c0="AMClbnasCw6PTs-Zv-IVDpi10YouMUFWQjY=|1534081576"',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
}

response = requests.get(url="https://www.zhihu.com/api/v3/oauth/captcha?lang=cn", headers=headers)

print(response.status_code)
print(response.text)