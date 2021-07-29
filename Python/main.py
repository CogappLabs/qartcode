# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Python program to read
# image using PIL module
# converting image to qrcode and then change into binary

from PIL import Image
import urllib.request
import requests
from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route("/")
def send_file():
    return send_from_directory('.', 'byte-fileO1375196.img')

if __name__ == "__main__":
    app.run()

# This lets you filter object records by the collecting department in the museum that manages an object.
req = requests.get('https://api.vam.ac.uk/v2/objects/search?id_collection=THES260586')
object_data = req.json()
object_info = object_data["info"]
object_records = object_data["records"]
record_count = object_info["record_count"]
print("There are {record_count} objects that are part of the 'Digital, Architecture and Design' department")
print(object_records)

for record in object_records[0:1]:
    print(record['systemNumber'])
    URL = 'https://api.qrserver.com/v1/create-qr-code/?data=https://collections.vam.ac.uk/item/' + \
          record['systemNumber'] + '&size=200x200'

    with urllib.request.urlopen(URL) as url:
        with open('collection-' + record['systemNumber'] + '.png', 'wb') as f:
            f.write(url.read())
            f.close()

    img = Image.open('collection-' + record['systemNumber'] + '.png')

    file2 = open("byte-file" + record['systemNumber'] + ".img", "wb")

    img = img.convert("1")
    newFileByteArray = img.tobytes()

    file2.write(newFileByteArray)

    file2.close()

    print(newFileByteArray)
    print(img.tobytes("xbm", "1"))

    img.show()
