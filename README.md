# Prova 1

Este é um sistema de visualização de monitoramento de temperaturas de loja em CLI via MQTT. O sistema possui um publisher, que publica as temperaturas, e um subscriber que as mostra e informa se elas estão dentro do normal. Para rodar, basta clonar esse repositório, iniciar o pacote e executar os nós.

## Como rodar 

```
pip install paho-mqtt
pip install -e ".[test]"
python3 subscriber.py
python3 publisher.py
```

## Como testar

```
pytest
```

## Demo

[Screencast from 2024-03-08 11-02-53.webm](https://github.com/elisaflemer/prova1-m9/assets/99259251/9d1e00d5-fcc8-46d5-ae2b-429e5f580114)
