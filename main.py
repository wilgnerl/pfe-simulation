import random
import uuid
import json
import requests
import schedule
import time


def read_sensors():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    identifier = str(uuid.uuid4())
    temperature = round(random.uniform(0, 40), 1)
    ph = random.randint(0, 14)
    o2_dissolved = round(random.uniform(0, 100), 2)

    return json.dumps({
        "latitude": latitude,
        "longitude": longitude,
        "identifier": identifier,
        "temperature": temperature,
        "ph": ph,
        "o2_dissolved": o2_dissolved
    }, indent=2)


def read_task():
    url = "http://127.0.0.1:5000/sensor-data"

    sensor_data = read_sensors()

    # Fazer uma solicitação POST para o endpoint
    response = requests.post(url, json=sensor_data)

    # Verificar a resposta
    if response.status_code == 200:
        print("POST dados do sensor enviado!")
        json_string = response.text
        # Primeiro, carregue a string JSON em um dicionário Python
        data = json.loads(json_string)

        # Em seguida, obtenha o valor associado à chave "dados recebidos"
        dados_recebidos = json.dumps(
            json.loads(data['dados recebidos']), indent=2)
        print(dados_recebidos)
    else:
        print("Erro no POST. Código de status:", response.status_code)


# Agende a função para ser executada a cada 2 segundos
schedule.every(2).seconds.do(read_task)

# Execute a agenda em um loop
while True:
    schedule.run_pending()
    time.sleep(1)
