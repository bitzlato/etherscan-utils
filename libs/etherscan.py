# Etherscan helpers

import logging
import os
import requests


ETH_CURRENCY_PARTS = 1_000_000_000_000_000_000

url = "https://api.etherscan.io/api"


def get_env_apikey():
    apikey = os.environ.get('ETHERSCAN_KEY')
    if apikey == None or apikey == "":
        logging.critical("ETHERSCAN_KEY environment variable is not set!\n")
        exit(1)
    return apikey


def __test_resp(data):
    if 'result' not in data or 'message' not in data:
        logging.critical("incorrect server response: " + str(data))
        return False

    if data['message'] == "NOTOK":
        logging.critical("error processing the request, resp: " + str(data))
        return False

    return True


def __make_request(params):
    resp = requests.get(url=url, params=params)
    if not __test_resp(resp.json()):
        exit(1)

    return resp.json()['result']


# https://docs.etherscan.io/api-endpoints/accounts#get-a-list-of-normal-transactions-by-address
def account_normal_transactions(account):
    apikey = get_env_apikey()
    return __make_request(dict(
        module="account",
        action="txlist",
        address=account,
        startblock=0,
        endblock=99999999,
        sort="asc",
        apikey=apikey
    ))


# https://docs.etherscan.io/api-endpoints/accounts#get-a-list-of-erc20-token-transfer-events-by-address
def account_token_transfers(contract_address="", address=""):
    apikey = get_env_apikey()

    params = dict(
        module="account",
        action="tokentx",
        sort="asc",
        apikey=apikey
    )
    if not contract_address and not address:
        logging.critical("contract_address or address must be set!")
        exit(1)

    if contract_address:
        params['contractaddress'] = contract_address
    if address:
        params['address'] = address

    return __make_request(params)
