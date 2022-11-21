# ipset
A collection of IP address prefixes grouped together for a specific purpose. If you know a prefix that is missing please submit an issue.

## Install
```
$ git clone https://github.com/PeymanHR/ipset.git
$ cd ipset
```
## Generate IP address list configuration
You can generate ip address list configuration for **ipset**, **mikrotik**, **apache**, **nginx** and **cisco**
```
cat prefixes/<path_to_prefixes_file> | python3 bin/prefix_list_processor.py <format> --name <name>
```
### example 1:
```
cat prefixes/iran/iran_prefixes.txt | python3 bin/prefix_list_processor.py cisco
```
#### output:
```
permit 2.144.0.0/14 0.3.255.255
permit 2.176.0.0/12 0.15.255.255
permit 5.1.43.0/24 0.0.0.255
permit 5.104.208.0/21 0.0.7.255
...
```
### example 2:
```
cat prefixes/iran/iran_prefixes.txt | python3 bin/prefix_list_processor.py mikrotik --name ir
```
#### output:
```
add address=2.144.0.0/14 list=ir
add address=2.176.0.0/12 list=ir
add address=5.1.43.0/24 list=ir
add address=5.104.208.0/21 list=ir
...
```
## Lookup an IP address in a prefixes file

```
$ python3 bin/lookup.py prefixes/<path_to_prefixes_file> <ip address>
```
### example:
```
$ python3 bin/lookup.py prefixes/iran/iran_prefixes.txt 5.210.205.201
```
#### output:
```
5.210.0.0/16
```