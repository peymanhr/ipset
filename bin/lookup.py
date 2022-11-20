from ipaddress import ip_network
from sys import argv

prefix_file = argv[1]
ip_address = argv[2]

with open (prefix_file) as f:
    for prefix in f:
        prefix = prefix.strip()
        if prefix:
            network = ip_network(prefix.strip())
            if ip_address in [str(x) for x in network]:
                print(network)
