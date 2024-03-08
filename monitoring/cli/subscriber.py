import paho.mqtt.client as mqtt
import json

# Callback quando uma mensagem é recebida do servidor.
def on_message(client, userdata, message):
    set_message(message)

def set_message(message):
    text = json.loads(message.payload.decode())
    loja = text['id'][2:3]
    tipo = text['tipo']
    numero = text['id'][4:5]
    temperatura = text['temperatura']
    to_be_shown = f'Lj {loja}: {tipo} {numero} | {temperatura}ºC '
    to_be_shown = set_alarms(to_be_shown, tipo, temperatura)
    print(to_be_shown)
    return text

def set_alarms(to_be_shown, tipo, temperatura):
    if tipo == 'Freezer':
        if temperatura  > -15:
            to_be_shown += f'[ALERTA: Temperatura ALTA]'
        elif temperatura < -25:
            to_be_shown += f'[ALERTA: Temperatura BAIXA]'
    else:
        if temperatura  > 10:
            to_be_shown += f'[ALERTA: Temperatura ALTA]'
        elif temperatura < 2:
            to_be_shown += f'[ALERTA: Temperatura BAIXA]'
    return to_be_shown



# Callback para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Conexão bem sucedida!")
        client.subscribe("stores")
    else:
        print(f"Conexão falhou! Código {reason_code}")
        exit(reason_code)

def run():

    # Configuração do cliente
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
    client.on_connect = on_connect
    client.on_message = on_message

    # Conecte ao broker
    client.connect("localhost", 1891, 60)

    # Loop para manter o cliente executando e escutando por mensagens
    client.loop_forever()

if __name__ == "__main__":
    run()