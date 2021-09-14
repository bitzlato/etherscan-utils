# Etherscan helpers

import logging
import os
import requests


ETH_CURRENCY_PARTS = 1_000_000_000_000_000_000

url = "https://api.etherscan.io/api"


def __test_resp(data):
    if 'result' not in data or 'message' not in data:
        logging.critical("incorrect server response: " + str(data))
        return False

    if data['message'] == "NOTOK":
        logging.critical("error processing the request, resp: " + str(data))
        return False

    return True


def get_env_apikey():
    apikey = os.environ.get('ETHERSCAN_KEY')
    if apikey == None or apikey == "":
        logging.critical("ETHERSCAN_KEY environment variable is not set!\n")
        exit(1)
    return apikey


def account_normal_transactions(account):
    apikey = get_env_apikey()

    params = dict(
        module="account",
        action="txlist",
        address=account,
        startblock=0,
        endblock=99999999,
        sort="asc",
        apikey=apikey
    )
    resp = requests.get(url=url, params=params)

    if not __test_resp(resp.json()):
        exit(1)

    return resp.json()['result']


def contract_fees(contract):
    key = get_env_apikey()
