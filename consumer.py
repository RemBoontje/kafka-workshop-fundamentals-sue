import json
from confluent_kafka import Consumer

conf = {
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'workshop-group-1',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['bestellingen'])

print("Consumer gestart...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None: continue
        if msg.error():
            print(f"Error: {msg.error()}")
            continue

        data = json.loads(msg.value().decode('utf-8'))
        print(f"Ontvangen uit partitie {msg.partition()}: {data['klant']} uit {data['stad']}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()