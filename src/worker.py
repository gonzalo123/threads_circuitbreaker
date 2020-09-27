from Listener import Listener
from dotenv import load_dotenv
import logging
from time import sleep
import os

logging.basicConfig(level=logging.INFO)

current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(dotenv_path="{}/.env".format(current_dir))

l = Listener()
l.start()


def main():
    while True:
        logging.info("*")
        sleep(1)
        if l.stop():
            break


if __name__ == '__main__':
    main()
