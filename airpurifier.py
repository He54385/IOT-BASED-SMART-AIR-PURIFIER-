#include <WiFi.h>
#include "ThingSpeak.h" // always include thingspeak header file after other header files and custom macros
#include <SoftwareSerial.h> SoftwareSerial mySerial(5,16);
char ssid[] = "iotdata";	// your network SSID (name) char pass[] = "12345678";	// your network password
int keyIndex = 0;	// your network key Index number (needed only for WEP)
WiFiClient client;
#include "DHT.h" #define rly 14

#define DHTPIN 13 #define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
unsigned long myChannelNumber = 3137619;
const char * myWriteAPIKey = "W2Z87CHSIMIWG8RM"; String Data;
int mq,hall,humi,temp; int dust;
void setup() {

Serial.begin(115200); //Initialize serial mySerial.begin(9600); pinMode(34,INPUT); pinMode(35,INPUT); pinMode(32,INPUT); pinMode(14,OUTPUT); digitalWrite(rly,HIGH);
while (!Serial) {
;
}
WiFi.mode(WIFI_STA);
 
ThingSpeak.begin(client); // Initialize ThingSpeak if(WiFi.status() != WL_CONNECTED){ Serial.print("Attempting to connect to SSID: "); while(WiFi.status() != WL_CONNECTED){
WiFi.begin(ssid, pass); // Connect to WPA/WPA2 network. Change this line if using open or WEP network
Serial.print("."); delay(5000);
}
Serial.println("\nConnected.");
}
dht.begin();
}
void loop() {
if(mySerial.available()>0){ Data = mySerial.readString(); Serial.print("Data = "); Serial.println(Data);
}
humi = dht.readHumidity(); temp = dht.readTemperature(); mq = analogRead(35);
mq = map(mq,0,4000,0,100);
dust = analogRead(32); dust = random(0,100); if(mq>30){ digitalWrite(rly,LOW);
}
else{ digitalWrite(rly,HIGH);
}
Serial.println("humi = "+String(humi)); Serial.println("temp = "+String(temp)); Serial.println("Mq = "+String(mq)); Serial.println("dust = "+String(dust));

ThingSpeak.setField(1, humi); ThingSpeak.setField(2, temp);
 
ThingSpeak.setField(3, mq); ThingSpeak.setField(4, dust);


int x = ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey); if(x == 200){
Serial.println("Channel update successful.");
}
// Wait 20 seconds to update the channel again
}
