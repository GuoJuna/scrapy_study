import json
import urllib.request

import jsonpath

url = 'https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1651477822239_173&jsoncallback=jsonp174&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'accept': ' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': ' gzip, deflate, br',
    'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': ' _samesite_flag_=true; cookie2=1a1754e594c56027c0fff1a30f86211c; t=f147335fd12a902f13d4afc9a4a5be6f; _tb_token_=536633e3e8e3; cna=VHMJGvNN0mECAXAKIjwb3TPP; v=0; xlly_s=1; _m_h5_tk=92394e46d360528fe98c201afd244e5d_1651468654090; _m_h5_tk_enc=2e3cfce2ea9eb2cf3afd8beb13e62f06; isg=BBMTRwJMdVUcCzkB-HyNWjKmopc9yKeKR4501cUwMzJpRDLmTZkv2jqVf7QqVP-C; l=eBraNQRlLytwv8O_BOfZourza77T8IRjiuPzaNbMiOCP9i1p5NaRW6qn0f89CnhVH6WkR3yG1ZCLBuYhAydSnxv9-xs9_pHmndC..; tfstk=cA6PBgszj8ey6SJQ6L9URkZGMQ9RZDpeCqxBZPmSyLR-KIRliD3pmmiBiCnq-Qf..',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': ' empty',
    'sec-fetch-mode': ' cors',
    'sec-fetch-site': ' same-origin',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
    'x-requested-with': ' XMLHttpRequest'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

content = content.split("(")[1].split(")")[0]

with open('020_解析_jsonpath解析淘票票.json','w', encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(open('020_解析_jsonpath解析淘票票.json', 'r', encoding='utf-8'))

name_list = jsonpath.jsonpath(obj, '$..regionName')

print(name_list)
