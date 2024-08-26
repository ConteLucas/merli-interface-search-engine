import yaml

from src.domain.utils.constants.file_system_constant import FileSystemConstant


class ConfigFilesUtil:
    def __init__(self):
        self.environment = FileSystemConstant.ENV
        self.dir = FileSystemConstant.DIR
        self.config_file = f'{self.dir}config/values_{self.environment}.yaml'
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def get(self, key: str):
        keys = key.split('.')
        config = self.config
        for k in keys:
            config = config.get(k)
            if config is None:
                return None
        return config

    def get_link(self, key: str):
        return self.get(key)
