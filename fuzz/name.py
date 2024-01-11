try:
    fileItem = ['xxx']     
        
    with open("/Users/xxx/Documents/tools/fuzzdb-master/wordlist/names.json","r") as file:
        f = file.read()
        for item in f.split("\n"):
            length = len(item)
            fileItem.append(item[3:len(item)-2]+"\n")

    with open("/Users/xxx/Documents/tools/fuzzdb-master/wordlist/json_names.txt","w") as afile:
        for i in fileItem:
            afile.write(f"{i}")
            print(".")


except Exception as e:
    print(f"Error {e}")
