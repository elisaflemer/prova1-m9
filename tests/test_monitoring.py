
import time
import json
import pytest
import uuid
from monitoring.cli import publisher as source
from monitoring.cli import subscriber as sub
import paho.mqtt.client as mqtt



test_message = {
    'id': 'lj1g1', 'tipo': 'Freezer', 'temperatura': -28, 'timestamp': '8/3/2024 10:29'
}

qos = None

# Callback para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Conexão bem sucedida!")
    else:
        print(f"Conexão falhou! Código {reason_code}")
        exit(reason_code)

def on_message(client, userdata, message):
    global qos
    qos = message.qos()
    print(qos)
    global received_message
    received_message = json.load(message.payload.decode())

def test_qos():
    global qos
    qos = None
    global test_message
    subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "subscriber")
    subscriber.on_connect = on_connect
    subscriber.on_message = on_message
    subscriber.connect("localhost", 1891, 60)
    subscriber.subscribe('test')

    publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "publisher")
    publisher.on_connect = on_connect
    publisher.connect("localhost", 1891, 60)
    
    source.publish_message(publisher, 'test', json.dumps(test_message))

    time.sleep(1)

    assert qos == 1

def test_integrity():
    global received_message 
    received_message = None

    global test_message
    
    publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "publisher")
    publisher.on_connect = on_connect
    publisher.connect("localhost", 1891, 60)
    
    source.publish_message(publisher, 'test', json.dumps(test_message))

    time.sleep(1)

    assert test_message == sub.

def test_alarm():
    low_temp_freezer = {
        'id': 'lj1f1', 'tipo': 'Freezer', 'temperatura': -30, 'timestamp': '8/3/2024 10:29'
    }

