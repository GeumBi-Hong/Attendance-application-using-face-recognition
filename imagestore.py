import pyrebase
import os
import paho.mqtt.client as mqtt
import shutil


#서버로부터 CONNTACK 응답을 받을 때 호출되는 콜백
def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))
   client.subscribe("hansung/mobile/act")
   client.subscribe("hansung/mobile/dbupload") #구독 
   

   
#서버로부터 publish message를 받을 때 호출되는 콜백
def on_message(client, userdata, msg):


    if msg.topic == "hansung/mobile/act":
        act = str(msg.payload)
     

    if msg.topic == "hansung/mobile/dbupload":
        msg.payload = msg.payload.decode("utf-8")
        print("메세지가 도착했습니다.")
        print(msg.topic+" "+"사용자 이름:"+str(msg.payload)) #토픽과 메세지를 출력한다.
  
        dirpath = './train_img/'+str(msg.payload)
        if os.path.exists(dirpath):
          shutil.rmtree(dirpath)
        os.makedirs(dirpath)
        print("folder ok")
        foldername = str(msg.payload)
        path = './train_img/'+foldername #로컬 pc에 저장 위치
        
        print("폴더이름"+foldername)
        for i in range(0,40):
            cloud_dir= foldername+'/'+str(i)+".jpg"
            setImageName= foldername+'_'+str(i)+".jpg"
            #storage.child(cloud_dir).download(cloud_dir,path+'/'+setImageName)
            storage.child(cloud_dir).download(path+'/'+setImageName)
            print("사진저장"+str(i))
        print("사진저장 완료!!")
        client.publish("hansung/pc/imgdownload",qos=0)
            

config = {
    "apiKey": "AIzaSyAl-oNSvBpWa8GGnRSzUKZXKeRFXtClfnQ",
    "authDomain": "capstone-aae4f.firebaseapp.com",
    
     "databaseURL": "https://capstone-aae4f.firebaseio.com",
    "projectId": "capstone-aae4f",
    "storageBucket": "capstone-aae4f.appspot.com",
  }

#Firebase 연동
firebase_storage = pyrebase.initialize_app(config)
storage = firebase_storage.storage()




client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 

client.connect("113.198.84.40", 80, 60) 
client.loop_forever()
