# This file contains unit tests for AddrValid library functionality
#
# Author: Josh McIntyre
#
import unittest
import os

import addrvalid

class TestAddrValid(unittest.TestCase):
    
    def test_validate_digibyte(self):
        
        DIR = "./test"

        addresses = []
        address_files = [ f for f in os.listdir(DIR) if (os.path.isfile(os.path.join(DIR,f)) and os.path.join(DIR,f).endswith(".txt")) ]
        
        for filename in address_files:
            with open(os.path.join(DIR, filename)) as f:
                address = f.read().strip()
                valid = addrvalid.validate_digibyte(address)

                assert valid