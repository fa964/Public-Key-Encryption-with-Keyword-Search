from Crypto.PublicKey import RSA

def key_gen():
    keywords = open('keywords.txt', 'r')
    counter  = 0
    for word in keywords:
        print(word)
        counter += 1
    
        # Generate Private and Public Key Pair
        key = RSA.generate(2048)
        # Generate Encrypted Private Key File
        private_key = key.export_key()
        file_name = "private_key_{0}.pem"
        file_out = open(file_name.format(counter), "wb")
        file_out.write(private_key)
        file_out.close()

        # Generate Public Key File
        public_key = key.publickey().export_key()
        file_name = "public_key_{0}.pem"
        file_out = open(file_name.format(counter), "wb")
        file_out.write(public_key)
        file_out.close()

        

if __name__ == '__main__':
    key_gen()
    print("Done")
