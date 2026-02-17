import json
import paho.mqtt.client as mqtt
from .models import SumpReading

BROKER = "broker.hivemq.com"
TOPIC = "sump/data"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print("Received:", data)

        SumpReading.objects.create(
            water_level=data["water_level"],
            mud_level=data["mud_level"],
            leakage_current=data["leakage_current"],
            motor_status=data["motor_status"],
        )

        print("Saved to database")

    except Exception as e:
        print("Error:", e)

def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, 1883, 60)
    client.loop_start()
