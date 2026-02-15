import time
import json
import random
from confluent_kafka import Producer
from faker import Faker

# Configuratie
conf = {
    'bootstrap.servers': 'localhost:29092', # Let op: 29092 voor externe toegang
    'client.id': 'workshop-producer'
}

producer = Producer(conf)
faker = Faker('nl_NL') # Nederlandse nep-data
topic = 'bestellingen'

def delivery_report(err, msg):
    if err is not None:
        print(f'Bericht gefaald: {err}')
    else:
        print(f'Bericht verstuurd naar {msg.topic()} [{msg.partition()}]')

print("Starten met produceren (CTRL+C om te stoppen)...")

try:
    while True:
        # 1. Maak een nep-bericht
        data = {
            'klant_naam': faker.name(),
            'adres': faker.address(),
            'bestel_bedrag': round(random.uniform(10.0, 500.0), 2),
            'timestamp': time.time()
        }

        # 2. Serialiseer naar JSON string
        value_bytes = json.dumps(data).encode('utf-8')

        # 3. Stuur naar Kafka
        # De key zorgt ervoor dat berichten van dezelfde 'klant' naar dezelfde partitie gaan
        key_bytes = data['klant_naam'].encode('utf-8')

        producer.produce(
            topic,
            key=key_bytes,
            value=value_bytes,
            callback=delivery_report
        )

        # Zorg dat het bericht daadwerkelijk de buffer verlaat
        producer.poll(0)

        time.sleep(1) # Wacht 1 seconde

except KeyboardInterrupt:
    print("Producer gestopt.")
finally:
    producer.flush()
