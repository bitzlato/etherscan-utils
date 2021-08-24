# Copyright (C) 2021 Dmitry Dmitriev

# dependencies:
#   pip install --user pipenv

import logging
import os
import sys
import time

import requests

logging.basicConfig(format='%(levelname)s\t\t| %(message)s', level=logging.DEBUG)

# API key for https://nownodes.io/
secret_api_key = os.environ.get('ETHERSCAN_API_KEY')
if secret_api_key == None or secret_api_key == "":
    logging.critical("API key must be set in env variable ETHERSCAN_API_KEY")
    exit(1)


url = "https://api.etherscan.io/api"


def get_accounts_from_file():
    accounts = []
    with open("accounts_list.txt") as file:
        for line in file:
            if line == "":
                continue
            accounts.append(line.strip())

    logging.info("got " + str(len(set(accounts))) + " accounts")
    return set(accounts)


def get_account_fee(account):
    logging.debug("----------------------------------------------")
    logging.info("calculate fee for account " + account)

    params = dict(
        module="account",
        action="txlist",
        address=account,
        startblock=0,
        endblock=99999999,
        sort="asc",
        apikey=secret_api_key
    )
    resp = requests.get(url=url, params=params)
    data = resp.json()

    logging.debug("server resp is '" + data["message"] + "'")

    if "result" not in data:
        logging.critical("incorrect server response: " + str(data))
        exit(1)
    if data["message"] == "NOTOK":
        logging.critical("error processing request, resp: " + str(data))
        exit(1)

    fee = 0
    for item in data["result"]:
        gas_price = int(item["gasPrice"], 16)
        gas_used = int(item["gasUsed"], 16)

        fee += gas_price * gas_used
        logging.debug(str(gas_price) + ", " + str(gas_used) + ", " + str(fee))

    return fee


def main(argv):
    logging.info("I'm started")

    accounts = get_accounts_from_file()
    logging.debug(accounts)

    results = {}
    for account in accounts:
        results[account] = get_account_fee(account)
        logging.info("result is " + str(results[account]))
        time.sleep(0.2)

    with open("result.txt", "w") as csv_file:
        for result in results:
            csv_file.write(result + ", " + str(results[result]) + os.linesep)


if __name__ == '__main__':
    main(sys.argv[1:])
