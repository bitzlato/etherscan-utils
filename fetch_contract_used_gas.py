import etherscan
import getopt
import logging
import sys

from decimal import *


getcontext().prec = 18

logging.basicConfig(format='%(levelname)s\t\t| %(message)s', level=logging.INFO)


def version():
    print("Etherscan utility for fetching gas used by a contract, v.0.1\n")
    print("Dmitry Dmitriev 2021")
    print("dmitriev.dd@hotmail.com")


def help():
    print("Etherscan utility for fetching gas used by a contract")
    print("This utility expecting apikey in ETHERSCAN_KEY environment variable\n")
    print("Expected parameters:")
    print("\t-b - sets number of analyzed blocks (10 by default)")
    print("\tSpace-separated list of contract addresses\n")
    print("Example:")
    print("\tETHERSCAN_KEY=123 ./fetch_used_gas -b 10 0x123 0x456 0x789")


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hv", ["version", "help"])
    except getopt.GetoptError:
        help()
        exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
            exit()
        elif opt in ("-v", "--version"):
            version()
            exit()


if __name__ == '__main__':
    main(sys.argv[1:])
