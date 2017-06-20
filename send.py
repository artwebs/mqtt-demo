import paho.mqtt.publish as publish

HOST = "artobj.dev"

publish.single("lettuce", "payload", hostname=HOST, port=1883,
               auth={'username': "admin", 'password':"123233"})
