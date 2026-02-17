import time, json, random
from confluent_kafka import Producer
from faker import Faker

conf = {'bootstrap.servers': 'localhost:29092', 'client.id': 'python-producer'}
producer = Producer(conf)
faker = Faker('nl_NL')
topic = 'bestellingen'

print(f"Producer gestart. Stuurt data naar '{topic}'...")

try:
    while True:
        data = {
            'klant': faker.name(),
            'stad': faker.city(),
            'bedrag': round(random.uniform(10, 100), 2)
        }
        producer.produce(topic, key=data['stad'], value=json.dumps(data))
        producer.poll(0)
        time.sleep(1)
        print(f"Verzonden: {data}")
except KeyboardInterrupt:
    pass
finally:
    producer.flush()