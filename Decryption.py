from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

def RSA_decryption(private_key_filename):
    file_in = open("encrypted_message.bin", "rb")
    private_key = RSA.import_key(open(private_key_filename).read())

    enc_session_key, nonce, tag, ciphertext = \
       [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
    file_in.close()

    try:
        #Correct Decypt
        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)

        #Output Data
        print(data.decode("utf-8"))
    except:
        print("Incorroect decryption.")

                   
if __name__ == '__main__':
    RSA_decryption("private_key_1.pem")
    print("Done")
