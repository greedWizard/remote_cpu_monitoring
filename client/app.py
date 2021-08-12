import requests
from classes import Sender


def main():
    sender = Sender('config.json')

    sender.start_sending()


if __name__ == '__main__':
    main()