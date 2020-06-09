
//--------------------------------
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
//-------------------------------
#include <RTClib.h>
#include <Wire.h>
RTC_DS3231 rtc;
char t[32];
boolean otpr ;
//------------------------------

//-------- Настройки Wi-Fi -----------
const char* ssid = "Beeline_2G_F43654";           // Имя
const char* password = "W123456w";      // пароль

//-------- IBM соединение - ESP32 -----------
#define ORG "0k740p" // ID организации
#define DEVICE_TYPE "Esp8266" // Введите имя компонента
#define DEVICE_ID "seradya" // введите идентификатор
#define TOKEN "NDdVf07KBd2vjL(e6d"// Вставьте токен

//-------- IOT связь --------

char server[] = ORG ".messaging.internetofthings.ibmcloud.com";
char authMethod[] = "use-token-auth";
char token[] = TOKEN;
char clientId[] = "d:" ORG ":" DEVICE_TYPE ":" DEVICE_ID;
const char eventTopic[] = "iot-2/evt/status/fmt/json";
const char cmdTopic[] = "iot-2/cmd/command/fmt/json";

void callback(char* topic, byte* payload, unsigned int payloadLength);
WiFiClient wifiClient;
PubSubClient client(server, 1883, callback, wifiClient);



void setup()
{
  Serial.begin(9600);
  //-----------------------------------------------------------------------
  Wire.begin();
  rtc.begin();
  rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  //----------------------------------------------------------------------
  pinMode(13, OUTPUT);              // LED13, который будет работать на волосах IBM
  pinMode(2, OUTPUT);               // LED2 показывает подключение к Интернету
  client.setCallback(callback);      // Настраивает на возврат функции
  client.subscribe(cmdTopic);
  wifiConnect();
  mqttConnect();
}

//connect wifi
void wifiConnect()
{ // Função void wifiConnect
  Serial.print("Conectando a Rede ");
  Serial.print(ssid);                // Указывает на сеть, к которой подключится ESP32
  WiFi.begin(ssid, password);        // Подключается к ssid и настроенному паролю
  while (WiFi.status() != WL_CONNECTED)
  { // Пока отключен
    delay(500);                      // Ждет 500 миллисекунд
    Serial.print(".");
  }
  Serial.print("Wi-Fi conectado, Endereço de IP: ");
  Serial.println(WiFi.localIP());     // Указывает IP-адрес
}

//connect mqtt
void mqttConnect()
{ // Função void mqttConnect
  if (!!!client.connected())
  {
    Serial.print("Reconectando MQTT do cliente ");
    Serial.println(server);                       // Указывает адрес сервера
    while (!!!client.connect(clientId, authMethod, token) )
    {
      Serial.print(".");
      delay(500);
    }
    if (client.subscribe(cmdTopic))
    {
      Serial.println("Resposta OK");              // Если ответ в порядке
      digitalWrite(2, LOW);                            // LED 2 OFF
    }
    else
    {
      Serial.println("Resposta FALHOU");   // Если ответ не получится
      digitalWrite(2, HIGH);                          // LED 2 ON
    }
  }
}

void loop()
{
  if (!client.loop())
  {
    mqttConnect();
  }
  // проверяет, верен ли возврат, в противном случае что-то не так.
  /*if (isnan((float)dht.readHumidity()) || isnan((float)dht.readTemperature()))
    {
    Serial.println("Failed to read from DHT");
    delay(2000);
    }
    else
    {  */
  String payload = "{\"ti\":";      // Начинается строка, связывающаяся с адресом
  //    payload += (dht.readHumidity());                 // Назначает значение показания температуры для строки
  payload += (25);
  payload += (",");
  payload += "\"to\":";
  //    payload += (dht.readTemperature());
  payload += (random(-10, 50));
  payload += (",");
   payload += "\"tw\":";
    payload += (40);
    payload += ",";
    payload += "\"pr\":";
    payload += (760);
    payload += ",";
    payload += "\"hi\":";
    payload += (90);
    payload += ",";
    payload += "\"ho\":";
    payload += (70);
    payload += ",";
    payload += "\"vo\":";
    payload += (14.4);
    payload += ",";
    payload += "\"ra\":";
    payload += (0);

  payload += "}";// Завершает строку.
  DateTime now = rtc.now();
  sprintf(t, "%02d:%02d:%02d %02d/%02d/%02d",  now.hour(), now.minute(), now.second(), now.day(), now.month(), now.year());
  Serial.print(F("Date/Time: "));
  Serial.println(t);
  if ((now.minute()%2 == 0)and(otpr == 0)){
    otpr = 1;
  Serial.print("Enviando payload: ");
  Serial.println(payload);                  // Запишите строку в последовательный монитор
  client.publish(eventTopic, (char*) payload.c_str() );  // Опубликовать строку
  delay(500);
  }
  if (now.minute()%2 != 0){
    otpr = 0;
  }
  delay(500);
  // }
}

void callback(char* topic, byte* payload, unsigned int payloadLength)
{
  //armazena msg recebida em uma sring
  payload[payloadLength] = '\0';
  String MSG = String((char*)payload);

  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  Serial.print(MSG);
  if ((char)payload[0] == '0')
  { // Caso receba o caractere 0
    digitalWrite(22, LOW);
    Serial.println("LOW");
  }
  if ((char)payload[0] == '1')
  { // Caso receba o caractere 1
    digitalWrite(22, HIGH);
    Serial.println("HIGH");
  }
}