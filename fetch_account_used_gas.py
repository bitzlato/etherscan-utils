# Copyright (C) 2021 Dmitry Dmitriev

# dependencies:
#   pip install --user pipenv

import logging
import os
import sys

import etherscan

from decimal import *

getcontext().prec = 18

logging.basicConfig(format='%(levelname)s\t| %(message)s', level=logging.INFO)


def get_accounts_from_file():
    accounts = []
    with open("accounts_list.txt") as file:
        for line in file:
            if line == "":
                continue
            accounts.append(line.strip())

    logging.info("got " + str(len(set(accounts))) + " accounts")
    return set(accounts)


def get_account_fees(account):
    data = etherscan.account_normal_transactions(account)

    # Calculate transaction fee
    fees = {}
    for item in data:
        logging.debug(item)
        gas_price = int(item["gasPrice"])
        gas_used = int(item["gasUsed"])

        if item["contractAddress"] != "":
            logging.warning("found contract address " + item["contractAddress"])

        if item["isError"] != "0":
            logging.debug("isError is set for " + item["hash"])

        if item["from"] != account:
            logging.debug("incoming tx " + item["hash"] + " not from our account")
            continue

        current_fee = gas_price * gas_used
        logging.debug(str(gas_price/etherscan.ETH_CURRENCY_PARTS) + ", " +
                      str(gas_used/etherscan.ETH_CURRENCY_PARTS) + ", " +
                      str(current_fee/etherscan.ETH_CURRENCY_PARTS))

        contract_address = "empty"
        if item["contractAddress"] != "":
            contract_address = item["contractAddress"]

        fees[item["hash"]] = {
            "fee": current_fee / etherscan.ETH_CURRENCY_PARTS,
            "fee_gwei": current_fee,
            "contract": contract_address,
        }

    return fees


def main(argv):
    logging.info("I'm started")

    accounts = get_accounts_from_file()
    logging.debug(accounts)

    results = {}
    acc_idx = 1
    for account in accounts:
        logging.info("[" + str(acc_idx) + "/" + str(len(accounts)) +
                     "] calculate fee for account " + account)

        results[account] = get_account_fees(account)
        acc_idx += 1

    with open("result.csv", "w") as csv_file:
        csv_file.write("address, tx, contract, fee\n")

        total_fee = 0
        for result in results:
            for transaction in results[result]:
                total_fee += results[result][transaction]["fee_gwei"]
                csv_file.write(result + ", " +
                               str(transaction) + ", " +
                               str(results[result][transaction]["contract"]) + ", " +
                               str(results[result][transaction]["fee_gwei"]) +
                               os.linesep)
                               
        print(Decimal(total_fee) / Decimal(etherscan.ETH_CURRENCY_PARTS))


if __name__ == '__main__':
    main(sys.argv[1:])
