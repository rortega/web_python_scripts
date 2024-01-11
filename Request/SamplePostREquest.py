import requests
from colorama import Fore,Back, Style
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {
    "http":"http://192.168.86.199:8080",
    "https":"http://192.168.86.199:8080"
}
headers = {
    "authorization": "Bearer eyJVtxxxxxxx9_M-Q",
    "Content-Type": "application/json",
    "Hasura-Client-Name": "GlobalPortal",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0",
    "Accept-Encoding":"gzip, deflate, br"
    }
def format_text(title,item):
    cr ='\r\n'
    section_break = cr + "*" * 20 + cr
    item = str(item)
    text = Style.BRIGHT + Fore.RED + title + Fore.RESET + section_break + item + section_break
    return text
data = {
    "operationName":"xxxxx_V05",
    "variables":{"uuid":"4c61xxxxxxx964dd"},
    "query":"query Gloxxxxs_V05($uuid: uuid) {\n  users_active_users(where: {user_id: {_eq: $uuid}}) {\n    user_id\n    email_address\n    first_name\n    last_name\n    tags {\n      tag\n      __typename\n    }\n    __typename\n  }\n}\n"
}
get_request = requests.post('https://graphql.xxxxxxx.com',proxies=proxies,headers=headers,json=data,verify=False)
print(format_text("status_code:",get_request.status_code)) 
print(format_text("cookies:",get_request.cookies)) 
print(format_text("headers:",get_request.headers)) 
print(format_text("text:",get_request.text)) 

