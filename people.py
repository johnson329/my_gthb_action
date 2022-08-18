import requests

cookies = {
    # '_zap': '2a9834c1-eeac-4702-84be-90ffcd9c13c2',
    # '_xsrf': 'c5b150ad-3392-49fe-9320-8824dbd74859',
    # 'd_c0': 'ABCY1j5pbBWPTiI5Bq4IbNTXdqjOro12fz0=|1660832599',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1660832616',
    '_9755xjdesxxd_': '32',
    'YD00517437729195%3AWM_NI': 'ICj6AY%2F3wa0hSsBJuuaexkML9rOf54H%2FYOIE%2BkJ2SHjt0czrcp%2FeSmm%2Fb8eGZ9IlXs%2BMEFSPjsOO%2B32hoUBsR4QaIOtOQstAksB0TvRcdEgJQvW7lfxo4Esh5M%2BU86MZNEM%3D',
    'YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6ee8ad87fa5af978cd77abb928ea2d85e928f8a87d5609aac9daaf933f29f8d90c52af0fea7c3b92a8b9da6d7c453ededb982b36491ad8eabf87fa3bbb88cd048fbae8187b8408cf197b0cc4fe9b586d3d244aaac0084f97aa1b0e186d267aff1aed9e84d9ae7878ddb79e9938ba7d25caaad81b0aa39f2b8a1b6c17992ec9f82cc45b8919f94f74ba9ad8ed1d77e92bdaca6e64293aa99d8ef6ebcb1fca6f264f793e5b6bb3e8f8682a6d037e2a3',
    'YD00517437729195%3AWM_TID': 'LBtKwlUegoxFFUEQBBLADI8XNy9nFWoB',
    'gdxidpyhxdE': '6Aga6iPCmmduLGdHj%2F5nLVlGIeZ3bb6eOO8tpC4HkzWyL9AXGELeXvxXyLbcYGgl9yCCEZ21D7DQr1TAtX3%5CqAGnVoHPrPtilD57%5C%2BfhSCUJA%5C1e%5CrV%2FSrQDMAabdVOywWKCJwXq3L2cOi%2FGdfGLNeZkltGGHf8%2FJYlLvyR17G1eUT%5C8%3A1660834401041',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1660833836',
    # 'captcha_session_v2': '2|1:0|10:1660833836|18:captcha_session_v2|88:NWgwVWhxeEtPeEkrV2w0TktlMXhiUGhpcGIxZlVUZW1hMDRpRm52WGk0UUI4Wm1IUjBtaXkzaXlkTitiaXYzNA==|60a14eb6a6312c129108cf50c033f41b9ebaa285993cb2710267d3f5c3530a76',
    'KLBRSID': 'cdfcc1d45d024a211bb7144f66bda2cf|1660833854|1660832599',
}

