import paho.mqtt.client as mqtt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

name = ""
tempFinish = ""
dpUploadFinsh = ""
temp =""
def on_connect(client, userdata, flag, rc):
        print("connect")
        client.subscribe("hansung/arduino/temp", qos = 0)
        client.subscribe("hansung/pc/webCamCapture", qos = 0)


def on_message(client, userdata, msg) :
      
        global temp 
        global tempFinish
        global dpUploadFinsh
        global name
        if msg.topic == "hansung/pc/webCamCapture":
            name = str(msg.payload.decode("utf-8"))
            print(name)

            dpUploadFinsh = True
          
        if msg.topic == "hansung/arduino/temp":
            temp = str(msg.payload.decode("utf-8"))
            print(temp)
            if name != "": 
                print("사람이름"+name)
                db.collection('studentlist').document(name).update({"temp":temp})
            print(temp)
            tempFinish = True

         
        if tempFinish and dpUploadFinsh == True:
            client.publish("hansung/mobile/reset","ok")
            tempFinish = False
            dpUploadFinsh =False

            print("done")
        
             
        

broker_ip = "113.198.84.40" 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_ip, 80)

client.loop_forever()

