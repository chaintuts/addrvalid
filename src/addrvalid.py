# A simple crypto address validation library
#
# Author: Josh McIntyre
#
import base58
import hashlib

# Validate a Digibyte address
def validate_digibyte(address):
    
    # Address must be valid 58
    try:
        raw_address = base58.b58decode(address)
    except ValueError:
        return False
        
    # Legacy DGB addresses are between 33 - 35 characters usually
    # This figure might be slightly off, IIRC most are 34 characters
    if len(address) < 33 or len(address) > 35:
        return False

    # Validate the checksum
    checksum_bits = raw_address[-4:]
    address_bits = raw_address[:-4]
    
    checksum_round1 = hashlib.sha256(address_bits).digest()
    checksum_round2 = hashlib.sha256(checksum_round1).digest()
    checksum = checksum_round2[:4]
    
    if checksum != checksum_bits:
        return False
    
    return True
