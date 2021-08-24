# Copyright (C) 2021 Dmitry Dmitriev

# dependencies:
#   pip install --user pipenv

import sys
import logging
import os
from privex.jsonrpc import JsonRPC, RPCException

logging.basicConfig(format='%(levelname)s:\t%(message)s', level=logging.DEBUG)

# API key for https://nownodes.io/
secret_api_key = os.environ.get('NOWNODES_API_KEY')
if secret_api_key == None or secret_api_key == "":
    logging.critical("API key must be set in env variable NOWNODES_API_KEY")
    exit(1)


def main(argv):
    logging.info("I'm started")

    NOWNodes = JsonRPC(hostname="eth.nownodes.io", port=443, ssl=True, url=secret_api_key)

    gasPrice = NOWNodes.eth_gasPrice()
    logging.info(gasPrice)


if __name__ == '__main__':
    main(sys.argv[1:])
