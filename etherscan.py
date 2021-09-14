# Etherscan helpers

import logging
import os
import requests


ETH_CURRENCY_PARTS = 1_000_000_000_000_000_000

url = "https://api.etherscan.io/api"


def get_env_apikey():
    apikey = os.environ.get('ETHERSCAN_KEY')
    if apikey == None or apikey == "":
        logging.critical("API key must be set in env variable ETHERSCAN_API_KEY")
        raise Exception("apikey not set in the environment")
    return apikey


def account_fees(apikey, url, account):
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
    return resp.json()
