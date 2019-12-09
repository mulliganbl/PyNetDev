#!/usr/bin/env python
from __future__ import print_function

try:
    ip_addr1 = raw_input("Enter an IP address: ")
except NameError:
    ip_addr1 = input("Enter an IP address: ")
print(ip_addr1)

