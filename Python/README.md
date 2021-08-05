# QArtCode server

This folder contains code used to supply data to the Watchy.

It is designed to be deployed as a Heroku Python/Flask app and you can access it directly from https://qartcode.herokuapp.com/

It uses the V&A API to retrieve a random collection object URL, passes that to qrserver.com to get a 200x200 QR code in PNG format, and then uses Pillow to load that image and obtain a list of the 5,000 bytes that represent the image.

These bytes are then served to anything that requests them using Flask.