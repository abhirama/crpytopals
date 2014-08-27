import binascii
import base64

hex_string='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

binary_string = binascii.unhexlify(hex_string)

print 'Unhexificed string is - ', binary_string

encoded_string = base64.b64encode(binary_string)

print 'Base 64 encoded string is - ', encoded_string


