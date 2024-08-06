import binascii

# Example data to encode/decode
data = b"Hello, World!"
hex_data = b"48656c6c6f2c20576f726c6421"
base64_data = b"SGVsbG8sIFdvcmxkIQ=="

# Hexlify: Convert binary data to hexadecimal representation
hex_encoded = binascii.hexlify(data)
print("Hexlify:", hex_encoded)

# Unhexlify: Convert hexadecimal data to binary representation
hex_decoded = binascii.unhexlify(hex_encoded)
print("Unhexlify:", hex_decoded)

# a2b_base64: Decode base64-encoded data
base64_decoded = binascii.a2b_base64(base64_data)
print("Base64 Decoded:", base64_decoded)

# b2a_base64: Encode binary data in base64 format
base64_encoded = binascii.b2a_base64(data, newline=True)
print("Base64 Encoded:", base64_encoded)
