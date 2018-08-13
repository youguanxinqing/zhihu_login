import requests

headers = {
	
	'accept': 'application/json, text/plain, */*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Content-Length': '0',
	'Cookie': '_zap=bde65003-27f5-4499-b9d5-3fc0285aa8fe; _xsrf=3885b220-95d4-439b-a414-5814e49e9140; q_c1=9745e17900094bc992b0a25416e39dab|1534081576000|1534081576000; d_c0="AMClbnasCw6PTs-Zv-IVDpi10YouMUFWQjY=|1534081576"; capsion_ticket="2|1:0|10:1534081576|14:capsion_ticket|44:NmZkNmMyMDI5NjA0NDBlMWE5OWQyODg3NzlmOTFlNzY=|850d97264df225120a28c66b0252ddd9659f5f9e344c45d0a47046766f23d271"; tgw_l7_route=61066e97b5b7b3b0daad1bff47134a22',
	'Host': 'www.zhihu.com',
	'Origin': 'https://www.zhihu.com',
	'Referer': 'https://www.zhihu.com/signin',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
	'x-ab-param': 'top_gr_model=0;se_gi=0;top_adpar=0;top_gif=0;top_hqt=0;top_mlt_model=0;top_root_web=0;top_sj=2;top_universalebook=1;top_uit=0;top_free_content=-1;top_gr_auto_model=0;top_sjre=0;top_video_fix_position=0;ls_play_continuous_order=1;top_follow_reason=0;top_nmt=0;top_ntr=1;se_tf=1;top_nuc=0;top_dtmt=0;top_root_ac=-1;top_tag_isolation=0;top_tmt=0;top_billupdate1=0;top_root_few_topic=0;top_root_mg=1;top_tffrt=0;top_vdio_rew=0;top_an=0;top_nad=1;top_retag=0;top_billab=0;top_hca=0;top_is_gr=0;top_yhgc=0;top_billpic=0;top_nid=0;top_user_gift=0;top_feedre=1;top_nszt=0;top_root=0;top_yc=0;top_memberfree=1;top_recall=1;top_30=0;top_bill=0;top_nucc=0;pin_efs=orig;top_alt=0;top_billvideo=0;top_gr_topic_reweight=0;top_followtop=0;top_feedre_cpt=101;top_tagore=1;top_topic_feedre=21;top_login_card=1;pin_ef=orig;web_ask_flow=default;top_tr=0;top_video_rew=0;top_billread=1;top_lowup=1;tp_sft=a;top_billupdate=0;top_feedre_itemcf=31;top_multi_model=0;web_logoc=blue;top_newfollow=0;top_ebook=0;top_feedre_rtt=41;top_f_r_nb=1',
	'x-requested-with': 'Fetch',
	'x-udid': 'AMClbnasCw6PTs-Zv-IVDpi10YouMUFWQjY=',
	'x-xsrftoken': '3885b220-95d4-439b-a414-5814e49e9140',
}

response = requests.post(url="https://www.zhihu.com/api/v3/account/api/login/qrcode", headers=headers)
print(response.status_code)
print("*"*50)

# for item in headers["Cookie"].split(";"):
# 	print(item.split("=")[0])

print(response.text)