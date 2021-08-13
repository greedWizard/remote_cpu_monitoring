print('starting')

from classes import Sender
import os


def main():
    config_path = os.environ.get('CLIENT_CONFIG', 'config.json')

    sender = Sender(config_path)
    sender.start_sending()


if __name__ == '__main__':
    main()