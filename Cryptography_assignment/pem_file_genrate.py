from Crypto.PublicKey import RSA

# Generate an RSA key
key = RSA.generate(2048)

# Create and write the PEM file
with open('9586.pem', 'wb') as file: 
    file.write(key.export_key('PEM'))