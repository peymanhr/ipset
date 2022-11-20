# ipset
A collection of IP address prefixes grouped together for a specific purpose

## Lookup an IP address in a prefixes file

```
python3 bin/lookup.py prefixes/<path_to_prefixes_file> <ip address>
```

### example:
```
python3 bin/lookup.py prefixes/iran/iran_prefixes.txt 5.210.205.201
```