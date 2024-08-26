import json
from kafka import KafkaProducer


class KafkaService:
    def __init__(self, config_files_util):
        self.config_util = config_files_util
        self.producer = KafkaProducer(
            bootstrap_servers=self.config_util.get('BOOTSTRAP_SERVER'),
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_to_kafka(self, topic: str, payload: str):
        self.producer.send(topic, value=payload)
        self.producer.flush()
