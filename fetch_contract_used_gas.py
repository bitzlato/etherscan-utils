#!/usr/bin/env python3 

import argparse
import logging
import statistics
import sys
import textwrap

from decimal import *
from libs.etherscan import *

getcontext().prec = 18

logging.basicConfig(format='%(levelname)s\t| %(message)s', level=logging.INFO)


def main(argv):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Etherscan utility for fetching gas used by a contract.\n
            Note that environment variable ETHERSCAN_KEY must be set
        '''))
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('-b', default=10, type=int, metavar='blocks_count',
                        help='sets number of analyzed blocks (10 by default)')
    parser.add_argument('addresses', action='extend', nargs='+', type=str)

    args = vars(parser.parse_args(argv))

    # begin processing
    print('contract_address', 'min', 'med', 'max', sep='\t')
    for address in args['addresses']:
        transactions = account_token_transfers(address)
        latest_transactions = transactions[-int(args['b']):]

        logging.debug('process ' + str(len(latest_transactions)) + ' latest transactions')
        gas_used_list = [int(x['gasUsed']) for x in latest_transactions]
        print(address, min(gas_used_list), int(statistics.median(
            gas_used_list)), max(gas_used_list), sep='\t')


if __name__ == '__main__':
    main(sys.argv[1:])
