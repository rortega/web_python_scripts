import hashlib

def sha1_hash_string(input_string):
    sha1= hashlib.sha1()
    sha1.update(input_string.encode('utf-8'))
    return sha1.hexdigest()



password   ="8635fcxxx5757e"
admin_pass ="f865bxxxf8c227"

session= "2583dc850xxxx68ab03766"



hashed = sha1_hash_string(password+session)
admin_hashed = sha1_hash_string(admin_pass+session)

print(f"teacher->{hashed}")
print(f"admin->{admin_hashed}")
