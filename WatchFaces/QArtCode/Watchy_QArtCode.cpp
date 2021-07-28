#include "Watchy_QArtCode.h"
#include <stdlib.h>     //srand, rand

unsigned char image_bytes[5000];

WatchyQArtCode::WatchyQArtCode(){} //constructor

void WatchyQArtCode::drawWatchFace(){

    String image_string;

    display.fillScreen(GxEPD_BLACK);
    display.setTextColor(GxEPD_WHITE);
    display.setCursor(0, 24);
    display.println("TESTING 2!");

    if(connectWiFi()){//Use Weather API for live data if WiFi is connected
        HTTPClient http;
        http.setConnectTimeout(3000);//3 second max timeout
        String imageURL = "http://192.168.0.66:8887/byte-fileO1373289.img";
        http.begin(imageURL.c_str());
        int httpResponseCode = http.GET();
        if(httpResponseCode == 200) {
            Serial.print("Got 200 response");
            Serial.println();
            int bodyLen = http.getSize();
            Serial.print("Body size is ");
            Serial.println(bodyLen);
            image_string = http.getString();
            Serial.print("String size is ");
            Serial.println(image_string.length());
            image_string.getBytes(image_bytes, 5000);
            display.fillScreen(GxEPD_WHITE);

            for (int i=0; i <50; i++) {
              Serial.print("Char ");
              Serial.print(i);
              Serial.print(" is ");
              Serial.println((int)image_string.charAt(i));
              
            }

            int row = 0;
            int column = 0;

            for (int i=0; i <5000; i++) {
              Serial.print("byte ");
              Serial.print(i);
              Serial.print(" value ");
              //Serial.println(image_bytes[i]);
              Serial.println((int)image_string.charAt(i));
              for (int j=0; j < 8; j++) {
                // oddly read from the wrong end of they byte?
                int pixelValue = bitRead((int)image_string.charAt(i), 7 - j);
                Serial.print(pixelValue);
                if (pixelValue == 0) {
                  display.drawPixel(row, column, GxEPD_BLACK);
                } else {
                  display.drawPixel(row, column, GxEPD_WHITE);
                }
                row++;
                if (row % 200 == 0) {
                  row = 0;
                  column++;
                }
              }
            }

             //String payload = http.getString();
            // JSONVar responseObject = JSON.parse(payload);
            // currentWeather.temperature = int(responseObject["main"]["temp"]);
            // currentWeather.weatherConditionCode = int(responseObject["weather"][0]["id"]);            
        }else{
            //http error
            Serial.println("http error");
            // draw a default QR code until we get wifi back
            display.drawBitmap(0, 0, bitmap_broken, DISPLAY_WIDTH, DISPLAY_HEIGHT, GxEPD_WHITE);
        }
        http.end();

        //turn off radios
        WiFi.mode(WIFI_OFF);
        btStop();
    }else{//No WiFi
            Serial.println("no wifi");
    }
    
    Serial.print("just did something");
    Serial.println();
}
