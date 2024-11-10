import requests

cookies = {
    'UBT_VID': '1730213552624.cea11kd6JEpT',
    'MKT_CKID': '1730213552723.xexi1.aqap',
    'GUID': '09031133218788269339',
    '_ga': 'GA1.1.28703764.1730213553',
    '_RSG': 'yuKmfg5U_i9iK3SWp3EqY8',
    '_RDG': '28f47fcd8f5d04241918c8d88bf997fb0b',
    '_RGUID': '9b3f785a-a9c1-4e3c-88b4-383ce070352c',
    'MKT_Pagesource': 'PC',
    'ibulanguage': 'CN',
    'ibulocale': 'zh_cn',
    'cookiePricesDisplayed': 'CNY',
    'nfes_isSupportWebP': '1',
    '_bfaStatusPVSend': '1',
    'StartCity_Pkg': 'PkgStartCity=1',
    '_ubtstatus': '%7B%22vid%22%3A%221730213552624.cea11kd6JEpT%22%2C%22sid%22%3A4%2C%22pvid%22%3A20%2C%22pid%22%3A290573%7D',
    '_bfaStatus': 'success',
    'intl_ht1': 'h4=2_4978892',
    'Hm_lvt_a8d6737197d542432f4ff4abc6e06384': '1730726197,1730727949,1730987553,1731215972',
    'Hm_lpvt_a8d6737197d542432f4ff4abc6e06384': '1731215972',
    'HMACCOUNT': 'F8778ABB6A39AE45',
    '_ga_9BZF483VNQ': 'GS1.1.1731215972.4.0.1731215974.0.0.0',
    '_ga_5DVRDQD429': 'GS1.1.1731215972.4.0.1731215974.0.0.0',
    '_ga_B77BES1Z8Z': 'GS1.1.1731215972.4.0.1731215974.58.0.0',
    '_RF1': '141.11.46.171',
    '_jzqco': '%7C%7C%7C%7C1731215554712%7C1.501347343.1730213552718.1731216010394.1731216020089.1731216010394.1731216020089.undefined.0.0.70.70',
    '_bfa': '1.1730213552624.cea11kd6JEpT.1.1731216011906.1731216021785.5.13.290510',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'UBT_VID=1730213552624.cea11kd6JEpT; MKT_CKID=1730213552723.xexi1.aqap; GUID=09031133218788269339; _ga=GA1.1.28703764.1730213553; _RSG=yuKmfg5U_i9iK3SWp3EqY8; _RDG=28f47fcd8f5d04241918c8d88bf997fb0b; _RGUID=9b3f785a-a9c1-4e3c-88b4-383ce070352c; MKT_Pagesource=PC; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; nfes_isSupportWebP=1; _bfaStatusPVSend=1; StartCity_Pkg=PkgStartCity=1; _ubtstatus=%7B%22vid%22%3A%221730213552624.cea11kd6JEpT%22%2C%22sid%22%3A4%2C%22pvid%22%3A20%2C%22pid%22%3A290573%7D; _bfaStatus=success; intl_ht1=h4=2_4978892; Hm_lvt_a8d6737197d542432f4ff4abc6e06384=1730726197,1730727949,1730987553,1731215972; Hm_lpvt_a8d6737197d542432f4ff4abc6e06384=1731215972; HMACCOUNT=F8778ABB6A39AE45; _ga_9BZF483VNQ=GS1.1.1731215972.4.0.1731215974.0.0.0; _ga_5DVRDQD429=GS1.1.1731215972.4.0.1731215974.0.0.0; _ga_B77BES1Z8Z=GS1.1.1731215972.4.0.1731215974.58.0.0; _RF1=141.11.46.171; _jzqco=%7C%7C%7C%7C1731215554712%7C1.501347343.1730213552718.1731216010394.1731216020089.1731216010394.1731216020089.undefined.0.0.70.70; _bfa=1.1730213552624.cea11kd6JEpT.1.1731216011906.1731216021785.5.13.290510',
    'cookieorigin': 'https://you.ctrip.com',
    'origin': 'https://you.ctrip.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://you.ctrip.com/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

params = {
    '_fxpcqlniredt': '09031133218788269339',
    'x-traceID': '09031133218788269339-1731216076562-1415533',
}

json_data = {
    'head': {
        'cid': '09031133218788269339',
        'ctok': '',
        'cver': '1.0',
        'lang': '01',
        'sid': '8888',
        'syscode': '999',
        'auth': '',
        'xsid': '',
        'extension': [],
    },
    'scene': 'online',
    'districtId': 1,
    'index': 1,
    'sortType': 1,
    'count': 10,
    'filter': {
        'filterItems': [],
    },
    'returnModuleType': 'product',
}

response = requests.post(
    'https://m.ctrip.com/restapi/soa2/18109/json/getAttractionList',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"head":{"cid":"09031133218788269339","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"999","auth":"","xsid":"","extension":[]},"scene":"online","districtId":1,"index":2,"sortType":1,"count":10,"filter":{"filterItems":[]},"returnModuleType":"product"}'
#response = requests.post(
#    'https://m.ctrip.com/restapi/soa2/18109/json/getAttractionList',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)