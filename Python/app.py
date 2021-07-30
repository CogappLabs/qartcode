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

def get_file():
    # Get a single random object (with images, on display in Kensington)
    req = requests.get('https://api.vam.ac.uk/v2/objects/search?random=1&images_exist=1&data_restrict=descriptive_only&on_display_at=southken&cluster_size=1&cluster_type=category&page_size=1')
    object_data = req.json()
    object_info = object_data["info"]
    object_records = object_data["records"]
    record_count = object_info["record_count"]
    print("There are {record_count} objects that match")
    print(object_records)

    for record in object_records:
        print(record['systemNumber'])
        URL = 'https://api.qrserver.com/v1/create-qr-code/?data=https://collections.vam.ac.uk/item/' + \
              record['systemNumber'] + '&size=200x200'

        with urllib.request.urlopen(URL) as url:
            with open('qr.png', 'wb') as f:
                f.write(url.read())
                f.close()

        img = Image.open('qr.png')

        file2 = open("qr-bytes.img", "wb")

        img = img.convert("1")
        newFileByteArray = img.tobytes()

        file2.write(newFileByteArray)

        file2.close()

        print(newFileByteArray)
        print(img.tobytes("xbm", "1"))

        # uncomment to debug
        # img.show()


@app.route("/")
def send_file():
    get_file()
    return send_from_directory('.', 'qr-bytes.img')

if __name__ == "__main__":
    app.run(host="0.0.0.0")

