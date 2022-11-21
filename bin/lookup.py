# Copyright (c) 2022 peymanhr <phooshmand@gmail.com>

from ipaddress import ip_address, ip_network
from sys import stdin
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(
    prog = "python3 lookup.py",
    description = "IP address lookup in prefixes read from STDIN",
    epilog = "Copyright (c) 2022 peymanhr <phooshmand@gmail.com>",
    formatter_class=RawTextHelpFormatter)

parser.add_argument("ip", type=str,
                    help="ip address")

args = parser.parse_args()

for prefix in stdin:
    prefix = prefix.strip()
    if prefix:
        network = ip_network(prefix.strip())
        if ip_address(args.ip) in network:
            print(network)
