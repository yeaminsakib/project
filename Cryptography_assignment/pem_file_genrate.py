from Crypto.PublicKey import RSA

# Generate an RSA key
key = RSA.generate(2048)

# Create and write the PEM file
with open('9586.pem', 'wb') as file:  # Replace 12345678 with your student number
    file.write(key.export_key('PEM'))