headers = {
    'authority': 'www.zhihu.com',
    'accept': '*/*',
    'accept-language': 'zh',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_zap=2a9834c1-eeac-4702-84be-90ffcd9c13c2; _xsrf=c5b150ad-3392-49fe-9320-8824dbd74859; d_c0=ABCY1j5pbBWPTiI5Bq4IbNTXdqjOro12fz0=|1660832599; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1660832616; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=ICj6AY%2F3wa0hSsBJuuaexkML9rOf54H%2FYOIE%2BkJ2SHjt0czrcp%2FeSmm%2Fb8eGZ9IlXs%2BMEFSPjsOO%2B32hoUBsR4QaIOtOQstAksB0TvRcdEgJQvW7lfxo4Esh5M%2BU86MZNEM%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee8ad87fa5af978cd77abb928ea2d85e928f8a87d5609aac9daaf933f29f8d90c52af0fea7c3b92a8b9da6d7c453ededb982b36491ad8eabf87fa3bbb88cd048fbae8187b8408cf197b0cc4fe9b586d3d244aaac0084f97aa1b0e186d267aff1aed9e84d9ae7878ddb79e9938ba7d25caaad81b0aa39f2b8a1b6c17992ec9f82cc45b8919f94f74ba9ad8ed1d77e92bdaca6e64293aa99d8ef6ebcb1fca6f264f793e5b6bb3e8f8682a6d037e2a3; YD00517437729195%3AWM_TID=LBtKwlUegoxFFUEQBBLADI8XNy9nFWoB; gdxidpyhxdE=6Aga6iPCmmduLGdHj%2F5nLVlGIeZ3bb6eOO8tpC4HkzWyL9AXGELeXvxXyLbcYGgl9yCCEZ21D7DQr1TAtX3%5CqAGnVoHPrPtilD57%5C%2BfhSCUJA%5C1e%5CrV%2FSrQDMAabdVOywWKCJwXq3L2cOi%2FGdfGLNeZkltGGHf8%2FJYlLvyR17G1eUT%5C8%3A1660834401041; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1660833836; captcha_session_v2=2|1:0|10:1660833836|18:captcha_session_v2|88:NWgwVWhxeEtPeEkrV2w0TktlMXhiUGhpcGIxZlVUZW1hMDRpRm52WGk0UUI4Wm1IUjBtaXkzaXlkTitiaXYzNA==|60a14eb6a6312c129108cf50c033f41b9ebaa285993cb2710267d3f5c3530a76; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1660833854|1660832599',
    'pragma': 'no-cache',
    'referer': 'https://www.zhihu.com/people/warmwine/answers?page=2',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-ab-pb': 'CtwBGwA/AEcAtABpAWoBdAE7AswC1wLYAk8DUAOgA6EDogO3A/MD9AMzBIwEjQSmBNYEEQUpBTIFUQWLBYwFngUWBjAGMQZ+BusGJwdXB3cHeAebB9gH3AfdBycIZwh0CHYIeQjFCNoI5Qg/CUIJVAlVCWAJjQmrCcMJxAnFCcYJxwnICckJygnLCcwJ0QnlCfEJ9AkECkkKZQprCpgKpQqpCr4KxArUCt0K7Qr9Cv4KKQs7CzwLQwtGC3ELdguFC4cLjQu5C8AL1wvgC+UL5gs4DHEMjwysDMMMyQy1CxJuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM=',
    'x-requested-with': 'fetch',
    'x-zse-93': '101_3_3.0',
    'x-zse-96': '2.0_X3KCG5wwG/O6HpB+ZYOW4GuwgTrPReJi=70ckukz0mXlzk/31M8Ir2DBKfG4Mfr0',
    'x-zst-81': '3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZBRY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPF8gB29xLFhrfxrHLeUxKyhxLtgcmhvOVc9N8MvSBSJSf20Y_nhpfjCOM99STvXXB9DoGGCg9Bbr0NDHxtqwLNBC9PcoGxUF9xBCOMXXMgcc__beLzCe9YUS9ebCfyhNmiqVOKTcC0gSGPvNXUvNm_9YLSLN9kve1QJNL09HGoXH_fwH9OqfzhbHL6ccGCqe8BqFB7CX9VhxYOCHYVUpffQN9YqO8uuoYu9XYAgoYwJLK3CHVegefNDx12qVf9qgmtG3_17F8r9HKe7cOcBHMgGom3u3BXBp9WwXCWrNC',
}
s=requests.Session()
for o in [40]:
    url='https://www.zhihu.com/api/v4/members/warmwine/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Cexcerpt%2Cis_labeled%2Clabel_info%2Crelationship.is_authorized%2Cvoting%2Cis_author%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.vessay_info%3Bdata%5B*%5D.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B*%5D.author.vip_info%3Bdata%5B*%5D.question.has_publishing_draft%2Crelationship&offset={}&limit=20&sort_by=created'.format(o)
    response = s.get(url, cookies=cookies, headers=headers)
from lxml import etree

if response.status_code == 200:
    html = etree.HTML(response.text)
    print(html)
