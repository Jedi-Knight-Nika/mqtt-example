import paho.mqtt.client as mqtt

broker_address = "mosquitto"
port = 1883
topic = "test/fucking-topic"

client = mqtt.Client("subscriber")

def on_connect(client, userdata, flags, response_code):
    if response_code == 0:
        print("connected to broker")
        client.subscribe(topic)
    else:
        print(f"connection failed with code {response_code}")

def on_message(client, userdata, message):
    print(f"received `{message.payload.decode()}` from `{message.topic}` topic")

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port=port)
client.loop_forever()