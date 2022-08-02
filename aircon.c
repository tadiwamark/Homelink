#include <SoftwareSerial.h>
SoftwareSerial hc06(2,3);
String cmd="";

void setup(){
pinMode(4,OUTPUT); 
//Initialize Serial Monitor
Serial.begin(9600);
//Initialize Bluetooth Serial Port
hc06.begin(9600);
}

void loop(){
//Read data from HC06
while(hc06.available()>0){
cmd+=(char)hc06.read();
}
//Select function with cmd
if(cmd!=""){
Serial.print("Command recieved : ");
Serial.println(cmd);
// We expect ON or OFF from bluetooth
if(cmd=="demarrer"){
digitalWrite(4,HIGH);//Start the fan
Serial.println("Function is on");
}else if(cmd=="stop"){
digitalWrite(4,LOW);//Stop the fan
Serial.println("Function is off");
}else{
Serial.println("Function is off by default");
}
cmd=""; //reset cmd
}
delay(100);
}