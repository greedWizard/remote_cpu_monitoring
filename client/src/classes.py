import requests
import json
import psutil
import time
import logging


class Sender:
    def _get_cpu_load(self):
        s = 0
        core = psutil.cpu_percent(interval=1)

        return round(core, 2)

    def __init__(self, config_path: str):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)

        self.timeout = config['timeout']
        self.url = config['url']
        self.connection_tries = config['connection_tries']

        self.logger = logging.getLogger('client-data')
        self.logger.addHandler(logging.FileHandler('info.log'))
        self.logger.setLevel(logging.INFO)

    def send_cpu_load(self):
        try:
            cpu_load =self._get_cpu_load()
            response = requests.post(
                url=self.url,
                data={
                    'cpu_load': cpu_load,
                }
            )
            self.logger.info(f'Sent cpu load:\t{cpu_load}')
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(str(e))

            if self.connection_tries == 0:
                raise SystemError(f'Could not connect to the server {self.url}')
            self.connection_tries -= 1
    
    def start_sending(self):
        while True:
            response = self.send_cpu_load()
            time.sleep(self.timeout)