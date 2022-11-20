# ipset
A collection of IP address prefixes grouped together for a specific purpose. If you know a prefix that is missing please submit an issue.

## Lookup an IP address in a prefixes file

```
$ git clone https://github.com/PeymanHR/ipset.git
$ cd ipset
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