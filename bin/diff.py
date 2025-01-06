# Copyright (c) 2022 peymanhr <phooshmand@gmail.com>

from ipaddress import ip_address, ip_network
from sys import stdin
import argparse
from argparse import RawTextHelpFormatter

def lookup(ipaddress, prefix_list):
    for prefix in prefix_list:
        network = ip_network(prefix)
        if ipaddress in network:
            return network


parser = argparse.ArgumentParser(
    prog = "python3 diff.py",
    description = "Compare prefixes read from STDIN to a prefix file",
    epilog = "Copyright (c) 2022 peymanhr <phooshmand@gmail.com>",
    formatter_class=RawTextHelpFormatter)

parser.add_argument("-f", type=str,
                    help="FILE")

args = parser.parse_args()

prefixes_a = [x for x in stdin.read().splitlines() if x.strip()]

with open(args.f) as f:
    prefixes_b = [x for x in f.read().splitlines() if x.strip()]

diff = [ip_network(x) for x in prefixes_b if x not in prefixes_a]


for i, prefix in enumerate(diff):

    if prefix.num_addresses > 1:
        first = next(prefix.hosts())
        print(f"{i + 1} - {prefix}")
        print(f"{lookup(first, prefixes_a)} ({first})")
        print(f"{lookup(prefix.broadcast_address, prefixes_a)} ({prefix.broadcast_address})", end="\n\n")
    else:
        print(prefix)
        print(f"{lookup(prefix.broadcast_address, prefixes_a)} ({prefix.broadcast_address})", end="\n\n")




# for prefix in stdin:
#     prefix = prefix.strip()
#     if prefix:
#         pass
#         # network = ip_network(prefix.strip())
#         # if ip_address(args.ip) in network:
#         #     print(network)
