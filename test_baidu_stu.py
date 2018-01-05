# -*-coding:utf-8-*-
import requests
import os
import json
import re

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}
source='http://image.baidu.com'
#得到vs
vs_url=source+'/?fr=shitu'
vs_page=requests.get(vs_url,headers=headers).text
vs_id=re.findall('window.vsid = "(.*?)"',vs_page)[0]

url='/pcdutu/a_upload?fr=html5&target=pcSearchImage&needJson=true'
filepath=os.getcwd()
pic=u"test1.jpg"
files={'file':(pic,open(filepath+'\\'+pic,'rb'),'image/jpeg'),'pos':(None,'upload'),
       'uptype':(None,'upload_pc'),'fm':(None,'home')}
r=requests.post(source+url,headers=headers,files=files)
tmp=r.text
tmp_json=json.loads(tmp)
queryImageUrl=tmp_json['url']
querySign=tmp_json['querySign']
simid=tmp_json['simid']
url2=source+'/pcdutu?queryImageUrl='+queryImageUrl+'&querySign='+querySign+'fm=index&uptype=upload_pc&result=result_camera&vs='+vs_id
r2=requests.get(url2,headers=headers).text
gussword=re.findall("'guessWord': '(.*?)'",r2)[0]
print gussword

