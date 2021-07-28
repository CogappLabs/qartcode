#include "Cogapp_Logo.h"
#include <stdlib.h>     //srand, rand

// All code based on RandPics example from https://github.com/wolfdtx/RandPics 
const unsigned char *art_sheet [5] = {cogapp_logo, qr_code_test, noor_test, byte_fileO1373289_img, collection_O1373289};

CogappLogo::CogappLogo(){} //constructor

void CogappLogo::drawWatchFace(){
    display.fillScreen(GxEPD_BLACK);
    srand(currentTime.Minute * currentTime.Hour * currentTime.Wday); //seeds rand() with the current minute causing watchy to display a new random image once per minute
    int ran;
    ran = (rand() % 5);
    //ran = (currentTime.Minute % 2);
    //change the % after rand() to the size of *art_sheet []
    display.drawBitmap(0, 0, art_sheet[ran], DISPLAY_WIDTH, DISPLAY_HEIGHT, GxEPD_WHITE); //draws a random image from *art_sheet [] full size
    Serial.print("just wrote a bitmap from variable with random ");
    Serial.print(ran, DEC);
    Serial.println();
    Serial.print(sizeof(art_sheet), DEC);
    Serial.println();
    Serial.print(sizeof(art_sheet[1]), DEC);
    Serial.println();
    Serial.print(sizeof(qr_code_test), DEC);
    Serial.println();

}
