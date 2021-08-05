# Python program to get a random V&A object URL, get it as a QR code and them use PIL to convert
# the image to a 5000 byte array to send to an Arduino-based Watchy (200px x 200px e-ink display)

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
    print("There are {} objects that match".format(record_count))
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

        img = img.convert("1") # 1 bit black/white
        newFileByteArray = img.tobytes()

        file2.write(newFileByteArray)

        file2.close()

        # print(newFileByteArray)

        # uncomment to debug
        # img.show()


@app.route("/")
def send_file():
    get_file()
    return send_from_directory('.', 'qr-bytes.img')

if __name__ == "__main__":
    app.run(host="0.0.0.0")

