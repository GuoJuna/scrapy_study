import urllib.request
import urllib.parse
import json

url_pre = 'https://fanyi.baidu.com/langdetect'
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
    'Cookie': 'BIDUPSID=E1AF31454E3AF8D21F19B7339FB7E1DB; PSTM=1635943871; BAIDUID=E7DA9B5624BF3B9429DE0B2FB91A0CCF:FG=1; __yjs_duid=1_e3734e750a788d185597f393d85cc4e91636022884013; MCITY=-164%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36309_36367_36166_34584_36120_36075_36296_36233_26350_36300_36312_36061; BDSFRCVID=CP4OJeC62GHrJf3DeW5yhHYEZtCbfyOTH6f3IpT0TSzy_PTpDxeyEG0PbU8g0KAb5MgwogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJAqVID2tD-3fP36q6_WK-FSqxby26nmLnn9aJ5nJDonO-o_b6bUbqb02f77XxQzbg7a0tTvQpP-eCOVKh823hth2JnTLnORMIT8Kl0MLnolbb0xyUQDjfus5UnMBMni52OnapTn3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-XD6oXjUK; BDSFRCVID_BFESS=CP4OJeC62GHrJf3DeW5yhHYEZtCbfyOTH6f3IpT0TSzy_PTpDxeyEG0PbU8g0KAb5MgwogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJAqVID2tD-3fP36q6_WK-FSqxby26nmLnn9aJ5nJDonO-o_b6bUbqb02f77XxQzbg7a0tTvQpP-eCOVKh823hth2JnTLnORMIT8Kl0MLnolbb0xyUQDjfus5UnMBMni52OnapTn3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-XD6oXjUK; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1651029331; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_PREFER_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; delPer=0; PSINO=3; BA_HECTOR=a0a52l2100a585ahnj1h6he150q; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[CLK3Lyfkr9D]=mk3SLVN4HKm; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1651030720; ab_sr=1.0.1_NmRmZDE3MWE5NzI0ZGQ0YTE1MjBmZGM0NGI2YjY3MzNmOTQ1Y2RiZTJkYTY2OGQ3ZTNiMzM4MGE1YjMxZWFiZjUxYzliYTNkNDljNjAyNTY3M2U0NTNkNjg3YjYzYjJkM2E3NGNlNWU3OGMzMDgwMTI2Yzg1MDgxOWJkZTlkNjc1MTcyMjEyODM2ZmY0MGNlYTkyZTMxZGU1ODM2MTc3Mg=='
}


data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': '3d030ddf8e0e63fd5b625b4c1cde8ade',
    'domain': 'common'
}

# post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post请求的参数 徐存在放在请求对象的参数中 必要要进行编码
request = urllib.request.Request(url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)

print(obj)

