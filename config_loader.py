import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'settings.yaml')
    with open(config_path, 'r') as file:
        settings_data = yaml.safe_load(file)
    return settings_data
