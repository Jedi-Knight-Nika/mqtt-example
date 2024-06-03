import paho.mqtt.client as mqtt
import time

broker_address = "mosquitto"
port = 1883
topic = "test/fucking-topic"

client = mqtt.Client("publisher")

def on_connect(client, userdata, flags, response_code):
    if response_code == 0:
        print("connected to broker")
    else:
        print(f"connection failed with code {response_code}")

def on_publish(client, userdata, mid):
    print(f"message {mid} published.")

client.on_connect = on_connect
client.on_publish = on_publish

client.connect(broker_address, port=port)
client.loop_start()

def publish_message():
    msg_count = 0
    while True:
        message = f"message {msg_count}"
        result = client.publish(topic, message)
        status = result.response_code
        if status == mqtt.MQTT_ERR_SUCCESS:
            print(f"send `{message}` to topic `{topic}`")
        else:
            print(f"failed to send message to topic {topic} with status {status}")
        msg_count += 1
        time.sleep(1)

if __name__ == "__main__":
    publish_message()