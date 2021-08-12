import requests
import json
import psutil
import time


class Sender:
    def _get_cpu_load(self):
        return psutil.cpu_percent(interval=1, percpu=True)[0]

    def __init__(self, config_path: str):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)

        self.timeout = config['timeout']
        self.url = config['url']

    def send_cpu_load(self):
        response = requests.post(
            url=self.url,
            data={
                'cpu_load': self._get_cpu_load()
            }
        )
        return response
    
    def start_sending(self):
        while True:
            response = self.send_cpu_load()
            print(response)
            time.sleep(self.timeout)