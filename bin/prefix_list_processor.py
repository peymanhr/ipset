# Copyright (c) 2022 peymanhr <phooshmand@gmail.com>

from sys import stdin
from ipaddress import ip_network
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(
    prog = "Prefix List Processor",
    description = "Generate IP address list configuration for different formats. from STDIN",
    epilog = "Copyright (c) 2022 peymanhr <phooshmand@gmail.com>",
    formatter_class=RawTextHelpFormatter)

parser.add_argument("format", type=str,
                    help="ipset mikrotik apache nginx cisco")

parser.add_argument("-n", "--name", type=str, required=False,
                    help="address list name or access list number")

parser.add_argument("--negate", action="store_true",
                    help="negate")

args = parser.parse_args()

for prefix in stdin:
    if prefix not in ["\r\n", "\n"]:
        if args.format == 'ipset':    
            print(f"ipset add {args.name} {prefix.strip()}", end="\n")

        elif args.format == 'mikrotik':
            print(f"add address={prefix.strip()} list={args.name}", end="\r\n")

        elif args.format == 'apache':
            print(f"Require {'not ' if args.negate else '' }ip {prefix.strip()}", end="\n")

        elif args.format == 'nginx':
            print(f"{'Deny' if args.negate else 'Allow'} {prefix.strip()};", end="\n")

        elif args.format == 'cisco':
            prefix = prefix.strip()
            print(f"{'deny' if args.negate else 'permit'} {prefix} {ip_network(prefix).hostmask}", end="\n")
