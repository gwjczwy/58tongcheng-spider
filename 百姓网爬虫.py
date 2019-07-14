import requests
import time
from bs4 import BeautifulSoup as bs

url='https://'+input('输入网址')+'/search/?query=%E5%8F%91%E7%94%B5%E6%9C%BA%E7%A7%9F%E8%B5%81'
def main():
    for i in range(50):
        url='https://donghai.baixing.com/search/?page='+str(i)+'&query=%E5%8F%91%E7%94%B5%E6%9C%BA%E7%A7%9F%E8%B5%81'
        infoList=getDetails(url)
        with open('./'+time.strftime("%Y-%m-%d %H.%M.%S", time.localtime())+'.txt','w') as output:
            for i in infoList:
                output.write(str(i).replace("'",'')+'\n')
        

def getDetails(url): 
    headers={
      'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.25 (KHTML, like Gecko) Chrome/12.0.706.0 Safari/534.25',
      'Referer':'https://baixing.com/'
      }
    url='https://nanjing.baixing.com/search/?query=%E5%8F%91%E7%94%B5%E6%9C%BA%E7%A7%9F%E8%B5%81'
    req=requests.get(url,headers=headers)
    # print(req.text)
    req=bs(req.text,'html.parser')
    urllist=[i['href'] for i in req.select('.main ul li .media-cap')]
    infoList=[]
    for i in urllist:
    #     print(i)
        try:
            info=getinfo(i)
        except:
            info='get info fall!!'
        infoList.append(info)
        print(info)
    info=[]
    for i in infoList:
        if i not in info:
            info.append(i)
    return infoList

def getinfo(url): 
    headers={
      'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.25 (KHTML, like Gecko) Chrome/12.0.706.0 Safari/534.25',
      'Referer':'https://baixing.com/'
      }
    req=requests.get(url,headers=headers)
    # print(req.text)
    req=bs(req.text,'html.parser')
    info={}
    try:
        info['电话号码']=req.select('#mobileNumber strong')[0].text
    except:
        info['电话号码']='获取失败'+url
    req=req.select('.viewad-meta2')
    for i in req[0].select('div'):
        if '公司名称' in i.text:
            txt=i.text.split('：')[1]
            info['公司名称']=f'{txt:^20}'
        elif '服务范围' in i.text:
            txt=i.text.split('：')[1]
            info['服务范围']=f'{txt:^20}'
        elif '联系人' in i.text:
            txt=i.text.split('：')[1]
            info['联系人']=f'{txt:^20}'
    return info
main()