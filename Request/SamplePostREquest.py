import requests
from colorama import Fore,Back, Style

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


proxies = {
    "http":"http://192.168.86.199:8080",
    "https":"http://192.168.86.199:8080"
}


headers = {
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkNVNDZNaDVkeWRibndfTkk4UzdjZFU2MmJJZmtKWHhFbTUzaFM3VmxnNFkiLCJ0eXAiOiJKV1QifQ.eyJ2ZXIiOiIxLjAiLCJpc3MiOiJodHRwczovL3Byb2RmbWdpZHAuYjJjbG9naW4uY29tLzcxYTE2MGE2LTdhYmQtNGM3Zi04ODUzLTkyNTM0YWVjMjljMC92Mi4wLyIsInN1YiI6ImIxOWUzZjcxLThhODItNDJiZS05MWFhLWMxMzk4NGVlYWYzMiIsImF1ZCI6ImMzMTE1NDg4LWRmN2EtNDhiNi1hZmRmLTVjOWJmOWJiNTBhOCIsImV4cCI6MTY5NzQ3Nzg2NiwiYWNyIjoiYjJjXzFhX21haW5fc2lnbnVwX3NpZ25pbiIsIm5vbmNlIjoiODMxMzY5ZGQtY2U2ZC00MTVkLThlOTMtMjg2ZmJkYmUxOTJhIiwiaWF0IjoxNjk3NDc2MDY2LCJhdXRoX3RpbWUiOjE2OTc0NzYwNjIsImVtYWlsIjoicHJvZC1wd2QtbXB0LXVzZXJzaW11bGF0ZXJlYWRvbmx5LTAxQHByb2RmbWdpZHAub25taWNyb3NvZnQuY29tIiwiY29ycmVsYXRpb25JZCI6IjI4YjdhMmM4LTA1NTQtNGU4ZS04ZjNkLWI1ZWM0YzliODg0ZSIsInVzZXJfdXVpZCI6IjRjNjFlZTM3LWVmMDQtNDM4ZC1hMTBlLTMyMzkyNjM5NjRkZCIsImdpdmVuX25hbWUiOiJwcm9kZWVlZWUiLCJmYW1pbHlfbmFtZSI6IlVzZXJTaW11bGF0ZVJlYWRPbmx5IiwiZGNlLXJvbGVzIjpbIm5vdGlmeS1oaWdoIiwicmVsaS1zdXBwb3J0IiwiYWRkcmVzcy1wcm9jZXNzaW5nIiwicmVsaS1jdXJhdGlvbiIsInZmc3QiLCJkZXNrdG9wLWFzc2Vzc21lbnQtYWxsIiwiZ2xvYmFsLXJpc2siLCJkc3Itdmlld2VyLXJlYWQtYWxsIiwicGxhdGZvcm0tdXNlciIsImdsb2JhbC1jbGFpbXMiLCJjb3ZlcmFnZSIsImNsaW1hdGUtY2hhbmdlLXJlc2VhcmNoIiwiY2xpbWF0ZS1jaGFuZ2UtY3N0IiwicHJldmlzaXQtbG9jYXRpb24tY29udGFjdCIsImxvY2F0aW9uLWFzc2Vzc21lbnQtZmllbGQtZW5naW5lZXIiLCJsb2NhdGlvbi1yaXNrIl0sImlkcCI6ImIyYyIsIm5hbWUiOiJwcm9kIFVzZXJTaW11bGF0ZVJlYWRPbmx5IiwidGlkIjoiNzFhMTYwYTYtN2FiZC00YzdmLTg4NTMtOTI1MzRhZWMyOWMwIiwiYXRfaGFzaCI6ImZSZFRYbVhlTUo4QnBsYTBrSDRpa0EiLCJuYmYiOjE2OTc0NzYwNjZ9.dcwmae_S3tXxsp9zOsW6AzldhXEf2H5UbnG7E5L2ATPMRxJTkJ3D81k6IhXn3yXzbNsUQyfMVkeoU2bel_zWWWqy0bhyp0Lza0xUD0sJQfXDD8hN2mldEBNyQ0Y4Jymh3M0AUaZdt5stiyMnNtSMjOm-9gX03x2gfaC6XqyyfAdJV8a_lrl-pQjStzjzb2EEzVDi23alpRNXRCPfrHpdN6tvPawvHpKPSNve47oD7U7t0ccJwPPZSQsWnmwZ18Nq-B6DFLcYYx_Kps5QpaJdL23KQIoyIxJSWmVZ5jtyhoqTw4emgzXdGEUfJaqzPL6G-7KnkvZ1kBmUv_sRW9_M-Q",
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
    "operationName":"GlobalPortal_GetActiveUsers_V05",
    "variables":{"uuid":"4c61ee37-ef04-438d-a10e-3239263964dd"},
    "query":"query GlobalPortal_GetActiveUsers_V05($uuid: uuid) {\n  users_active_users(where: {user_id: {_eq: $uuid}}) {\n    user_id\n    email_address\n    first_name\n    last_name\n    tags {\n      tag\n      __typename\n    }\n    __typename\n  }\n}\n"
}


get_request = requests.post('https://graphql.app.fmglobal.com',proxies=proxies,headers=headers,json=data,verify=False)
print(format_text("status_code:",get_request.status_code)) 
print(format_text("cookies:",get_request.cookies)) 
print(format_text("headers:",get_request.headers)) 
print(format_text("text:",get_request.text)) 

#post_request = request.post('graphql.app.fmglobal.com', json=data)
