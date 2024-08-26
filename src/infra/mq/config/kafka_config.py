# infra/mq/config/kafka_config.py

class KafkaConfig:
    BOOTSTRAP_SERVERS = [
        'localhost:9092',
        'broker2:9092'  #
    ]

    TOPICS = {
        'input_topic': 'input_topic_name',
        'output_topic': 'output_topic_name'
    }

    PRODUCER_CONFIG = {
        'acks': 'all',
        'retries': 5,
        'batch_size': 16384,
        'linger_ms': 10,
        'buffer_memory': 33554432
    }

    CONSUMER_CONFIG = {
        'group_id': 'my_consumer_group',
        'auto_offset_reset': 'earliest',
        'enable_auto_commit': True,
        'auto_commit_interval_ms': 1000
    }

    @staticmethod
    def get_producer_config():
        return KafkaConfig.PRODUCER_CONFIG

    @staticmethod
    def get_consumer_config():
        return KafkaConfig.CONSUMER_CONFIG

    @staticmethod
    def get_topics():
        return KafkaConfig.TOPICS

    @staticmethod
    def get_bootstrap_servers():
        return KafkaConfig.BOOTSTRAP_SERVERS
