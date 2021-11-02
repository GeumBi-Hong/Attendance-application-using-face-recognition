import paho.mqtt.client as mqtt
import time
from bluetooth import *

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("raspberry connected!")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    message=str(msg.payload.decode("utf-8"))
    print(msg.topic+" : "+"received message :"+ message)

#블루투스연결
socket = BluetoothSocket(RFCOMM)
socket.connect(("00:18:E4:0A:00:01", 1))
print("bluetooth connected!")

# 새로운 클라이언트 생성
client = mqtt.Client()
# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
# on_message(발행된 메세지가 들어왔을 때)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message
# address : localhost, port: 1883 에 연결
client.connect('192.168.0.61', 1883)
# common topic 으로 메세지 발행

#client.loop_forever()
client.loop_start()

if __name__ == '__main__':
        msg = ["0","0"]
        while True:
                msg[0] = socket.recv(1024)
                msg[0] = msg[0].decode('utf-8')
                msg[1] = socket.recv(1024)
                msg[1] = msg[1].decode('utf-8')
                mqtt = msg[0]+msg[1]
                print("recv msg : {}".format(mqtt))
                client.publish("hansung/arduino/temp",mqtt,qos=0)
        socket.close()
