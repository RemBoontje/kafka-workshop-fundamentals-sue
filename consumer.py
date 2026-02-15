import json
from confluent_kafka import Consumer

conf = {
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'workshop-group-1',
    'auto.offset.reset': 'earliest' # Begin bij het begin als er geen offset is
}

consumer = Consumer(conf)
topic = 'bestellingen'

consumer.subscribe([topic])

print(f"Luisteren naar topic '{topic}'... (CTRL+C om te stoppen)")

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        # Decodeer de bytes terug naar tekst/json
        value = msg.value().decode('utf-8')
        data = json.loads(value)

        print(f"Ontvangen: {data['klant_naam']} kocht voor €{data['bestel_bedrag']}")

except KeyboardInterrupt:
    print("Consumer gestopt.")
finally:
    consumer.close()
