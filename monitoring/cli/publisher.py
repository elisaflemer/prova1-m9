import paho.mqtt.client as mqtt
import time
import json
import random
import datetime

# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")

# Conecte ao broker
client.connect("localhost", 1891, 60)


def generate_reading():
    type_appliance = random.choice(["Freezer", "Geladeira"])
    temperature = random.randint(-30, -5) if type_appliance == "Freezer" else random.randint(0, 15)
    right_now = datetime.datetime.now()
    suffix = 'f' if type_appliance == "freezer" else 'g'
    full_id = f'lj{random.randint(1, 6)}' + suffix + f'{random.randint(1, 3)}'
    print(full_id)
    return {
         "id": full_id,
  "tipo": type_appliance,
  "temperatura": temperature, 
  "timestamp": f"{right_now.day}/{right_now.month}/{right_now.year} {right_now.hour}:{right_now.minute}"
    }

def publish_message(client, topic, message):
    client.publish(topic, json.dumps(message), qos=1)
    print(f"Publicado: {message} em {topic}")

def run():
    try:
        while True:
            message = generate_reading()
            topic = f'stores'
            publish_message(client, topic, message)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Publicação encerrada")
    client.disconnect()

if __name__ == '__main__':
    run()