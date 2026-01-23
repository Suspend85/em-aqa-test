import platform
import sys

from config import settings

def create_allure_environment_file():
    platform_items = [
        f'OS={platform.system()}, {platform.version()}',
    ]
    interpretator_ver = [
        f'Python.Version={sys.version}'
    ]
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(platform_items + interpretator_ver + items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+', encoding='utf-8') as file:
        file.write(properties)